module MIPS (
	input wire clk_fpga, reset, interrupt,
	output wire regDst, jump, branch, memRead, memtoReg, memWrite, aluSrc, regWrite,
	output wire [1:0] aluOp,
	//output wire [31:0] PC_goto_add1,
	//input wire [15:0] input16,
	//output wire [31:0] output32
	output wire [31:0] instrucao
);

	//wire clock;
	//divisor_frequencia df(cerlk_fpga, clock);
	
	wire [31:0] PC_backfrom_add1;
	wire [31:0] PC_goto_add1;
	ALUadd1(.data1(PC_goto_add1), .aluResult(PC_backfrom_add1));
	program_counter pc(.clock(clk_fpga), .address(PC_backfrom_add1), .interrupt(interrupt), .reset(reset), .programCounter(PC_goto_add1));
	
	//wire [31:0] instrucao;
	Instructions_memory(.clock(clk_fpga), .address(PC_goto_add1), .instrucao(instrucao));
	
	Unidade_de_controle(.instrucao(instrucao[31:26]), .regDst(regDst), .jump(jump), .branch(branch),
							  .memRead(memRead), .memtoReg(memtoReg), .aluOp(aluOp),
							  .memWrite(memWrite), .aluSrc(aluSrc), .regWrite(regWrite));
	
	//ALU alu(data1, data2, operation, zero, aluResult);
	//bitExtender be( .input16(input16), .output32(output32));
	
endmodule
// memoria
// banco de registradores