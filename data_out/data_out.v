module mainMemory(clock, data_in, address, MemWrite, data_out);
	input wire clock, MemWrite;
	input wire [31:0] data_in;
	input wire [9:0] address;
	output reg [31:0] data_out;
	
	reg [31:0] ram[40:0];
	always @ ( posedge clock ) begin
		data_out = ram[address];
		if ( MemWrite ) begin
			ram[address] = data_in;
		end
	end
		
endmodule