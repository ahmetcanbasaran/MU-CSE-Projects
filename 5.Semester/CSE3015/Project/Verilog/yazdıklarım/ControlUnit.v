`include "FiniteStateMachine.v"

module ControlUnit (clk, id0, id1, id2);

    input clk, id0, id1, id2;

    reg pcReadSignalOut, memoryReadOut, 
		registerWriteSignalOut, aluControlSignalOut, 
		isStoreOut, clockCounterEnabledOut, 
		writeMemorySignalOut;

    reg pcReadSignal, dataMemoryReadSignal, 
		registerWriteSignal, aluControlSignal, 
		isStore, clockCounterEnabled,
        writeMemorySignal;
		
	wire pcReadSignalOut_wire, memoryReadOut_wire, 
		registerWriteSignalOut_wire, aluControlSignalOut_wire, 
		isStoreOut_wire, clockCounterEnabledOut_wire, 
		writeMemorySignalOut_wire;

    wire pcReadSignal_wire, dataMemoryReadSignal_wire, 
		registerWriteSignal_wire, aluControlSignal_wire, 
		isStore_wire, clockCounterEnabled_wire,
        writeMemorySignal_wire;

    initial 
	begin
		pcReadSignal = 0;
        pcReadSignalOut = 0;
		dataMemoryReadSignal = 0;
		memoryReadOut = 0;
		registerWriteSignal = 0;
		registerWriteSignalOut = 0;
        aluControlSignal = 0;
		aluControlSignalOut = 0; 
		isStore = 0;
		isStoreOut = 0; 
		clockCounterEnabled = 0;
		clockCounterEnabledOut = 0;
		writeMemorySignal = 0;
		writeMemorySignalOut = 0;
    end

    always @(posedge clk) 
	begin
        pcReadSignal <= pcReadSignalOut;
        dataMemoryReadSignal <= memoryReadOut;
        registerWriteSignal <= registerWriteSignalOut;
        aluControlSignal <= aluControlSignalOut;
        isStore <= isStoreOut;
        clockCounterEnabled <= clockCounterEnabledOut;
        writeMemorySignal <= writeMemorySignalOut;
    end
	
	assign pcReadSignal_wire = pcReadSignal;
	assign dataMemoryReadSignal_wire = dataMemoryReadSignal;
	assign registerWriteSignal_wire = registerWriteSignal;
	assign aluControlSignal_wire = aluControlSignal;
	assign clockCounterEnabled_wire = clockCounterEnabled,
	assign writeMemorySignal_wire = writeMemorySignal;
	
	FiniteStateMachine fsm(
        clk,
        pcReadSignal_wire,
        dataMemoryReadSignal_wire,
        registerWriteSignal_wire,
        aluControlSignal_wire,
        isStore_wire,
        clockCounterEnabled_wire,
        writeMemorySignal_wire,
        id0,
        id1,
        id2,
		
		pcReadSignalOut_wire,
        memoryReadOut_wire,
        registerWriteSignalOut_wire,
        aluControlSignalOut_wire,
        isStoreOut_wire,
        clockCounterEnabledOut_wire,
        writeMemorySignalOut_wire);
		
	assign pcReadSignalOut = pcReadSignalOut_wire;
	assign memoryReadOut = memoryReadOut_wire;
	assign registerWriteSignalOut = registerWriteSignalOut_wire;
	assign aluControlSignalOut = aluControlSignalOut_wire;
	assign isStoreOut = isStoreOut_wire;
	assign clockCounterEnabledOut = clockCounterEnabledOut_wire;
	assign writeMemorySignalOut = writeMemorySignalOut_wire;
	
endmodule