#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Converts a hexadecimal string to integer.
int hex2int(char* hex){

  int result = 0;

  while (*hex != '\0'){
    if (('0' <= *hex) && (*hex <= '9'))
      result = result * 16 + *hex - '0';
    else if(('a' <= *hex) && (*hex <= 'f'))
      result = result * 16 + *hex - 'a' + 10;
    else if(('A' <= *hex) && (*hex <= 'F'))
      result = result * 16 + *hex - 'A' + 10;
    hex++;
  }
  return result;
}

void LDI(int* program_ptr, int* counter){

  char* op1 = strtok(NULL, "\n\t\r "); 
  char* op2 = strtok(NULL, "\n\t\r "); 
  
  program_ptr[*counter] = 0x4000 + hex2int(op1); // Generate the first 16-bit of the ldi instruction.
  *counter = *counter + 1; // Skip to the next memory location.

  if((op2[0] == '0') && (op2[1] == 'x')) // If the 2nd operand is twos complement hexadecimal
    program_ptr[*counter] = hex2int(op2 + 2) & 0xFFFF; // Convert it to integer and form the second 16-bit.

  else if(((op2[0]) == '-') || ((op2[0] >= '0') && (op2[0] <= '9'))) // If the 2nd operand is decimal
    program_ptr[*counter] = atoi(op2) & 0xFFFF; // Convert it to integer and form the second 16-bit.

  else // If the second operand is not decimal or hexadecimal, it is a laber or a variable.    
    printf("Unrecognizable LDI offset!\n");  // In this case, the 2nd 16-bits of the ldi instruction cannot be generated.
  
  *counter = *counter + 1; // Skip to the next memory location.

}

void ALUImm(int* program_ptr, int* counter, const int aluOpCodeInHex){

  char* op1 = strtok(NULL, "\n\t\r "); 
  char* op2 = strtok(NULL, "\n\t\r ");
  char* op3 = strtok(NULL, "\n\t\r "); 
  
  char ch = (((op2[0] - '0') << 6) | (op1[0] - '0'));  //op1=tr, op2=src1, op3=src2
  program_ptr[*counter] = 0xC000 + aluOpCodeInHex + ((ch) & 0x00FF);
  *counter = *counter + 1; // Skip to the next memory location.

  if((op3[0] == '0') && (op3[1] == 'x')) // If the 2nd operand is twos complement hexadecimal
    program_ptr[*counter] = hex2int(op3 + 2) & 0xFFFF; // Convert it to integer and form the second 16-bit.

  else if(((op3[0]) == '-') || ((op3[0] >= '0') && (op3[0] <= '9'))) // If the 2nd operand is decimal
    program_ptr[*counter] = atoi(op3) & 0xFFFF; // Convert it to integer and form the second 16-bit.

  else // If the second operand is not decimal or hexadecimal, it is a laber or a variable.    
    printf("Unrecognizable LDI offset!\n");  // In this case, the 2nd 16-bits of the ldi instruction cannot be generated.
  
  *counter = *counter + 1; // Skip to the next memory location.

}

void _1_Reg_Inst(int* program_ptr, int* counter, const int aluOpCodeInHex){
  char* op1 = strtok(NULL, "\n\t\r ");
  char ch = (((op1[0] - '0') << 3) | (op1[0] - '0'));  //op1=tr, op2=src1, op3=src2
  program_ptr[*counter] = 0x8000 + aluOpCodeInHex + ((ch) & 0x00FF);
  *counter = *counter + 1; // Skip to the next memory location.
}

void _2_Reg_Inst(int* program_ptr, int* counter, const int aluOpCodeInHex){
  char* op1 = strtok(NULL, "\n\t\r ");
  char* op2 = strtok(NULL, "\n\t\r ");
  char ch = (((op2[0] - '0') << 6) | (op1[0] - '0'));  //op1=tr, op2=src1, op3=src2
  program_ptr[*counter] = 0x8000 + aluOpCodeInHex + ((ch) & 0x00FF);
  *counter = *counter + 1; // Skip to the next memory location.
}

void _3_Reg_Inst(int* program_ptr, int* counter, const int aluOpCodeInHex){
  char* op1 = strtok(NULL, "\n\t\r ");
  char* op2 = strtok(NULL, "\n\t\r ");
  char* op3 = strtok(NULL, "\n\t\r ");

  int chch = ((op3[0] - '0') << 3) | ((op2[0] - '0') << 6) | ((op1[0] - '0'));  //op1=tr, op2=src1, op3=src2
  program_ptr[*counter] = 0x8000 + aluOpCodeInHex + ((chch) & 0x00FF);
  *counter = *counter + 1; // Skip to the next memory location.
}

int main (){

  FILE* fp;
  char line[100];
  char* token = NULL;
  int lineNo;
  int dataArea = 0;

  int program[1000];
  int	counter = 0;  // Holds the address of the machine code instruction.

  fp = fopen("instructions.txt", "r");

  while(fgets(line, sizeof line, fp) != NULL){
    
    token = strtok(line, "\n\t\r "); // Get the instruction mnemonic or label.

    if(strcmp(token, "LDI") == 0)
      LDI(program, &counter);
    
    else if(strcmp(token, "ADD") == 0)
      _3_Reg_Inst(program, &counter, 0x000);
    else if(strcmp(token, "SUB") == 0)
      _3_Reg_Inst(program, &counter, 0x100);
    else if(strcmp(token, "AND") == 0)
      _3_Reg_Inst(program, &counter, 0x200);
    else if(strcmp(token, "OR") == 0)
      _3_Reg_Inst(program, &counter, 0x300);
    else if(strcmp(token, "XOR") == 0)
      _3_Reg_Inst(program, &counter, 0x400);

    else if(strcmp(token, "NOT") == 0)
      _2_Reg_Inst(program, &counter, 0x500);
    else if(strcmp(token, "MOV") == 0)
      _2_Reg_Inst(program, &counter, 0x600);

    else if(strcmp(token, "INC") == 0)
      _1_Reg_Inst(program, &counter, 0x700);
    else if(strcmp(token, "DEC") == 0)
      _1_Reg_Inst(program, &counter, 0x800);

    else if(strcmp(token, "ADDI") == 0)
      ALUImm(program, &counter, 0x000);
    else if(strcmp(token, "SUBI") == 0)
      ALUImm(program, &counter, 0x100);
    else if(strcmp(token, "ANDI") == 0)
      ALUImm(program, &counter, 0x200);
    else if(strcmp(token, "ORI") == 0)
      ALUImm(program, &counter, 0x300);
    else if(strcmp(token, "XORI") == 0)
      ALUImm(program, &counter, 0x400);    

    else // ------ WHAT IS ENCOUNTERED IS NOT A VALID INSTRUCTION OPCODE
      printf("Invalid opcode!\n");

  }

  fclose(fp);

  // To write into a RAM file
  fp = fopen("RAM", "w");

  fprintf(fp, "v2.0 raw\n"); // Logisim needs this header.

  for (lineNo = 0; lineNo < counter + dataArea; lineNo++)
    fprintf(fp, "%04x\n", program[lineNo]);

  return 0;

}
