module registers (
	readRegister1, readRegister2, writeRegister,
	clock, RegWrite,
	writeData,
	readData1, readData2
);
	input wire [4:0] readRegister1, readRegister2, writeRegister;
	input wire clock, RegWrite;
	input wire [31:0] writeData;
	
	output wire [31:0] readData1, readData2;
	
	reg[31:0] registerFile[31:0];
	
	always @ (posedge clock) begin
			if(RegWrite == 1)
				registerFile[writeRegister] = writeData;
	end
	assign readData1 = registerFile[readRegister1];
	assign readData2 = registerFile[readRegister2];

endmodule