module MIPS (
	input wire clk_fpga, Dreset, interrupt, Dclock,
	input wire [5:0] user_number,
	input wire [1:0] progr,
	output wire [6:0] ones, tens, hundreds, thousands, programOnes,
	programTens, programHundreds, programThousands, userOnes, userTens,
	userHundreds, userThousands,
	output wire clock, jump, branch, memRead, memtoReg, memWrite, aluSrc, regWrite, regDst, reset,
	output wire [1:0] aluOp
);
	wire zero;
	wire [31:0] PC_backfrom_add1, PC_goto_add1, instrucao, data1, data2, memDataOut,
	muxBranch_out, muxJump_out, aluAddResult, mainAluResult, output32, toDisplay,
	returnToRegisters, muxRegDst_out, ULASrc_out;
	
	DeBounce db1(.clk(clk_fpga), .n_reset(1), .button_in(Dreset), .DB_out(reset));
	//input clk, n_reset, button_in, // inputs
	//output reg 	DB_out // output
 
	//divisor_frequencia df(.clk_alta_f(clk_fpga), .clk_baixa_f(clock));
	
	DeBounce db2(.clk(clk_fpga), .n_reset(1), .button_in(Dclock), .DB_out(clock));
	
	ALUadd1 AluAdd1(.data1(PC_goto_add1), .aluResult(PC_backfrom_add1));
	
	MUX32bits muxBranch(.data1(PC_backfrom_add1), .data2(aluAddResult),
						     .sign(branch & zero), .mux_out(muxBranch_out));
	MUX32bits muxJump(.data1(muxBranch_out),
						   .data2({{PC_backfrom_add1[31:28]}, {2'b00}, {instrucao[25:0] }}), //<< 2}}),
						   .sign(jump), .mux_out(muxJump_out));
	
	ALUadd ALUadd(.data1(PC_backfrom_add1), .data2(output32), // << 2),
			 .aluResult(aluAddResult));
	
	program_counter pc(.clock(clock), .address(muxJump_out),
							 .interrupt(interrupt), .reset(~reset),
							 .programCounter(PC_goto_add1), .progr(progr));
	
	Instructions_memory IM(.clock(clock), .address(PC_goto_add1), .instrucao(instrucao));
	
	Unidade_de_controle UC(.instrucao(instrucao[31:26]), .regDst(regDst),
							  .jump(jump), .branch(branch), .memRead(memRead),
							  .memtoReg(memtoReg), .aluOp(aluOp), .memWrite(memWrite),
							  .aluSrc(aluSrc), .regWrite(regWrite));
	
	MUX5bits muxRegDst(.data1(instrucao[20:16]), .data2(instrucao[15:11]),
						    .sign(regDst), .mux_out(muxRegDst_out));
	
	registers rgs(.readRegister1(instrucao[25:21]), .readRegister2(instrucao[20:16]),
	   .writeRegister(muxRegDst_out), .clock(clock), .RegWrite(regWrite), .user_number(user_number),
		.writeData(returnToRegisters), .readData1(data1), .readData2(data2), .toDisplay(toDisplay)
	);
	
	bitExtender be(.input16(instrucao[15:0]), .output32(output32));
		
	MUX32bits ULASrc(.data1(data2), .data2(output32),
						  .sign(aluSrc), .mux_out(ULASrc_out));
							  
	ALU MainALU(.data1(data1), .data2(ULASrc_out), .operation(instrucao[5:0]),
		 .zero(zero), .aluResult(mainAluResult));
	
	mainMemory MainMem(.clock(clock), .data_in(data2), .address(mainAluResult),
				  .MemWrite(memWrite), .data_out(memDataOut));
	
	MUX32bits finalMux(.data1(mainAluResult), .data2(memDataOut),
						     .sign(memtoReg), .mux_out(returnToRegisters));
							 
	Output out1(.binary(toDisplay), .ones(ones), .tens(tens), // ULASrc_out, toDisplay
			 .hundreds(hundreds), .thousands(thousands)); 
	
	Output out2(.binary(PC_goto_add1), .ones(programOnes), .tens(programTens),
			 .hundreds(programHundreds), .thousands(programThousands)); 
			 
	Output out3(.binary(32'b0 + user_number), .ones(userOnes), .tens(userTens),
			 .hundreds(userHundreds), .thousands(userThousands)); 
	
endmodule
