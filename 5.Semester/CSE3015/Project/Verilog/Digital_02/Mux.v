
module mux2to1(out, in0, in1, sel);
	input [19:0 ] in0;
	input [19:0] in1;
	input sel;
	output [19:0] out;
	assign out = (sel==1'b0) ? in0 : in1;
endmodule

module mux4to1(out, in0, in1, in2, in3, sel);
	input [19:0] in0;
	input [19:0] in1;
	input [19:0] in2;
	input [19:0] in3;
	input [1:0] sel;
	output [19:0] out;

	assign out = (sel==2'b00) ? in0 : 
		(sel==2'b01) ? in1 : 
		(sel==2'b10) ? in2 :
		in3;
endmodule

module mux8to1(out, in0, in1, in2, in3, in4, in5, in6, in7, sel);
	input [19:0] in0, in1, in2, in3, in4, in5, in6, in7;
	input [2:0] sel;
	output [19:0] out;
	assign out = 
		(sel==3'h0) ? in0 : 
		(sel==3'h1) ? in1 : 
		(sel==3'h2) ? in2 : 
		(sel==3'h3) ? in3 : 
		(sel==3'h4) ? in4 : 
		(sel==3'h5) ? in5 : 
		(sel==3'h6) ? in6 :
		in7;
endmodule

module mux16to1(out, in0, in1, in2, in3, in4, in5, in6, in7, in8, in9, in10,
in11, in12, in13, in14, in15, sel);
	input [19:0] in0, in1, in2, in3, in4, in5, in6, in7, in8, in9, in10,
		in11, in12, in13, in14, in15;
	input [3:0] sel;
	output [19:0] out;
	assign out = 
		(sel==4'h0) ? in0 : 
		(sel==4'h1) ? in1 : 
		(sel==4'h2) ? in2 : 
		(sel==4'h3) ? in3 : 
		(sel==4'h4) ? in4 : 
		(sel==4'h5) ? in5 : 
		(sel==4'h6) ? in6 : 
		(sel==4'h7) ? in7 : 
		(sel==4'h8) ? in8 : 
		(sel==4'h9) ? in9: 
		(sel==4'ha) ? in10: 
		(sel==4'hb) ? in11 : 
		(sel==4'hc) ? in12 : 
		(sel==4'hd) ? in13 : 
		(sel==4'he) ? in14 : 
		in15;
endmodule