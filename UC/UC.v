module Unidade_de_controle(instrucao, regDst, jump, branch, memRead, memtoReg, aluOp, memWrite, aluSrc, regWrite);
	input [5:0] instrucao;

	output reg regDst, jump, branch, memRead, memtoReg, memWrite, aluSrc, regWrite;
	output reg [2:0] aluOp;
	
	always@ (instrucao) begin
		case(instrucao)
			6'b000000:begin // R-type logic arithmetic
				regDst  	= 1'b1;
				aluSrc 	= 1'b0;
				memtoReg = 1'b0;
				regWrite = 1'b1;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b0;
				jump 		= 1'b0;
				aluOp 	= 2'b000;
			end
			6'b000001:begin // I-type logic arithmetic
				regDst  	= 1'b1;
				aluSrc 	= 1'b1;
				memtoReg = 1'b0;
				regWrite = 1'b1;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b0;
				jump 		= 1'b0;
				aluOp 	= 2'b000;
			end
			6'b100010:begin // load word
				regDst  	= 1'b0;
				aluSrc 	= 1'b1;
				memtoReg = 1'b1;
				regWrite = 1'b1;
				memRead 	= 1'b1;
				memWrite = 1'b0;
				branch 	= 1'b0;
				jump 		= 1'b0;
				aluOp 	= 2'b001;
			end
			6'b100011:begin // load word immediate
				regDst  	= 1'b0;
				aluSrc 	= 1'b1;
				memtoReg = 1'b0;
				regWrite = 1'b1;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b0;
				jump 		= 1'b0;
				aluOp 	= 2'b011;
			end
			6'b101010:begin // store word
				regDst  	= 1'b0;
				aluSrc 	= 1'b1;
				memtoReg = 1'b0;
				regWrite = 1'b0;
				memRead 	= 1'b0;
				memWrite = 1'b1;
				branch 	= 1'b0;
				jump 		= 1'b0;
				aluOp 	= 2'b001;
			end
			6'b000100:begin // branch if equal
				regDst  	= 1'b0;
				aluSrc 	= 1'b0;
				memtoReg = 1'b0;
				regWrite = 1'b0;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b1;
				jump 		= 1'b0;
				aluOp 	= 2'b100;
			end
			6'b000110:begin // branch if not equal
				regDst  	= 1'b0;
				aluSrc 	= 1'b0;
				memtoReg = 1'b0;
				regWrite = 1'b0;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b1;
				jump 		= 1'b0;
				aluOp 	= 2'b101;
			end
			6'b010000:begin // jump
				regDst  	= 1'b0;
				aluSrc 	= 1'b0;
				memtoReg = 1'b0;
				regWrite = 1'b0;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b0;
				jump 		= 1'b1;
				aluOp 	= 2'b000;
			end
			default:begin 
				regDst  	= 1'b0;
				aluSrc 	= 1'b0;
				memtoReg = 1'b0;
				regWrite = 1'b0;
				memRead 	= 1'b0;
				memWrite = 1'b0;
				branch 	= 1'b0;
				jump 		= 1'b0;
				aluOp 	= 2'b000;
			end
		endcase
	end
	
endmodule