module ALUControl (
	instr, ALUOp,
	instr_out
);
	input [5:0] instr;
	input [2:0] ALUOp;
	
	output reg [5:0] instr_out;

	always @ (ALUOp) begin
		case (ALUOp)
			3'b001: begin
				instr_out = 6'b000000; // passa data1 original
			end
			3'b011: begin
				instr_out = 6'b100000; // passa data2 original - ldi
			end
			3'b100: begin
				instr_out = 6'b100001; // branch equal
			end
			3'b101: begin
				instr_out = 6'b100010; // branch not equal
			end
			default: begin
				instr_out = instr; // r-type
			end
		endcase
	end
	
endmodule