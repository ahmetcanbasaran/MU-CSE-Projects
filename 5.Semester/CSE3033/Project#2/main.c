#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <memory.h>
#include <wait.h>
#include <dirent.h>
#include <ctype.h>
#include <fcntl.h>      // For non-blocking reading support.
#include <limits.h>     // For INT_MAX.
#include "LinkedList.h" // Our linked list code.
#include <termios.h>    // For up and down arrow keys detection.


#define MAX_LINE 80 /* 80 chars per line, per command, should be enough. */

char path[MAX_LINE];        // To hold command's path
int success = 0;            // To check whether path is found
LinkedList cmdHistory = { NULL, NULL }; // LL to hold command history.

// To access functions easily
enum command_state {

    BOOKMARK,
    CODESEARCH,
    PRINT,
    SET,
    EXIT,
    COMMAND

};

enum RedirectionType{

    Default         = 1,
    StdOutTruncate  = 2,
    StdOutAppend    = 4,
    StdIn           = 8,
    StdErr          = 16

};

// To hold command names into char pointers
const char *Bookmark = "bookmark";
const char *CodeSearch = "codesearch";
const char *Set = "set";
const char *Print = "print";
const char *Exit = "exit";
const char *Command = "command";

// Function Prototypes.
enum command_state command(char *input);
int  createChildProcess( char* args[], int background );
int  redirect( char* file, int redirectionDest, int flags, int mode );
int  redirection(enum RedirectionType type, char *inFile, char *outFile);
void bookmark( char* args[], LinkedList* bookmarks );
int  setup( char inputBuffer[], char *args[], int *background, int justParse );
void pathing(char *args[]);
void removeCharacters( char* str, char c );
void codesearch(const char *dir_name, int indent, char *args[]);
void print(int argc, char **args, char **envp);
void set(int argc, char *args[], int background);
void exitProgram(int argc, char **argv, char **envp);
void setTerminalModes( struct termios* canonicalMode, struct termios* nonCanonicalMode );

void setTerminalModes( struct termios* canonicalMode, struct termios* nonCanonicalMode )
{
    // Get the terminal settings for stdin.
    tcgetattr( STDIN_FILENO, canonicalMode );

    // We want to keep the old setting (canonical) to restore them later on.
    *nonCanonicalMode = *canonicalMode;

    // Disable canonical mode (buffered i/o) and local echo for new setting.
    nonCanonicalMode->c_lflag &= ( ~ICANON & ~ECHO );
}

enum command_state command(char *input){

    if(command != NULL){

        //strcmp returns 0 if two char array are equal
        if(!strcmp(input, Bookmark))
            return BOOKMARK;

        else if(!strcmp(input, CodeSearch))
            return CODESEARCH;

        else if(!strcmp(input, Set))
            return SET;

        else if(!strcmp(input, Print))
            return PRINT;

        else if(!strcmp(input, Exit))
            return EXIT;

        else
            return COMMAND;     // To run normal linux terminal commands

    }

    perror("No command entered!\n");
    exit(EXIT_FAILURE);

}

// Removes all occurences of the given character from given string.
void removeCharacters( char* str, char c )
{
    char *readPtr  = str;
    char* writePtr = str;
    while( *readPtr )
    {
        *writePtr = *readPtr++; // Overwrite the char at writePtr with the char at readPtr.
        // Don't move writePtr if we encountered c. It'll get overwritten next iteration.
        writePtr += (*writePtr != c );
    }
    *writePtr = '\0';
}

int createChildProcess(char* args[], int background){

    pid_t childpid;
    int i;                         // Loop index variable.
    enum RedirectionType redType = Default;
    char* inFile  = NULL;
    char* outFile = NULL;
    int firstRedirOpPos = INT_MAX; // Keeps the position of the first redirection operator.

    //(1) fork a child process using fork()
    if( ( childpid = fork() ) == -1 )
    {
        perror( "Failed to fork" );
        return 1;
    }

    //(2) the child process will invoke execv()
    if( childpid == 0 ){    // Child thread
        // To find path of command
        pathing(args);

        // To add "/<command_name>"
        strcat(path, "/");
        strcat(path, args[0]);

        // REDIRECTION.
        // Find out if args has one or two of these: { "<", ">", ">>", "2>" }.
        for( i = 0; args[ i ] != NULL; i++ )
        {
            if( strcmp( args[ i ], ">" ) == 0 )
            {
                redType |= StdOutTruncate;
                outFile = args[ i + 1 ];
                firstRedirOpPos = i < firstRedirOpPos ? i : firstRedirOpPos;
            }
            if( strcmp( args[ i ], ">>" ) == 0 )
            {
                redType |= StdOutAppend;
                outFile = args[ i + 1 ];
                firstRedirOpPos = i < firstRedirOpPos ? i : firstRedirOpPos;
            }
            if( strcmp( args[ i ], "<" ) == 0 )
            {
                redType |= StdIn;
                inFile = args[ i + 1 ];
                firstRedirOpPos = i < firstRedirOpPos ? i : firstRedirOpPos;
            }
            if( strcmp( args[ i ], "2>" ) == 0 )
            {
                redType |= StdErr;
                outFile = args[ i + 1 ];
                firstRedirOpPos = i < firstRedirOpPos ? i : firstRedirOpPos;
            }
        }

        if( redType != Default )
        {
            printf( "inFile: %s\noutFile: %s\n", inFile, outFile );
            args[ firstRedirOpPos ] = ( char * )NULL; // By setting it to NULL, we limit args to arguments priot to it in execv().
            redirection( redType, inFile, outFile );
        }

        execv( path, args );
        perror( "Child process failed upon running execv() function." );
    }

    //(3) if background == 0, the parent will wait, otherwise it will invoke the setup () function again.
    if( background != 1 )
    {
        if( childpid != wait( NULL ) ) // Parent thread
        {
            perror( "Parent failed to wait due to signal or error" );
            return 1;
        }
    }

    return 0;
}

// Handles the redirection of redirectionDest with given file, flags and mode.
int redirect( char* file, int redirectionDest, int flags, int mode )
{
    int fileDesc;

    // 1. Open the file.
    fileDesc = open( file, flags, mode );
    if( fileDesc == -1 )
    {
        fprintf( stderr, "Failed to open the file." );
        return 1;
    }
    // 2. Duplicate the desired descriptor.
    if( dup2( fileDesc, redirectionDest ) == -1 )
    {
        switch( redirectionDest )
        {
            case STDIN_FILENO:
                fprintf( stderr, "Failed to redirect STDIN." );
                break;
            case STDOUT_FILENO:
                fprintf( stderr, "Failed to redirect STDOUT." );
                break;
            case STDERR_FILENO:
                fprintf( stderr, "Failed to redirect STDERR." );
                break;
        }
        return 1;
    }
    // 3. Close the file since we don't need it anymore.
    if( close( fileDesc ) == -1 )
    {
        fprintf( stderr, "Failed to close the file." );
        return 1;
    }
}

// Handles redirection off all supported kinds.
int redirection( enum RedirectionType type, char *inFile, char *outFile )
{
    int writingMode = S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH;
    int readingMode = S_IRUSR | S_IRGRP | S_IROTH;
    int result = 0;

    if( type & StdOutTruncate )
    {
        result = redirect( outFile, STDOUT_FILENO, O_WRONLY | O_CREAT | O_TRUNC,  writingMode );
    }
    else if( type & StdOutAppend )
    {
        result = redirect( outFile, STDOUT_FILENO, O_WRONLY | O_CREAT | O_APPEND, writingMode );
    }

    if( type & StdIn )
    {
        result = redirect( inFile,  STDIN_FILENO,  O_RDONLY,                      readingMode );
    }

    if( type & StdErr )
    {
        result = redirect( outFile, STDERR_FILENO, O_WRONLY | O_CREAT | O_APPEND, writingMode );
    }

    return result;
}

// Bookmarks (and accesses, executes or removes) commands.
void bookmark( char* args[], LinkedList* bookmarks )
{
    int   i;                                   // Loop index variable.
    int   commandIndex;                        // Index of the command to exec/delete.
    int   numArgs;                             // Number of arguments.
    char  commandStr[ MAX_LINE ] = { 0 };      // Command string.
    char* commandArgs[ ( MAX_LINE / 2 ) + 1 ]; // Command line arguments.
    int   background = 0;                      // Whether the command will be run on background or not.

    if( strcmp( args[ 1 ], "-l" ) == 0 )       // -l means list all bookmarked commands
    {
        if( bookmarks->header == NULL )
        {
            fprintf( stderr, "Bookmark: Currently there are no bookmarked commands!\n" );
        }
        else
        {
            PrintLinkedList( bookmarks, 1 );
        }
    }
    else if( strcmp( args[ 1 ], "-i" ) == 0 ) // -i means execute the command at given index.
    {
        commandIndex = atoi( args[ 2 ] ); // Second argument is the command to execute.
        if( bookmarks->header == NULL )
        {
            fprintf( stderr, "Bookmark: Currently there are no bookmarked commands!\n" );
        }
        else
        {
            if( commandIndex > GetLinkedListSize( bookmarks ) ) // Bounds checking.
            {
                fprintf( stderr, "Bookmark: Could not find command at index %d.\n", commandIndex );
            }
            else
            {
                // Find the data in the linked list and copy to a string.
                strcpy( commandStr, LocateData( bookmarks, commandIndex ) );

                // Parse that string into an argument array.
                numArgs = setup( commandStr, commandArgs, &background, 1 );

                // Remove quotation marks from first and last arguments.
                removeCharacters( commandArgs[ 0           ], '"' );
                removeCharacters( commandArgs[ numArgs - 1 ], '"' );

                // Check if the command will be run on background or not.
                background = strcmp( commandArgs[ numArgs - 1 ], "&" ) ? 1 : 0;

                // Create a child process to execute the command.
                createChildProcess( commandArgs, background );
            }
        }
    }
    else if( strcmp( args[ 1 ], "-d" ) == 0 ) // -d means delete the command at given index.
    {
        if( bookmarks->header == NULL )
        {
            fprintf( stderr, "Bookmark: Currently there are no bookmarked commands!\n\n" );
        }
        else
        {
            commandIndex = atoi( args[ 2 ] ); // Second argument is the command to delete.
            if( commandIndex > GetLinkedListSize( bookmarks ) )
            {
                fprintf( stderr, "Bookmark: Could not find command at index %d.\n", commandIndex );
            }
            else
            {
                RemoveFromLinkedList( bookmarks, commandIndex );
            }
        }
    }
    else // Add the command to the end of the list.
    {
        // Concatenate args to create the command's string.
        for( i = 1; args[ i ] != NULL; i++ )
        {
            if( i != 1 ) // Don't leave space before the first argument but leave spaces between others.
            {
                strcat( commandStr, " " );
            }
            strcat( commandStr, args[ i ] ); // Concatenate arguments.
        }

        // Check if the command is enclosed within quotation marks, print error otherwise.
        if( commandStr[ 0 ] != '"' || commandStr[ strlen( commandStr ) - 1 ] != '"' )
        {
            fprintf( stderr, "Bookmark: Commands should be surrounded by quotation marks (\"\").\n" );
        }
        else
        {
            InsertIntoLinkedList( bookmarks, commandStr );
        }
    }
}

// To find where the command is in paths of Linux
void pathing(char *args[]){

    FILE *pp;
    pp = popen("printenv PATH", "r");

    int i;  // Counter fo loops
    int a = 0, b = 0;   //For path array

    char *line;     // To hold readed lines
    char path_array[MAX_LINE][MAX_LINE];

    // Erase path characters
    for(i = 0; i < MAX_LINE; i++){
        path[i] = '\000';
    }

    // To search every lines until they finish
    if (pp != NULL) {

        for(i = 0; i < 1; i++) {

            char buf[1000];

            line = fgets(buf, sizeof buf, pp);

            if (line == NULL)
                break;

        }

    }

    // To divide obtained hold PATH into paths
    for(i  = 0; line[i] != '\n'; i++){

        if(line[i] == ':'){     // Paths are seperated with ':'

            path_array[a][b] = '\0';
            a++;
            b = 0;

        } else {

            path_array[a][b] = line[i];
            b++;

        }

    }

    // To obtain command from args array
    char command[MAX_LINE/2+1];
    strcpy(command, args[0]);

    // To erase '"' character from command
    if(command[0] == '"'){
        for(i = 0; i < strlen(command); i++)
            command[i] = command[i+1];
    }

    success = 0;    // Erase the success of finding path of command

    // To search every path in order to find command program
    for(i = 0; i < a & success == 0; i++){

        strcpy(path, path_array[i]);

        DIR *dirp = opendir(path_array[i]);
        struct dirent *sd;

        if( dirp == NULL )
            continue;

        while ((sd = readdir(dirp)) != NULL){

            if(!strcmp(sd -> d_name, command)) {
                success = 1;
                break;
            }

        }

        (void)closedir(dirp);

    }

    // If command program is not found in paths, print error
    if(success != 1)
        printf("PATH of obtained command cannot be found!\n");

    pclose(pp);

}

void codesearch(const char *dir_name, int indent, char *args[]){

    int rMode = 0, i = 0;          // rMode: Recursive mode, i: counter
    char *file_type;

    // If only "codesearch"
    if (args[1] == NULL){
        printf("Too few input for codesearch()\n");
        return;
    }

    // To check recursive mode searching
    if (strcmp(args[1], "-r") == 0) {
        rMode = 1;
    }

    // If only "codesearch -r"
    if (rMode == 1 && args[2] == NULL){
        printf("There is no argument to search!\n");
        return;
    }

    char word[MAX_LINE];    // To hold word which will be searched
    char pre_word[MAX_LINE];    // To hold searching word with '"' if it has

    for(i = 0; i < MAX_LINE; i++)   // Erase everything
        word[i] = pre_word[i] = '\000';

    // To hold what is the searching keyword index in args[]
    if (rMode == 0){
        i = 1;
    } else {
        i = 2;
    }

    int count = 0;

    // To erase '"' from searching keyword and if it contained with
    // many word, to concatenate them
    for(; args[i] != NULL; i++){

        strncpy(pre_word, args[i], strlen(args[i]));
        pre_word[strlen(args[i])] = '\0';

        if(strstr(pre_word, "\"") != NULL){
            printf("pre_word: %s\n", pre_word);
            removeCharacters(pre_word, '"');
        }

        if(count == 0){
            strcpy(word,pre_word);
        } else {
            strcat(word, " ");
            strcat(word, pre_word);
        }

        count++;

    }

    // Open directory and file pointer in order to search files in directory or directories
    FILE *fp;
    DIR *dir;
    struct dirent *d;

    // To open directory
    if (!(dir = opendir(dir_name)))
        return;

    // To run search in directory until it ends
    while ((d = readdir(dir)) != NULL) {

        if (d -> d_type == DT_DIR && rMode == 1) {

            char paths[1024];

            // To pass "." and ".." which means current and parrent directory in Linux
            if (strcmp(d->d_name, ".") == 0 || strcmp(d->d_name, "..") == 0) {
                continue;
            }

            snprintf(paths, sizeof(paths), "%s/%s", dir_name, d->d_name);

            // To continue searching recursively
            codesearch(paths, indent + 2, args);

        } else {    // No recursive search

            // To pass "." and ".." which means current and parrent directory in Linux
            if (strcmp(d->d_name, ".") == 0 || strcmp(d->d_name, "..") == 0) {
                continue;
            }

            // To divide file names from '.' in order to get file types
            file_type = strrchr(d->d_name, '.');

            if (file_type != NULL){

                if(strcmp(file_type, ".c") == 0 || strcmp(file_type, ".C") == 0 ||
                   strcmp(file_type, ".h") == 0 || strcmp(file_type, ".H") == 0){

                    fp = fopen(d->d_name, "r");

                    char *line;

                    // To read every line in file in order to find searching keyword
                    if (fp != NULL) {

                        for(i = 1; ; i++) {

                            char buf[1000];

                            line = fgets(buf, sizeof buf, fp);

                            if (line == NULL)
                                break;

                            if(strstr(line, word) != NULL)
                                printf("\t%d: %s/%s -> %s", i, dir_name, d->d_name, line);

                        }
                    }
                }
            }
        }
    }

    closedir(dir);

}

// To check whether a char is numeric
int numeric(char *input){

    while (*input) {
        if (isdigit(*input++) != 0)
            return 1;
    }

    return 0;

}

// To print a specific variable or all enviroment variables
void print(int argc, char **args, char **envp){

    // If input like this "print PWD PATH"
    if(args[2] != NULL){
        printf("Only 1 name of enviroment variables is allowed\n");
        return;
    }

    // To print a specific variable
    if(args[1] != NULL){

        if(numeric(args[1])){
            printf("Numeric input in not allowed!\n");      // If input like this "print 1" or "print 12"
            return;
        }

        char* pPath;

        removeCharacters(args[1], '"');     // Remove '"' from variable name

        pPath = getenv (args[1]);   // Read the value of enviromental variable

        // To print if it is not NULL
        if (pPath!=NULL)
            printf ("%s=%s\n", args[1], pPath);

    } else {        // To print all enviromental variables

        for (char **env = envp; *env != 0; env++){
            char *thisEnv = *env;
            printf("%s\n", thisEnv);
        }

    }

}

// To set an enviroment variable
void set(int argc, char *args[], int background){

    // To check whether input is like this "set PWD = /usr/lib"
    if (strcmp(args[2], "=") != 0) {
        printf("Wrong assignment for set()!\n");
        return;
    }

    // To check whether input is like this "set PWD = /usr/lib", no more arguments
    if(args[4] != NULL){

        printf("Wrong usage! The command must contains only 4 distinct elements.\n");

    }

    // To check whether input is like this "set PWD = /usr/lib", no numeric input
    if(numeric(args[1])){
        printf("Numeric input in not allowed!\n");
        return;
    }

    // To set new value for enviromental variable
    setenv(args[1], args[3], 1);

}

// To exit program if there is no child process
void exitProgram(int argc, char **argv, char **envp){

    // To hold child process ID
    pid_t child_pid = waitpid(-1, NULL, WNOHANG);

    // If there is any child process, wait for it until it is terminated
    if(child_pid == 0){

        printf("Before exit, you must close background processes!\n");

        return;

        // If there is no child process, finish the program successfully
    } else {

        printf("See you later |(o_o)|\n");
        exit(EXIT_SUCCESS);

    }

}

// The setup function below will not return any value, but it will just: read
// in the next command line; separate it into distinct arguments (using blanks as
// delimiters), and set the args array entries to point to the beginning of what
// will become null-terminated, C-style strings. Retruns the number of arguments.
int setup( char inputBuffer[], char *args[], int *background, int justParse )
{
    int         length = -1;    // # of characters in the command line.
    int         i;              // Loop index for accessing inputBuffer array.
    int         start;          // Index where beginning of next command parameter is.
    int         ct;             // Index of where to place the next parameter into args[].
    char        pressedKey;     // Will hold the value of the pressed key.
    int         char1, char2, char3;
    ct = 0;

    if( !justParse ) // Read inputBuffer from the keyboard.
    {
        length = read( STDIN_FILENO, inputBuffer, MAX_LINE ) + 1;

        /*
        strcpy( inputBuffer, "\0" ); // Empty the inputBuffer.

        length = read( STDIN_FILENO, inputBuffer, MAX_LINE ) + 1;
        inputBuffer[ length - 2 ] = '\n'; // Make sure the last character is NULL.
        inputBuffer[ length - 1 ] = '\0'; // Make sure the last character is NULL.

        InsertIntoLinkedList( &cmdHistory, inputBuffer );
        */
    }
    else // inputBuffer is already filled and ready to be parsed, use it directly.
    {
        //length = strlen( inputBuffer ) + 1;
        length = strlen( inputBuffer ) + 2;
        inputBuffer[ length - 2 ] = '\n'; // Setup expects the strings to end with "\n".
        inputBuffer[ length - 1 ] = '\0'; // Null-terminate the string.
    }

    // 0 is the system predefined file descriptor for stdin (standard input),
    // which is the user's screen in this case. inputBuffer by itself is the
    // same as &inputBuffer[0], i.e. the starting address of where to store
    // the command that is read, and length holds the number of characters
    // read in. inputBuffer is not a null terminated C-string.

    start = -1;
    if( length == 0 )
    {
        exit( 0 ); // ^d was entered, end of user command stream
    }

    for( i = 0; i < length; i++ )
    {	// Examine every character in the inputBuffer.
        switch( inputBuffer[ i ] )
        {
            case ' ' :
            case '\t': // Argument separators.
                if( start != -1 )
                {
                    args[ct] = &inputBuffer[ start ]; // Set up pointer.
                    ct++;
                }

                inputBuffer[ i ] = '\0'; // Add a null char; make a C string.
                start = -1;

                break;
            case '\n': // Should be the final char examined.
                if( start != -1 )
                {
                    args[ ct ] = &inputBuffer[ start ];
                    ct++;
                }

                inputBuffer[ i ] = '\0';

                args[ ct ] = NULL; // No more arguments to this command.

                break;
            default: // Some other character.
                if( start == -1 )
                {
                    start = i;
                }

                if( inputBuffer[ i ] == '&' )
                {
                    *background  = 1;
                    inputBuffer[ i - 1 ] = '\0';
                }
        } // end of switch
    } // end of for

    args[ ct ] = NULL; // just in case the input line was > 80

    if(*background == 1){
        args[ct-1] = NULL;
    }

    return ct; // Return the number of arguments;
}

void DeleteStringFromTerminal( char* string )
{
    int length = strlen( string );
    int i;
    for( i = 0; i < length; i++ )
    {
        printf( "\b" );
    }
}

int main(int argc, char **argv, char **envp){

    int i, j;
    char inputBuffer[MAX_LINE]; // buffer to hold command entered
    int background;	// equals 1 if a command is followed by '&'
    char *args[MAX_LINE];	// command line arguments
    int result; // Will hold the result of CreateChildProcess().
    LinkedList bookmarks = { NULL, NULL }; // LL to hold bookmarked commands.
    Node*           cmdHistoryPtr   = NULL;
    int             inputAcquired   = 0;
    int             historyMode     = 0;
    int             pressedKey      = ' ';
    int             firstPress;
    int             inputLength;
    int             exit            = 0;
    struct termios  canonicalMode;
    struct termios  nonCanonicalMode;

    //setTerminalModes( &canonicalMode, &nonCanonicalMode );

    while (1){

        background = 0;
        printf("myshell> \n");
        inputAcquired = 0;
        firstPress = 1;

        /*while( !inputAcquired )
        {
            // Set the terminal to non-canonical mode.
            tcsetattr( STDIN_FILENO, TCSANOW, &nonCanonicalMode );

            pressedKey = getchar();
            if( pressedKey == 27 )
            {
                getchar(); // Second key is of no importance here. We need the third one.
                pressedKey = getchar();

                if( firstPress )
                {
                    if( pressedKey == 65 )
                        cmdHistoryPtr = cmdHistory.tail;
                    else if( pressedKey == 66 )
                        cmdHistoryPtr = cmdHistory.header;

                    if( cmdHistoryPtr != NULL )
                        printf( "%s\n", cmdHistoryPtr->data );

                    firstPress = 0;
                }
                // 65 means Up-arrow key was pressed.
                if( !firstPress && pressedKey == 65 && cmdHistoryPtr != NULL && cmdHistoryPtr->prevPtr != NULL )
                {
                    //DeleteStringFromTerminal( cmdHistoryPtr->data );
                    cmdHistoryPtr = cmdHistoryPtr->prevPtr;

                    printf( "%s\n", cmdHistoryPtr->data );
                }
                // 66 means Down-arrow key was pressed.
                else if( !firstPress && pressedKey == 66 && cmdHistoryPtr != NULL && cmdHistoryPtr->nextPtr != NULL )
                {
                    //DeleteStringFromTerminal( cmdHistoryPtr->data );
                    cmdHistoryPtr = cmdHistoryPtr->nextPtr;

                    printf( "%s\n", cmdHistoryPtr->data );
                }
            }
            else if( !firstPress && pressedKey == 10 && cmdHistoryPtr != NULL )
            {
                // Last parameter of setup() means 0: Read input from user, 1: Just parse.
                argc = setup( cmdHistoryPtr->data, args, &background, 1 );
                //historyMode = 0; // Exit history mode and carry on as usual.

                inputAcquired = 1;
            }
            else
            {
                // Set the terminal mode back to canonical mode for usual input reading.
                tcsetattr( STDIN_FILENO, TCSANOW, &canonicalMode );

                // Count how many arguments entered
                int argc = setup( inputBuffer, args, &background, 0);

                inputAcquired = 1;
            }
        }
*/
        int argc = setup( inputBuffer, args, &background, 0);

        switch(command(args[0])){

            case BOOKMARK:

                //pathing(args);

                bookmark( args, &bookmarks );

                break;

            case CODESEARCH:

                codesearch(".", 0, args);

                break;

            case PRINT:

                print(argc, args, envp);

                break;

            case SET:

                set(argc, args, envp);

                break;

            case EXIT:

                exitProgram(argc, args, envp);

                break;

            case COMMAND:

                result = createChildProcess( args, background );
                if( result != 0 ) // If there was an error, terminate the program.
                    return result;

                break;

            default:

                printf("Case - Default\n");

        }

    }   // End of While Loop

}