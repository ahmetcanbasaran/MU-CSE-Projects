/*
 *  OPERATING SYSTEM PROJECT #3
 *
 *      PROGRAMMER: OĞUZHAN BÖLÜKBAŞ
 *      STUDENT ID: 150114022
 *
 */

/*
 *  This program opens obtained directory,
 *  reads only ".txt" files in it line by line and
 *  put them into dynamically allocated array
 *  with help of multi-threads.
 *
 */

/* To compile the program, use the following code:
 *
 *  gcc program_name.c -o program_name.out -lpthreap
 *
 * (pthread: POSIX Thread Library)
 *
 */


// To include required libraries
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <dirent.h>
#include <memory.h>
#include <semaphore.h>

// Prototype of functions
void readDirectory(char *files[], char **args);
void* readFile(void *filename);

// To hold thread arguments
typedef struct t_s{
    pthread_t tid;      // To hold thread id
    sem_t* s_q;         // Semaphore queue
    int* index;         // Dynamically allocated array index
    long* size;          // Size of array
    char** d_array;     // Dynamically allocated array
    char* filename;     // Name of file which will be read
} t_s;

// To open directory in order to reach contained files
void readDirectory(char *files[], char **args){

    // To use obtained directory
    char *directory = args[2];

    DIR *dir;           // Pointer for directory
    struct dirent *d;
    char *file_type;    // To specify only ".txt" files
    int fileNum = 0;    // To store how many ".txt" files exist

    // To open directory
    if (!(dir = opendir(directory)))
        return;

    // To run search in directory until it ends
    while ((d = readdir(dir)) != NULL) {

        // To pass "." and ".." which means current and parrent directory in Linux
        if (strcmp(d->d_name, ".") == 0 || strcmp(d->d_name, "..") == 0) {
            continue;
        }

        // To divide file names from '.' in order to get file types
        file_type = strrchr(d->d_name, '.');

        if (file_type != NULL){

            // To compare cutted string to check whether it is ".txt"
            if(strcmp(file_type, ".txt") == 0){

                files[fileNum++] = d->d_name;

            }
        }

    }

}

// To read files. The function is specified for thread usage
void* readFile(void *param){

    // Parameters of thread
    t_s* p = (t_s*) param;

    // To get thread id's
    p->tid = pthread_self();

    // To print which thread is attached which file
    printf("MAIN THREAD: Assigned \"%s\" to worker thread %ld.\n", p->filename, p->tid);

    // To keep file names
    char filename[100];

    // To copy file names from char* to char[]
    strcpy(filename, p->filename);

    // To open file in read-only mode
    FILE *fp = fopen(filename, "r");

    char *line;     // To keep lines in files
    int i = 0, j = 0, same = 0;     // i and j for loops and same for checking exist word in dynamic array

    // To store words which obtained from current reading line
    char word[100];

    // To read every line in file in order to find searching keyword
    if (fp != NULL) {

        for(;;){

            char buf[1000];

            // To obtain line
            line = fgets(buf, sizeof buf, fp);

            // To finish reading file if lines are finished
            if (line == NULL){
                p->filename = NULL;     // To reset filename in order to reuse this thread
                break;
            }

            // To check every char in line array
            for (i = 0; ;i++){

                // To reset same word checker
                same = 0;

                // To finish storing char in word
                if(line[i] == ' ' || line[i] == '\n' || line[i] == '\0'){

                    word[j] = '\0'; // To assign word's last element NULL

                    j = 0;

                    // To allow give storing word permission to one thread on each time
                    sem_wait(p->s_q); //threads wait in this semaphore queue

                        // To check whether this word is stored before
                        for (int k = 0; k < *(p->index); k++) {

                            if(strcmp(p->d_array[k], word) == 0)
                                same = 1;

                        }

                        // If the word is not stored, then run below part
                        if(same == 0){

                            // To allocate memory space to store new word in dynamic array
                            p->d_array[*(p->index)] = (char *)malloc(sizeof(char *) * *(p->size));

                            // To copy string in allocated memory space
                            strcpy(p->d_array[*(p->index)], word);

                            // To print which thread have added which word
                            printf("THREAD %ld: Added \"%s\" at index %d\n", pthread_self(), p->d_array[*(p->index)], *(p->index));

                            // To check whether memory space is filled fully
                            if(*(p->index)+1 == *(p->size)){

                                // To allocate memory space as it's previous size
                                *(p->size) = *(p->size) * 2;

                                // Realloc current dynamic array
                                *(p->d_array) = realloc(*(p->d_array), (sizeof(char *)) * (*(p->size)));

                                // To print which thread reallocate the array
                                printf("THREAD %ld: Re-allocated array of %d pointers.\n", pthread_self(), *(p->size));

                            }

                            // To increase index of dynamic array
                            (*(p->index))++;

                        }

                    // To unlock permission which is to store word
                    sem_post(p->s_q);

                    // To break for loop when the line reaches end of line or file
                    if(line[i] == '\n' || line[i] == '\0')
                        break;

                // To store new char into word array in order to make a word
                } else {
                    word[j] = line[i];
                    j++;
                }

            }   // End of inner for loop

        }   // End of outer for loop

    }   // End of file pointer

    return NULL;

}

// Our main functions. It acts like an orchestra chef
int main(int argc, char **args){

    // To print error when usage of the program is wrong
    if((argc != 5) || strstr(args[1], "-d") == NULL || strstr(args[3], "-n") == NULL){
        perror("ERROR: Invalid arguments");
        perror("USAGE: ./a.out -d <directoryName> -n <#ofThreads>");
    }

    long NUM_THREADS = atoi(args[4]);   // To get thread numbers
    long t, f, i;                       // For loops
    int rc, success;                    //
    int array_index = 0, file_num = 0;
    char *files[1000];
    char **d_array;         // Dynamically allocated array
    long p_size = 8;        // Pointer array size

    // To allocate memory space for our main array
    d_array = malloc(sizeof(char *) * p_size);

    pthread_t thread[NUM_THREADS];      // Thread array
    t_s thread_arg[NUM_THREADS];        // Thread arguments array

    sem_t semaphore_queue;              // To define semaphore
    sem_init(&semaphore_queue, 0, 1);   // To give permission to one thread only in each time

    // Initialize threads' arguments
    for (t = 0; t < NUM_THREADS; t++) {
        thread_arg[t].s_q = &semaphore_queue;
        thread_arg[t].index = &array_index;
        thread_arg[t].d_array = d_array;
        thread_arg[t].size = &p_size;
        thread_arg[t].filename = NULL;
    }

    // To read directory in order to reach files
    readDirectory(files, args);

    // To count how many file is founded
    for (t = 0; files[t] != NULL; t++) {
        file_num++;
    }

    // To store file names
    char file_array[1000][100];

    // To copy char* which keeps file names to file name array
    for (int t = 0; t < file_num; t++){
        strncpy(file_array[t], files[t], sizeof(file_array) -1 );
        file_array[t][sizeof(file_array)] = '\0';
    }

    // Turn until each file is processed
    for(t = 0; t < file_num; t++){

        // To reset finding thread success at each time
        success = 0;

        // To turn until one thread holds that unused file in order to process it
        while(1){

            // To check every thread to find which one finishes execution
            for (f = 0; f < NUM_THREADS; f++) {

                // To give file name into free thread
                if (thread_arg[f].filename == NULL) {

                    //To allocate memory space in order to keep file name
                    thread_arg[f].filename = (char *) malloc(sizeof(file_array[t]));

                    // To copy file name
                    strcpy(thread_arg[f].filename, file_array[t]);

                    // To run thread with its argument structure
                    rc = pthread_create(&thread[f], NULL, &readFile, &thread_arg[f]);

                    // To print error if thread generating is failed
                    if (rc) {
                        printf("ERROR; return code from pthread_create() is %d\n", rc);
                        exit(-1);
                    }

                    // To specify that this file name is obtained by currently free thread
                    success = 1;

                    // To exit loop
                    break;

                }   // End of if

            }   // End of for loop

            // To exit from while loop
            if (success == 1)
                break;

        }   // End of while loop

    }

    // To wait all threads by joining them
    for (i = 0; i < NUM_THREADS; i++) {
        pthread_join(thread[i], NULL);
    }

    // To print the result
    printf("MAIN THREAD: All done (successfully read %d words with %d threads from %d files).\n",
           *(thread_arg[0].index), (int) NUM_THREADS, file_num);

    // To exit the program successfully
    exit(EXIT_SUCCESS);

}