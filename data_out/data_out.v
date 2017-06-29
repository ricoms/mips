module mainMemory(clock, data_in, address, MemWrite, data_out);
	input clock, MemWrite;
	input [31:0] data_in;
	input [9:0] address;
	output [31:0] data_out;
	reg [9:0] addressRegister;
	
	reg [31:0] ram[40:0];
	always @ ( posedge clock ) begin
		if ( MemWrite ) begin
			ram[address] = data_in;
		end
		addressRegister = address;
	end
	
	assign data_out = ram[address];

endmodule