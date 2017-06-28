module MUX32bits (
	input [31:0] data1, data2,
	input sign,
	output reg [31:0] mux_out
);

	always @ (data1 or data2) begin
		case (sign)
		   1'b0: mux_out = data1;
			1'b1: mux_out = data2;
		endcase
	end	
endmodule