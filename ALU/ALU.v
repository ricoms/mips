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
	
	reg [31:0] result;
	output reg zero;
	output reg [31:0] aluResult;
	
	always @ (*) begin
		case (operation)
			6'b000000: result = data1; 		   // passa direto - ld
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
			default: result = 0;
		endcase
		case (ALUOp)
			2'b10: begin
				zero = (data1 == data2) ? 1'b0 : 1'b1;   // BNE
				aluResult = result;
			end
			2'b01: begin
				zero = (data1 == data2) ? 1'b1 : 1'b0; // BEQ
				aluResult = data2; // passa imediato original - ldi
			  // passa imediato (* 4) (usado para endereco) - (ld  e st)
			end
			2'b11: begin
				zero = (data1 == data2) ? 1'b1 : 1'b0; // BEQ
				aluResult = data2;
			end
			default: begin
				zero = (data1 == data2) ? 1'b1 : 1'b0; // BEQ
				aluResult = result;
			end
		endcase
	end

endmodule