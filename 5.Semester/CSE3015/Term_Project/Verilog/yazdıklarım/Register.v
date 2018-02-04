
`include "DFF.v"

module Register(PCOut,PCin,select,clk);  
 output [19:0] PCOut;  
 input [19:0] PCin;  
 input select,clk;

wire [19:0] in;
 

assign in = (select==1'b1) ? PCin : in;


D_FF dff0(PCOut[0],in[0],clk);  
DFF dff1(PCOut[1],in[1],clk);  
DFF dff2(PCOut[2],in[2],clk);  
DFF dff3(PCOut[3],in[3],clk);  
DFF dff4(PCOut[4],in[4],clk);  
DFF dff5(PCOut[5],in[5],clk);  
DFF dff6(PCOut[6],in[6],clk);  
DFF dff7(PCOut[7],in[7],clk);  
DFF dff8(PCOut[8],in[8],clk);  
DFF dff9(PCOut[9],in[9],clk);  
DFF dff10(PCOut[10],in[10],clk);  
DFF dff11(PCOut[11],in[11],clk);  
DFF dff12(PCOut[12],in[12],clk);  
DFF dff13(PCOut[13],in[13],clk);  
DFF dff14(PCOut[14],in[14],clk);  
DFF dff15(PCOut[15],in[15],clk);  
DFF dff16(PCOut[16],in[16],clk);  
DFF dff17(PCOut[17],in[17],clk);  
DFF dff18(PCOut[18],in[18],clk);  
DFF dff19(PCOut[19],in[19],clk);  


 
endmodule  