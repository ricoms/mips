module ALU (
	data1, data2,
	operation,
	ALUOp,
	zero,
	aluResult
);
	input wire [31:0] data1, data2;
	input wire [5:0] operation;
	input wire [1:0] ALUOp;
	
	output reg zero;
	output reg [31:0] aluResult;
	
	always @ (operation or data1 or data2 or ALUOp) begin
		case (ALUOp)
			2'b01: aluResult = data2;     // passa imediato original - ldi
            // passa imediato (* 4) (usado para endereco) - (ld  e st)
			2'b11: aluResult = data2;
			default:
			case (operation)
				6'b000000: aluResult = data1; 		   // passa direto - ld
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
			endcase
		endcase
	end
	always @ (operation or data1 or data2 or ALUOp) begin
		case (ALUOp)
			2'b10: zero = (data1 == data2) ? 0 : 1;   // BNE
			default: zero = (data1 == data2) ? 1 : 0; // BEQ
		endcase
	end

endmodule