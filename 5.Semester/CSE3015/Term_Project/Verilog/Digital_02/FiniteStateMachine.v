module FiniteStateMachine (
    clk,
    pcReadSignal,
    dataMemoryReadSignal,
    registerWriteSignal,
    aluControlSignal,
    isStore,
    clockCounterEnabled,
    writeMemorySignal,
    id0,
    id1,
    id2,

    pcReadSignalOut,
    memoryReadOut,
    registerWriteSignalOut,
    aluControlSignalOut,
    isStoreOut,
    clockCounterEnabledOut,
    writeMemorySignalOut
);

input wire
    clk,
    pcReadSignal,  
    dataMemoryReadSignal,
    registerWriteSignal,
    aluControlSignal,
    isStore,
    clockCounterEnabled,
    writeMemorySignal,
    id0,
    id1,
    id2;

output reg pcReadSignalOut,
    memoryReadOut,
    registerWriteSignalOut,
    aluControlSignalOut,
    isStoreOut,
    clockCounterEnabledOut,
    writeMemorySignalOut;

reg r1, r2;
reg tmp1, tmp2;

always @(posedge clk) begin
    r1 <= (~pcReadSignal & ~clockCounterEnabled) |
    (pcReadSignal & ~clockCounterEnabled) |
    (~pcReadSignal & clockCounterEnabled);

    r2 <= ~(dataMemoryReadSignal | registerWriteSignal | aluControlSignal | isStore | writeMemorySignal);

    pcReadSignalOut <= r2 & ~id0 & id1 & id2 & r1;
    memoryReadOut <= r2 & ~id0 & id1 & ~id2 & r1;
    registerWriteSignalOut <= r2 & ~id0 & ~id2 & r1;
    aluControlSignalOut <= r2 & ~id0 & ~id1 & ~id2 & r1;
    isStoreOut <= r2 & id0 & ~id1 & ~id2 & r1;


    tmp1 <= ~pcReadSignal & 
        registerWriteSignal & 
        ~isStore & 
        ~clockCounterEnabled & 
        ~writeMemorySignal &
        ~id0 & 
        ~id2 &
        (dataMemoryReadSignal & ~aluControlSignal & id1) | 
        (~dataMemoryReadSignal & aluControlSignal & ~id1);

        tmp2 <= ~pcReadSignal &
        ~dataMemoryReadSignal &
        ~registerWriteSignal &
        ~aluControlSignal &
        isStore &
        ~clockCounterEnabled &
        writeMemorySignal &
        id0 &
        ~id1 &
        ~id2;




    clockCounterEnabledOut <= tmp1 | tmp2;

    writeMemorySignalOut <= isStoreOut; 

end




endmodule
