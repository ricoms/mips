module ALU (
	data1, data2,
	operation,
	zero,
	aluResult
);
	input [31:0] data1, data2;
	input [5:0] operation;
	
	output zero;
	output reg [31:0] aluResult;

	always @ (data1 or data2 or operation) begin
		case (operation)
			6'b000001: aluResult = data1 + data2;    // add
			6'b000010: aluResult = data1 - data2;    // sub
			6'b000011: aluResult = data1 & data2;    // and
			6'b000100: aluResult = data1 | data2;    // or
			6'b000101: aluResult = data1 ^ data2;    // xor
			6'b000110: aluResult = ~data1; 		     // not
			6'b000111: aluResult = data1 << data2;   // shift left
			6'b001000: aluResult = data1 >> data2;   // shift right
			6'b001001: aluResult = data1 * data2;    // multiplicacao
			6'b001010: aluResult = data1 / data2;    // divisao
			6'b001011: aluResult = data1 % data2;    // modulo
			6'b100000: aluResult = data2;				  // passa data2 direto - ldi
			6'b100001: aluResult = (data1 == data2); // passa data2 direto - ldi
			6'b100010: aluResult = (data1 != data2); // passa data2 direto - ldi
			default: aluResult = data1; 		        // passa direto - ld
		endcase
	end
	
	assign zero = (aluResult == 0);
endmodule
