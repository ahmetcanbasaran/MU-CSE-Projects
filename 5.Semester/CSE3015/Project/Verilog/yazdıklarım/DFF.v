module D_FF(
  out, // output
  data, // Data Input
  clk // clk
  
);
// MARK: Input
input data, clk; 

//MARK: Output
output out;

// MARK: Internel Variables
reg out;

//-------------Start---------
always @ ( posedge clk) begin
  out <= data;
end

endmodule //End Of Module dlatch