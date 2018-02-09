
//-----------------------------------------------------
module PriorityEncoder_5_3 (
binary_out , //  3 bit binary output
encoder_in , //  5-bit input 
);

output [2:0] binary_out ;
input [4:0] encoder_in ; 

wire [2:0] binary_out ;
      
assign  binary_out  = (encoder_in == 5'b0_0001) ? 0 : 
    (encoder_in == 5'b0_0010) ? 1 : 
    (encoder_in == 5'b0_0100) ? 2 : 
    (encoder_in == 5'b0_1000) ? 3 : 4; 

endmodule 
