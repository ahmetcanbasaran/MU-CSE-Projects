module ROM(
	address , // Address input
	data      // Data output
);

	input [19:0] address;
	output [19:0] data; 
			   
	reg [19:0] mem [0:19] ;  
		  
	assign data = mem[address];

	initial begin
	  $readmemb("memory.txt", mem); // memory_list is memory file
		mem[0] = 20'b11010101010101010101;
		mem[1] = 20'b11010101010101010101;
		mem[2] = 20'b11010101010101010101;
		mem[3] = 20'b01010101010101010101;
	end

endmodule