module MUX32bits (
	input [31:0] data1, data2,
	input sign,
	output [31:0] mux_out
);

	assign mux_out = (sign == 1'b1) ? data2 : data1;

endmodule