module registers (
	readRegister1, readRegister2, writeRegister,
	clock, RegWrite, user_number,
	writeData,
	readData1, readData2,
	toDisplay
);
	input [4:0] readRegister1, readRegister2, writeRegister;
	input clock, RegWrite;
	input [31:0] writeData;
	input [5:0] user_number;
		
	output [31:0] readData1, readData2;
	output [31:0] toDisplay;
	
	reg [31:0] registerFile[31:0];
	
	always @ (posedge clock) begin
		if(RegWrite == 1) begin
			registerFile[writeRegister] = writeData;
		end
		registerFile[30] = user_number;
	end
	
	assign readData1 = registerFile[readRegister1];
	assign readData2 = registerFile[readRegister2];
	assign toDisplay = registerFile[31];

endmodule
