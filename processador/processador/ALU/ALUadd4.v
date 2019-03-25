module ALUadd1 (
	data1,
	aluResult
);
	input wire [31:0] data1;
	output reg [31:0] aluResult;

	always @ (data1) begin
		aluResult = data1 + 1;
	end
endmodule