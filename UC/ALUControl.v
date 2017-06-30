module ALUControl (
	operation,
	ALUOp, operation_out
);
	input [5:0] operation;
	input [2:0] ALUOp;
	
	output reg [5:0] operation_out;

	always @ (operation or ALUOp) begin
		case (ALUOp)
			2'b001: begin
				operation_out = 6'b000000; // passa data1 original
			end
			2'b011: begin
				operation_out = 6'b100000; // passa data2 original - ldi
			end
			2'b100: begin
				operation_out = 6'b100001; // branch equal
			end
			2'b101: begin
				operation_out = 6'b100010; // branch not equal
			end
			default: begin
				operation_out = operation;
			end
		endcase
	end
	
	//assign zero = (result == 0);
endmodule