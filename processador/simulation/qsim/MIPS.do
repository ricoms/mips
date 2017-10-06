onerror {exit -code 1}
vlib work
vlog -work work MIPS.vo
vlog -work work UC_wave.vwf.vt
vsim -novopt -c -t 1ps -L cycloneive_ver -L altera_ver -L altera_mf_ver -L 220model_ver -L sgate work.MIPS_vlg_vec_tst -voptargs="+acc"
vcd file -direction MIPS.msim.vcd
vcd add -internal MIPS_vlg_vec_tst/*
vcd add -internal MIPS_vlg_vec_tst/i1/*
run -all
quit -f
