module program_counter(clock, address, interrupt, reset, programCounter, progr);

	input wire clock, interrupt, reset;
	input wire [1:0] progr;
	input [31:0] address;
	output reg [31:0] programCounter = 0;
	
	always @ ( posedge clock ) begin
		if (reset) begin
			case (progr)
				2'b00: programCounter <= 0;
				2'b01: programCounter <= 25;
				2'b11: programCounter <= 35;
				default: programCounter <= address;
			endcase
		end
		else begin
			programCounter <= address;
		end
	end
	
endmodule