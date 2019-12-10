module Segment7(grounds, display, clk);

	output reg [3:0] grounds;
	output reg [6:0] display;
	input clk; 

	reg [3:0] data [4:0]; //number to be printed on display
	reg [1:0] count;       //which data byte to display.
	reg [25:0] clk1;
	reg [3:0] temp;
	
	always @(posedge clk1[15]) //25 slow //19 wavy //15 perfect
	begin
		grounds<={grounds[2:0],grounds[3]};
		count<=count+1;
	end

	always @(posedge clk1[25])
	begin
		data[4]<=data[3];
		data[3]<=data[2];
		data[2]<=data[1];
		data[1]<=data[0];
		data[0]<=data[4];
	end

	always @(posedge clk)
		clk1<=clk1+1;

	always @(*)
		case(data[count])
			0:display=7'b0110111; //starts with a, ends with g
			1:display=7'b0110000;
			2:display=7'b0001110;
			3:display=7'b1111001;
			4:display=7'b0110011;
			5:display=7'b1011011;
			6:display=7'b1011111;
			7:display=7'b1110000;
			8:display=7'b1111111;
			9:display=7'b1111011;
			'ha:display=7'b1110111;
			'hb:display=7'b0011111;
			'hc:display=7'b1001110;
			'hd:display=7'b0111101;
			'he:display=7'b1001111;
			'hf:display=7'b1000111;
			default display=7'b1111111;
	endcase

	initial begin
		data[0]=4'ha;
		data[1]=4'h2;
		data[2]=4'h1;
		data[3]=4'h0;
		data[4]=4'h2;
		count = 2'b0;
		grounds=4'b1110;
		clk1=0;
	end
endmodule