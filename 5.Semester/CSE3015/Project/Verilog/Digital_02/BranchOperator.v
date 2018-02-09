`include "Mux.v"
`include "Adder.v"

module BranchOperator(
    currentPC,
    addr,
    nzp,
    cmpResult,
    newPC
);

input [19:0] currentPC, addr;
input [2:0] nzp, cmpResult;
output [19:0] newPC;

wire [2:0] andResult;
wire [19:0] temp1, temp2;

assign andResult = nzp & cmpResult;

    Full_Adder20 adderModule(temp1, 20'b00000000000000000001, currentPC);
    Full_Adder20 adderModule2(temp2, currentPC, addr);

    mux8to1 muxtto1Module(newPC, temp1, temp2, temp2, temp2, temp2, temp2, temp2, temp2, andResult);

endmodule
