module program_counter(clock, address, interrupt, reset, programCounter, program);

	input wire clock, interrupt, reset, program;
	input [31:0] address;
	output reg [31:0] programCounter = 32'b00000000000000000000000000000000;
		
	always @ ( posedge clock ) begin
		if (reset) begin
			case (program)
				1'b0: programCounter <= 0;
				1'b1: programCounter <= 15;
			endcase
		end
		else begin
			programCounter <= address;
		end
	end
	
endmodule