
`include "PriorityEncoder.v"

module ControlUnit (
    instruction, clk,

    nzp, reg1, reg2, reg3, aluOperation, immediateControl,
    immValue, addr, fsmControlType, isBranch, jump_addr,
    pcReadSignal, dataMemoryReadSignal, registerWriteSignal, aluControlSignal,
    isStore, clockCounterEnabled, writeMemorySignal
    );

    input [19:0] instruction;
    input clk;

    output [19:0] jump_addr, immValue; // Done
    output [11:0] addr; // Done
    output [3:0] reg1, reg2, reg3; // Done
    output [1:0] aluOperation; // Done
    output [2:0] nzp, fsmControlType; // Done
    output immediateControl, isBranch;
    output reg pcReadSignal, dataMemoryReadSignal, registerWriteSignal,
    aluControlSignal, isStore, clockCounterEnabled, writeMemorySignal;

    wire [3:0] opcode;
    assign opcode = instruction[19:16];
    wire add, addi, bgt, jump, beq, xorr, bge, st, blt, xori, andd, andi, ble, ld, orr, ori;

    assign add = (opcode==4'b0000) ? 1 : 0;
    assign addi = (opcode==4'b0001) ? 1 : 0;
    assign bgt = (opcode==4'b0010) ? 1 : 0;
    assign jump = (opcode==4'b0011) ? 1 : 0;
    assign beq = (opcode==4'b0100) ? 1 : 0;
    assign xorr = (opcode==4'b0101) ? 1 : 0;
    assign bge = (opcode==4'b0110) ? 1 : 0;
    assign st = (opcode==4'b0111) ? 1 : 0;
    assign blt = (opcode==4'b1000) ? 1 : 0;
    assign xori = (opcode==4'b1001) ? 1 : 0;
    assign andd = (opcode==4'b1010) ? 1 : 0;
    assign andi = (opcode==4'b1011) ? 1 : 0;
    assign ble = (opcode==4'b1100) ? 1 : 0;
    assign ld = (opcode==4'b1101) ? 1 : 0;
    assign orr = (opcode==4'b1110) ? 1 : 0;
    assign ori = (opcode==4'b1111) ? 1 : 0;


    //Jump Address
    assign jump_addr[15:0] = instruction[15:0];
    wire tmp1;
    assign tmp1 = instruction[15];
    assign jump_addr[19:16] = {tmp1, tmp1, tmp1, tmp1};

    //immadiete Value
    assign immValue[7:0] = instruction[7:0];
    wire tmp2;
    assign tmp2 = instruction[7];
    assign immValue[19:8] = {tmp2, tmp2, tmp2, tmp2, tmp2, tmp2, tmp2, tmp2, tmp2, tmp2, tmp2, tmp2};

    //Address
    assign addr = instruction[11:0];
    
    //Registers
    assign reg1 = instruction[15:12];
    assign reg2 = instruction[11:8];
    assign reg3 = instruction[7:4];

    // Alu Operation
    assign aluOperation = 
		(andd == 1 | andi == 1) ? 2'b00 : 
		(orr == 1 | ori == 1) ? 2'b01 : 
		(xorr == 1 | xori == 1) ? 2'b10 : 
		(add == 1 | addi == 1) ? 2'b11 : 2'b00;

    // NZP
    assign nzp = instruction[19:17];

    // Immedieate Control
    assign immediateControl = andi | ori | xori | addi;
    // Is_Branch
    assign isBranch = beq | bge | ble | bge | bgt;
    
    // FSM Control Type

    // ALU_CONTROL
    // JUMP_CONTROL
    // LD_CONTROL
    // BRANCH_CONTROL
    // ST_CONTROL

    wire [4:0] fsmControlInput;

    assign fsmControlInput[0] = add | addi | orr | ori | xorr | xori | add | addi;
    assign fsmControlInput[1] = jump;
    assign fsmControlInput[2] = ld;
    assign fsmControlInput[3] = beq | bgt | bge | ble | blt;
    assign fsmControlInput[4] = st; 

    PriorityEncoder_5_3 pe(fsmControlType,fsmControlInput);

    //Finite State Machine

    reg [6:0] state, nextState;

    initial begin
      state = 7'b0000000;
      nextState = 7'b0000000;
    end

    always @(posedge clk) begin
      state <= nextState;
      if (state == 7'b0000000 && fsmControlType == 3'b010) begin
        nextState = 7'b0110000;
      end else if (state == 7'b1000000 && fsmControlType == 3'b010) begin
        nextState = 7'b0110000;
      end else if (state == 7'b0000010 && fsmControlType == 3'b010) begin
        nextState = 7'b0110000;
      end else if (state == 7'b0110000 && fsmControlType == 3'b010) begin
        nextState = 7'b0000010;
      end else if (state == 7'b0000000 && fsmControlType == 3'b100) begin
        nextState = 7'b0000101;
      end else if (state == 7'b0000010 && fsmControlType == 3'b100) begin
        nextState = 7'b0000101;
      end else if (state == 7'b1000000 && fsmControlType == 3'b100) begin
        nextState = 7'b0000101;
      end else if (state == 7'b0000101 && fsmControlType == 3'b100) begin
        nextState = 7'b0000010;
      end else if (state == 7'b1000000 && fsmControlType == 3'b001) begin
        nextState = 7'b1000000;
      end else if (state == 7'b0000010 && fsmControlType == 3'b001) begin
        nextState = 7'b1000000;
      end else if (state == 7'b0000000 && fsmControlType == 3'b001) begin
        nextState = 7'b1000000;
      end else if (state == 7'b1000000 && fsmControlType == 3'b000) begin
        nextState = 7'b0011000;
      end else if (state == 7'b1000000 && fsmControlType == 3'b000) begin
        nextState = 7'b0011000;
      end else if (state == 7'b0000010 && fsmControlType == 3'b000) begin
        nextState = 7'b0011000;
      end else if (state == 7'b0011000 && fsmControlType == 3'b000) begin
        nextState = 7'b0000010;
      end else if (state == 7'b0000000 && fsmControlType == 3'b011) begin
        nextState = 7'b1000000;
      end else if (state == 7'b1000000 && fsmControlType == 3'b011) begin
        nextState = 7'b1000000;
      end else if (state == 7'b0000010 && fsmControlType == 3'b011) begin
        nextState = 7'b1000000;
      end

      writeMemorySignal = nextState[0];
      clockCounterEnabled = nextState[1];
      isStore = nextState[2];
      aluControlSignal = nextState[3];
      registerWriteSignal = nextState[4];
      dataMemoryReadSignal = nextState[5];
      pcReadSignal = nextState[6];

    end

    






    
    //

     
endmodule