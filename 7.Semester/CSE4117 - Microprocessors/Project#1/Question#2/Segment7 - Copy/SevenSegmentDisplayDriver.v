module SevenSegmentDisplayDriver(grounds, grounds1, display, clk, switches, volt, ground);

	output reg [3:0] grounds;
	output reg [6:0] display;
	output reg [3:0] grounds1;
	reg [3:0] old_grounds;
	output reg volt;
	output reg ground;
	input [3:0] switches;
	input clk;
	reg blinkMode;
	reg blink;
	reg goLeft;
	reg swing;
	reg [4:0] counter;
	reg [3:0] data [17:0];  //number to be printed on display
	reg [1:0] count;  //which data byte to display.
	reg [25:0] clk1;
	reg [71:0] din;
	reg speed;
	
	always @(posedge clk)
		clk1<=clk1+1;
	
	always @(posedge clk1[15]) begin  //25 slow //19 wavy //15 perfect
		count<=count+1;
		grounds={grounds[2:0],grounds[3]};
		if(blink)
			grounds1<=4'b1111;
		else
			grounds1<=grounds;
	end
	
	always @(posedge clk1[21]) begin
		if(blinkMode)
			blink<=~blink;
		else
			blink=0;
	end
	
	always @(*) begin
		case(switches[0])
			0: speed = 0;
			1: speed = 1;
		endcase
		case(switches[1])
			0: swing = 0;
			1: swing = 1;
		endcase
		case(switches[3])
			0:	blinkMode = 0;
			1: blinkMode = 1;
		endcase
	end		
			
	always @(posedge clk1[24-speed]) begin
		if(swing) begin

			if(counter == 14)
				counter=0;
			else
				counter=counter+1;
				
			if(counter == 0)
				goLeft=~goLeft;
		
			if(goLeft) begin  // Sola kayma
				data[0]<=data[17];
				data[17]<=data[16];
				data[16]<=data[15];
				data[15]<=data[14];
				data[14]<=data[13];
				data[13]<=data[12];
				data[12]<=data[11];
				data[11]<=data[10];
				data[10]<=data[9];
				data[9]<=data[8];
				data[8]<=data[7];
				data[7]<=data[6];
				data[6]<=data[5];
				data[5]<=data[4];
				data[4]<=data[3];
				data[3]<=data[2];
				data[2]<=data[1];
				data[1]<=data[0];
			end
			else begin  // Sağa kayma
				data[17]<=data[0];
				data[16]<=data[17];
				data[15]<=data[16];
				data[14]<=data[15];
				data[13]<=data[14];
				data[12]<=data[13];
				data[11]<=data[12];
				data[10]<=data[11];
				data[9]<=data[10];
				data[8]<=data[9];
				data[7]<=data[8];
				data[6]<=data[7];
				data[5]<=data[6];
				data[4]<=data[5];
				data[3]<=data[4];
				data[2]<=data[3];
				data[1]<=data[2];
				data[0]<=data[1];
			end
		end
		else begin
			if(!switches[2]) begin  // Sola kayma
				data[0]<=data[17];
				data[17]<=data[16];
				data[16]<=data[15];
				data[15]<=data[14];
				data[14]<=data[13];
				data[13]<=data[12];
				data[12]<=data[11];
				data[11]<=data[10];
				data[10]<=data[9];
				data[9]<=data[8];
				data[8]<=data[7];
				data[7]<=data[6];
				data[6]<=data[5];
				data[5]<=data[4];
				data[4]<=data[3];
				data[3]<=data[2];
				data[2]<=data[1];
				data[1]<=data[0];
			end
			else begin  // Sağa kayma
				data[17]<=data[0];
				data[16]<=data[17];
				data[15]<=data[16];
				data[14]<=data[15];
				data[13]<=data[14];
				data[12]<=data[13];
				data[11]<=data[12];
				data[10]<=data[11];
				data[9]<=data[10];
				data[8]<=data[9];
				data[7]<=data[8];
				data[6]<=data[7];
				data[5]<=data[6];
				data[4]<=data[5];
				data[3]<=data[4];
				data[2]<=data[3];
				data[1]<=data[2];
				data[0]<=data[1];
			end
		end
	end
	
	always @(*)
		case(data[count])
			0:display=7'b1111110; //starts with a, ends with g
			1:display=7'b0110000;
			2:display=7'b1101101;
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
			default display=7'b0000000;
		endcase
		
	initial begin
		din=72'h150114022150114026;
	
		data[0]<=din[59:56];
		data[1]<=din[63:60];
		data[2]<=din[67:64];
		data[3]<=din[71:68];
		data[4]<=din[3:0];
		data[5]<=din[7:4];
		data[6]<=din[11:8];
		data[7]<=din[15:12];
		data[8]<=din[19:16];
		data[9]<=din[23:20];
		data[10]<=din[27:24];
		data[11]<=din[31:28];
		data[12]<=din[35:32];
		data[13]<=din[39:36];
		data[14]<=din[43:40];
		data[15]<=din[47:43];
		data[16]<=din[51:48];
		data[17]<=din[55:52];
		
		count = 2'b0;
		grounds=4'b1110;
		clk1=0;
		volt = 1;
		ground = 0;
		speed = 0;
		blinkMode = 0;
		blink = 0;
		goLeft = 1;
		swing = 0;
		counter = 5'b00000;
	end
endmodule