module RFID(RAM, ALU, isArithmetic, input_data, reg1_out,
			dr, isStore, reg2_out, reg3, isBrach, reg1_in, reg2_in);
    
	input isArithmetic;
	input isStore;
	input isBrach;
	input [19:0] RAM;
	input [19:0] ALU;
	input [3:0] reg3;
	input [3:0] reg1_in; 
	input [3:0] reg2_in;
	output reg [3:0] dr;
	output reg [3:0] reg1_out;
	output reg [3:0] reg2_out;
	output reg [19:0] input_data;
	
    always @(*)
    begin    
		
		if (isArithmetic == 0)
		begin
			input_data <= RAM;
		end

		else
		begin
			input_data <= ALU;
		end
	
		
		if (isBrach == 0)
		begin
			reg2_out <= reg3;
			dr <= reg1_in;
			
			if (isStore == 0)
			begin
				reg1_out <= reg2_in;
			end
			else
			begin
				reg1_out <= reg1_in;
			end			
		end
		else
		begin
			reg2_out <= reg2_in;
			reg1_out <= reg1_in;
		end
	end
	
endmodule