`include "ControlUnit.v"
`include "ROM.v"
`include "RAM.v"
`include "PC.v"
`include "ALU.v"
`include "RFID.v"
`include "RegisterFile.v"
`include "Mux.v"
`include "Comperator.v"
`include "BranchOperator.v"
`include "Adder.v"

module CPU();

    wire clk;
    wire CCE;
    wire PRS;
    wire [19:0] dataFromCounter;
    wire [19:0] jump_addr, immValue; // Done
    wire [11:0] addr; // Done
    wire [3:0] reg1, reg2, reg3; // Done
    wire [1:0] aluOperation; // Done
    wire [2:0] nzp, fsmControlType; // Done
    wire immediateControl, isBranch;
    wire pcReadSignal, dataMemoryReadSignal, registerWriteSignal,
    aluControlSignal, isStore, clockCounterEnabled, writeMemorySignal;

    wire [3:0] reg1_in, reg2_in, reg3_in, reg1_out, reg2_out, drFromRFID;
    wire [2:0] cmpResult;
    wire [19:0] ramDataOutput, aluOutput, inputDataFromRFID, rd1Data, rd2Data,
        aluOutData, aluInputData, branchOperatorResult, adderCounterResult, pcOut, instruction;

    // Modules: CPU Part

    pc pcModule(clk, PRS, dataFromCounter, CCE, pcOut);
   
    ROM romModule(pcOut, instruction);
    
    ControlUnit controlUnitModule(instruction, clk,
        nzp, reg1, reg2, reg3, aluOperation, immediateControl,
        immValue, addr, fsmControlType, isBranch, jump_addr,
        pcReadSignal, dataMemoryReadSignal, registerWriteSignal, aluControlSignal,
        isStore, clockCounterEnabled, writeMemorySignal
    );

    RAM ramModeule(clk, addr, rd1Data, writeMemorySignal, dataMemoryReadSignal, ramDataOutput);
   
    RFID rfidModule(ramDataOutput, aluOutput, aluControlSignal, inputDataFromRFID, reg1_out,
		drFromRFID, isStore, reg2_out, reg3_in, isBranch, reg1_in, reg2_in);

    registerfile registerFileModule(clk, registerWriteSignal, reg1_out, reg2_out, 
        drFromRFID, inputDataFromRFID, rd1Data, rd2Data);

    mux2to1 mux2to1Module(aluInputData, rd1Data, immValue, immediateControl);

    ALU aluModule(aluOutData, rd2Data, aluInputData, aluOperation);

    Comperator comperatorModule(rd1Data, rd2Data, cmpResult);

    BranchOperator branchOperatorModule(pcOut, immValue, nzp, cmpResult, branchOperatorResult);

    Full_Adder20 adderModule(adderCounterResult, pcOut, jump_addr);

    mux2to1 mux2to1Module1(dataFromCounter, adderCounterResult, branchOperatorResult, isBranch);


endmodule