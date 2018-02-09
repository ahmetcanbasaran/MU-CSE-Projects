module RAM (
  clk,        // Clock Input
  address,    // Address Input
  data_in,    // Data input
  str,        // Write Enable/Read Enable
  ld,         // Output Enable
  data_out    // Data output
); 

parameter DATA_WIDTH = 20;
parameter ADDR_WIDTH = 12;
parameter RAM_DEPTH = 1 << 12;  // 2^12 = 4,096

input clk;
input [ADDR_WIDTH-1 : 0] address;
input str;
input ld; 
input [DATA_WIDTH-1 : 0]  data_in;
output [DATA_WIDTH-1 : 0] data_out;

reg [DATA_WIDTH-1 : 0] data;
reg [DATA_WIDTH-1 : 0] mem [0 : RAM_DEPTH-1]; 

// Memory Write Block 
// Write Operation : When str = 1, ld = 1
always @ (posedge clk)
begin : MEM_WRITE
   if (str && !ld)
   begin
      mem[address] = data_in;
   end
end

// Memory Read Block 
// Read Operation : When str = 0, ld = 1
always @ (posedge clk)
begin: MEM_READ
  if (!str && ld)
  begin
    data = mem[address];
  end
end

assign data_out = data;

endmodule // End of Module RAM