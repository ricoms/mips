module program_counter(clock, address, interrupt, reset, programCounter);

	input wire clock, interrupt, reset;
	input [31:0] address;
	reg [31:0] programCounter;
	output [31:0] programCounter;
	
	always @ ( posedge clock ) begin
		if (reset) begin
			programCounter <= 0;
		end
		else if (interrupt) begin
		end
		else begin
			programCounter <= address;
		end
	end
	
endmodule