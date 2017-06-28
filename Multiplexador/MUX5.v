module MUX5bits (
	input [4:0] data1, data2,
	input sign,
	output [4:0] mux_out
);

	assign mux_out = (sign == 1'b1) ? data2 : data1;

endmodule