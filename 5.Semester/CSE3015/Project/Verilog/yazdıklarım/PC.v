module pc(clock, PRS, Data, CCE, pcout);
    
	input clock;
    input PRS;
	input CCE;
    input [19:0] Data;
    output reg [19:0] pcout;
	
	initial
	begin	
		pcout <= 20'h00000;
	end
	
    always @(posedge clock)
    begin    
		
		if (CCE == 1)
		begin
			pcout = pcout + 1;
		end
		
		if (PRS == 1)
		begin
			pcout = Data;
		end
		
	end
	
endmodule