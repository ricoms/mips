library verilog;
use verilog.vl_types.all;
entity MIPS is
    port(
        clk_fpga        : in     vl_logic;
        reset           : in     vl_logic;
        interrupt       : in     vl_logic;
        regDst          : out    vl_logic;
        jump            : out    vl_logic;
        branch          : out    vl_logic;
        memRead         : out    vl_logic;
        memtoReg        : out    vl_logic;
        memWrite        : out    vl_logic;
        aluSrc          : out    vl_logic;
        regWrite        : out    vl_logic;
        aluOp           : out    vl_logic_vector(1 downto 0);
        instrucao       : out    vl_logic_vector(31 downto 0)
    );
end MIPS;
