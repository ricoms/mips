module ALUadd (
	data1, data2,
	aluResult
);
	input wire [31:0] data1, data2;
	output reg [31:0] aluResult;
	
	always @ (data1 or data2) begin
		aluResult = data1 + data2;
	end
endmodule