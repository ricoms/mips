module mainMemory(clock, data_in, address, MemWrite, MemRead, data_out);
	input clock, MemWrite, MemRead;
	input [31:0] data_in;
	input [9:0] address;
	output reg [31:0] data_out;
	reg [9:0] addressRegister;
	
	reg [31:0] ram[40:0];
	always @ ( posedge clock ) begin
		if ( MemWrite ) begin
			ram[address] = data_in;
		end
		addressRegister = address;
	end
	always @ (MemRead) begin
		data_out = ram[address];
	end

endmodule