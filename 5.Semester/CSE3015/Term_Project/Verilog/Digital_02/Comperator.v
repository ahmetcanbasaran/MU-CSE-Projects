module Comperator (
    input wire [19:0] a,
    input wire [19:0] b,
    output reg [2:0] out
    );

    always @* begin
      if (a<b) begin
        out[1] = 0;
        out[2] = 1;
        out[0] = 0;
      end
      else if (a==b) begin
        out[1] = 1;
        out[2] = 0;
        out[0] = 0;
      end
      else begin
        out[1] = 0;
        out[2] = 0;
        out[0] = 1;
      end
    end
endmodule
