module Instructions_memory(clock, address, instrucao);
	input clock;
	input [9:0] address;
	
	output reg [31:0] instrucao;
	//integer clock0 = 0;
	reg [31:0] RAM[80:0];
	
	always @ ( posedge clock ) begin
		if (address == 0) begin
		// programa 1: fibonacci
			RAM[0] = 32'b100011_00000_11111_0000000000000000;
			// ldi $0, $0, 0
			RAM[1] = 32'b101010_00000_11110_0000000000000000;
			// st user_number $30
			RAM[2] = 32'b100010_00000_11111_0000000000000000;
			// ld display_reg $31 user_number
			RAM[3] = 32'b100010_00000_00000_0000000000000000;
			// ld user_number $0
			RAM[4] = 32'b100011_00000_00001_0000000000000001;
			// ldi $1, $0, 1
			RAM[5] = 32'b100011_00000_00010_0000000000000000;
			// ldi $2, $0, 0
			RAM[6] = 32'b000000_00000_00001_00000_00000_000010;
			// *loop sub $0, $0, $2
			RAM[7] = 32'b000100_00000_00010_0000000000111101;
			// beq $0 $2, pqp
			RAM[8] = 32'b000000_11111_00001_11111_00000_000001;
			// sum $31 = $31 + $1
			RAM[9] = 32'b000000_11111_00001_00001_00000_000010;
			// sub $1 = $31 - $1
			RAM[10] = 32'b010000_00000000000000000000000101;
			// jump to 6
			
		// programa 2: fatorial
			RAM[15] = 32'b100011_00000_11111_0000000000000000;
			// ldi $0, $0, 0
			RAM[16] = 32'b101010_00000_11110_0000000000000000;
			// st $30 M[0]			
			RAM[17] = 32'b100010_11111_11111_0000000000000000;
			// ld display_reg $31 user_number
			RAM[18] = 32'b100010_00000_00000_0000000000000000;
			// ld user_number $0
			RAM[19] = 32'b100011_00001_00001_0000000000000001;
			// ldi $1, $0, 1
			RAM[20] = 32'b100011_00010_00010_0000000000000000;
			// ldi $2, $0, 0
			RAM[21] = 32'b000000_00000_00001_00000_00000_000010;
			// *loop sub $0 = $0 - $1
			RAM[22] = 32'b000100_00000_00010_0000000000111101;
			// beq $0 $2, pqp
			RAM[23] = 32'b000000_11111_00000_11111_00000_001001;
			// $31 = $31 * $0
			RAM[24] = 32'b010000_00000000000000000000010100;
			// jump to 20
			
			
		// programa 3: sintetico
			RAM[30] = 32'b100011_00000_11111_0000000000000000;
			// ldi $0, $0, 0
			RAM[31] = 32'b101010_00000_11110_0000000000000000;
			// st user_number $30 M[0]
			RAM[32] = 32'b100010_11111_11111_0000000000000000;
			//ld display_reg $31 user_number
			RAM[33] = 32'b100011_00001_00001_0000000000000010;
			// ldi $1, $0, 2
			RAM[34] = 32'b000000_11111_00001_11111_00000_000111;
			// shift left $31 << 2
			RAM[35] = 32'b000000_11111_00001_11111_00000_001000;
			// shift left $31 >> 2
			
			//clock0 <= 0;
		end
		instrucao = RAM[address];
	end
	
endmodule
