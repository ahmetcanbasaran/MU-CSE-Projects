module TopModule(reg0, grounds, display, clk50Mhz, clkPushButton);

	inout wire [15:0] reg0;
	output wire [3:0] grounds;
	output wire [6:0] display;
	input clk50Mhz, clkPushButton;

	SevenSegmentDisplayDriver sevenSegDriver(reg0, grounds, display, clk50Mhz);
	Frog cpu(clkPushButton, reg0);

endmodule