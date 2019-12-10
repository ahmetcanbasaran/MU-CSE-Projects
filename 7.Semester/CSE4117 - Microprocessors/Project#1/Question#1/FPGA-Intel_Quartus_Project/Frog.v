module Frog(input wire clk, output [15:0] reg0 );

	reg [1:0] state;
	reg [15:0] memory[0:255];
	wire[15:0] src1, src2;
	wire[3:0] aluop;
	reg [15:0] pc, aluout, ir;
	reg [15:0] regbank[0:3];
	reg immsig;

	localparam FETCH = 2'b00;
	localparam LDI = 2'b01;
	localparam ALU = 2'b10;
	localparam ALUIMM = 2'b11;

	always @(posedge clk)
		case(state)
			FETCH: begin
				state<=memory[pc][15:14];
				ir<=memory[pc][11:0];
				pc<=pc+1;
				immsig<=0;
			end
			LDI: begin
				state<=FETCH;
				regbank[ ir[1:0] ] <= memory[pc];
				pc<=pc+1;
				immsig<=0;
			end
			ALU: begin
				state<=FETCH;
				regbank[ ir[1:0] ] <= aluout;
				immsig<=0;				
			end
			ALUIMM: begin
				state<=FETCH;
				regbank[ ir[1:0] ] <= aluout;  
				pc<=pc+1;
				immsig<=1;
			end
		endcase

	assign reg0 = regbank[ 0 ];
	assign src1=regbank[ir[7:6]];
	assign src2=regbank[ir[4:3]];
	assign aluop=ir[11:8];
	
	always @*
		case( aluop )
			4'h0:  aluout = src1 + src2;
			4'h1:  aluout = src1 - src2;
			4'h2:  aluout = src1 & src2;
			4'h3:  aluout = src1 | src2;
			4'h4:  aluout = src1 ^ src2;
			4'h5:  aluout = ~src1;
			4'h6:  aluout = src1;
			4'h7:  aluout = src1 + 16'h0001;
			4'h8:  aluout = src1 - 16'h0001;
			default: aluout = 0;
		endcase

	initial begin
		$readmemh("RAM", memory);  //must be exactly 512 locations
		state = FETCH;
	 end
endmodule