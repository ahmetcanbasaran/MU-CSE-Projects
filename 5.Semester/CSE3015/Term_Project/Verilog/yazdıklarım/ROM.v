module ROM(
	address , // Address input
	data    , // Data output
	read_en , // Read Enable 
	ce        // Chip Enable
);

	input [19:0] address;
	output [19:0] data; 
	input read_en; 
	input ce; 
			   
	reg [19:0] mem [0:6] ;  
		  
	assign data = (ce && read_en) ? mem[address] : 20'b0;

	initial begin
	  $readmemb("memory.txt", mem); // memory_list is memory file
	end

endmodule