
`include "Mux.v"
`include "Adder.v"

module ALU ( out, in0, in1, select );

    output wire [19:0] out;
    input wire [19:0] in0, in1;
    input wire [1:0] select;

    wire [19:0] andResult, orResult, xorResult, addResult;
    assign andResult = in0 & in1;
    assign orResult = in0 | in1;
    assign xorResult = in0 ^ in1;
    Full_Adder20 adder ( addResult, in0, in1 );

    mux4to1 m1(out, andResult, orResult, xorResult, addResult, select );

endmodule


