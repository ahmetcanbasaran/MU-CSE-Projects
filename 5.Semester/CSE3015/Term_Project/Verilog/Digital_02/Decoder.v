
module decoder16 (
binary_in   , //  4 bit binary input
decoder_out , //  16-bit out 
);
input [3:0] binary_in  ;
output [15:0] decoder_out ; 
        
wire [15:0] decoder_out ; 

assign decoder_out = (1 << binary_in);

endmodule