module ALU (
	data1, data2,
	operation,
	ALUOp,
	zero,
	aluResult
);
	input [31:0] data1, data2;
	input [5:0] operation;
	input [1:0] ALUOp;
	
	reg [31:0] result;
	output reg zero;
	output reg [31:0] aluResult;
	
	/*always @ (data1 or data2 or operation or ALUOp) begin
		case (operation)
			6'b000001: result = data1 + data2;  // add
			6'b000010: result = data1 - data2;  // sub
			6'b000011: result = data1 & data2;  // and
			6'b000100: result = data1 | data2;  // or
			6'b000101: result = data1 ^ data2;  // xor
			6'b000110: result = ~data1; 		   // not
			6'b000111: result = data1 << data2; // shift left
			6'b001000: result = data1 >> data2; // shift right
			6'b001001: result = data1 * data2;  // multiplicacao
			6'b001010: result = data1 / data2;  // divisao
			6'b001011: result = data1 % data2;  // modulo
			default: result = data1; 		      // passa direto - ld
		endcase
	end*/
	always @ (data1 or data2 or operation or ALUOp) begin
		case (ALUOp)
			2'b01: begin
				zero = (data1 == data2) ? 1'b0 : 1'b1;   // BNE
				aluResult = data2; // passa imediato original - ldi
			end
			2'b11: begin
				zero = (data1 == data2) ? 1'b1 : 1'b0; // BEQ
				aluResult = data2; // passa imediato original - ldi
			end
			default: begin
				zero = (data1 == data2) ? 1'b1 : 1'b0; // BEQ
				case (operation)
					6'b000001: aluResult = data1 + data2;  // add
					6'b000010: aluResult = data1 - data2;  // sub
					6'b000011: aluResult = data1 & data2;  // and
					6'b000100: aluResult = data1 | data2;  // or
					6'b000101: aluResult = data1 ^ data2;  // xor
					6'b000110: aluResult = ~data1; 		   // not
					6'b000111: aluResult = data1 << data2; // shift left
					6'b001000: aluResult = data1 >> data2; // shift right
					6'b001001: aluResult = data1 * data2;  // multiplicacao
					6'b001010: aluResult = data1 / data2;  // divisao
					6'b001011: aluResult = data1 % data2;  // modulo
					default: aluResult = data1; 		      // passa direto - ld
				endcase
			end
		endcase
	end
	
	//assign zero = (result == 0);
endmodule
