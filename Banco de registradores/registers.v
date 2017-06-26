module registers (
	readRegister1, readRegister2, writeRegister,
	clock, RegWrite, user_number,
	writeData,
	readData1, readData2,
	toDisplay
);
	input wire [4:0] readRegister1, readRegister2, writeRegister;
	input wire clock, RegWrite;
	input wire [31:0] writeData;
	input wire [5:0] user_number;
	
	output wire [31:0] readData1, readData2;
	output wire [31:0] toDisplay;
	
	reg[31:0] registerFile[31:0];
	
	always @ (posedge clock) begin
		assign toDisplay = registerFile[31];
		assign registerFile[30] = {{26{'0'}}, {user_number}};
		if(RegWrite == 1)
			registerFile[writeRegister] = writeData;
	end
	assign readData1 = registerFile[readRegister1];
	assign readData2 = registerFile[readRegister2];

endmodule