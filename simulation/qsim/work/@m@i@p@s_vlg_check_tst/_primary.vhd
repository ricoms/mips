library verilog;
use verilog.vl_types.all;
entity MIPS_vlg_check_tst is
    port(
        aluOp           : in     vl_logic_vector(1 downto 0);
        aluSrc          : in     vl_logic;
        branch          : in     vl_logic;
        instrucao       : in     vl_logic_vector(31 downto 0);
        jump            : in     vl_logic;
        memRead         : in     vl_logic;
        memWrite        : in     vl_logic;
        memtoReg        : in     vl_logic;
        regDst          : in     vl_logic;
        regWrite        : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end MIPS_vlg_check_tst;
