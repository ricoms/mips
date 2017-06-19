library verilog;
use verilog.vl_types.all;
entity MIPS_vlg_sample_tst is
    port(
        clk_fpga        : in     vl_logic;
        interrupt       : in     vl_logic;
        reset           : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end MIPS_vlg_sample_tst;
