module registerfile(
            input clk,
            input wr_en,
            input [3:0]rd0_addr,
            input [3:0]rd1_addr,
            input [3:0]wr_addr,
            input [19:0]wr_data,
            output reg [19:0]rd0_data,
            output reg [19:0]rd1_data);

    reg [19:0] mem[15:0];

    always @(posedge clk)
    begin
        if (wr_en) begin
            mem[wr_addr] <= wr_data;
        end
        rd0_data <= mem[rd0_addr];
        rd1_data <= mem[rd1_addr];
    
    end
endmodule