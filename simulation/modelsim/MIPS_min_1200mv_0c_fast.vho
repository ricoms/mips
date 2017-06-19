-- Copyright (C) 1991-2013 Altera Corporation
-- Your use of Altera Corporation's design tools, logic functions 
-- and other software and tools, and its AMPP partner logic 
-- functions, and any output files from any of the foregoing 
-- (including device programming or simulation files), and any 
-- associated documentation or information are expressly subject 
-- to the terms and conditions of the Altera Program License 
-- Subscription Agreement, Altera MegaCore Function License 
-- Agreement, or other applicable license agreement, including, 
-- without limitation, that your use is for the sole purpose of 
-- programming logic devices manufactured by Altera and sold by 
-- Altera or its authorized distributors.  Please refer to the 
-- applicable agreement for further details.

-- VENDOR "Altera"
-- PROGRAM "Quartus II 64-Bit"
-- VERSION "Version 13.1.0 Build 162 10/23/2013 SJ Web Edition"

-- DATE "05/07/2017 07:59:59"

-- 
-- Device: Altera EP4CE115F29C7 Package FBGA780
-- 

-- 
-- This VHDL file should be used for ModelSim-Altera (VHDL) only
-- 

LIBRARY CYCLONEIVE;
LIBRARY IEEE;
USE CYCLONEIVE.CYCLONEIVE_COMPONENTS.ALL;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY 	MIPS IS
    PORT (
	clk_fpga : IN std_logic;
	reset : IN std_logic;
	interrupt : IN std_logic;
	PC_goto_add4 : BUFFER std_logic_vector(7 DOWNTO 0)
	);
END MIPS;

-- Design Ports Information
-- clk_fpga	=>  Location: PIN_G6,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- reset	=>  Location: PIN_Y13,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- interrupt	=>  Location: PIN_F5,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[0]	=>  Location: PIN_D1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[1]	=>  Location: PIN_R28,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[2]	=>  Location: PIN_AG25,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[3]	=>  Location: PIN_G11,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[4]	=>  Location: PIN_F1,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[5]	=>  Location: PIN_A23,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[6]	=>  Location: PIN_D28,	 I/O Standard: 2.5 V,	 Current Strength: Default
-- PC_goto_add4[7]	=>  Location: PIN_H5,	 I/O Standard: 2.5 V,	 Current Strength: Default


ARCHITECTURE structure OF MIPS IS
SIGNAL gnd : std_logic := '0';
SIGNAL vcc : std_logic := '1';
SIGNAL unknown : std_logic := 'X';
SIGNAL devoe : std_logic := '1';
SIGNAL devclrn : std_logic := '1';
SIGNAL devpor : std_logic := '1';
SIGNAL ww_devoe : std_logic;
SIGNAL ww_devclrn : std_logic;
SIGNAL ww_devpor : std_logic;
SIGNAL ww_clk_fpga : std_logic;
SIGNAL ww_reset : std_logic;
SIGNAL ww_interrupt : std_logic;
SIGNAL ww_PC_goto_add4 : std_logic_vector(7 DOWNTO 0);
SIGNAL \clk_fpga~input_o\ : std_logic;
SIGNAL \reset~input_o\ : std_logic;
SIGNAL \interrupt~input_o\ : std_logic;
SIGNAL \PC_goto_add4[0]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[1]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[2]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[3]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[4]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[5]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[6]~output_o\ : std_logic;
SIGNAL \PC_goto_add4[7]~output_o\ : std_logic;

BEGIN

ww_clk_fpga <= clk_fpga;
ww_reset <= reset;
ww_interrupt <= interrupt;
PC_goto_add4 <= ww_PC_goto_add4;
ww_devoe <= devoe;
ww_devclrn <= devclrn;
ww_devpor <= devpor;

-- Location: IOOBUF_X0_Y68_N9
\PC_goto_add4[0]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[0]~output_o\);

-- Location: IOOBUF_X115_Y34_N23
\PC_goto_add4[1]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[1]~output_o\);

-- Location: IOOBUF_X91_Y0_N23
\PC_goto_add4[2]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[2]~output_o\);

-- Location: IOOBUF_X25_Y73_N16
\PC_goto_add4[3]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[3]~output_o\);

-- Location: IOOBUF_X0_Y59_N16
\PC_goto_add4[4]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[4]~output_o\);

-- Location: IOOBUF_X102_Y73_N2
\PC_goto_add4[5]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[5]~output_o\);

-- Location: IOOBUF_X115_Y60_N16
\PC_goto_add4[6]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[6]~output_o\);

-- Location: IOOBUF_X0_Y59_N23
\PC_goto_add4[7]~output\ : cycloneive_io_obuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	open_drain_output => "false")
-- pragma translate_on
PORT MAP (
	i => GND,
	devoe => ww_devoe,
	o => \PC_goto_add4[7]~output_o\);

-- Location: IOIBUF_X0_Y67_N15
\clk_fpga~input\ : cycloneive_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_clk_fpga,
	o => \clk_fpga~input_o\);

-- Location: IOIBUF_X52_Y0_N8
\reset~input\ : cycloneive_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_reset,
	o => \reset~input_o\);

-- Location: IOIBUF_X0_Y65_N15
\interrupt~input\ : cycloneive_io_ibuf
-- pragma translate_off
GENERIC MAP (
	bus_hold => "false",
	simulate_z_as => "z")
-- pragma translate_on
PORT MAP (
	i => ww_interrupt,
	o => \interrupt~input_o\);

ww_PC_goto_add4(0) <= \PC_goto_add4[0]~output_o\;

ww_PC_goto_add4(1) <= \PC_goto_add4[1]~output_o\;

ww_PC_goto_add4(2) <= \PC_goto_add4[2]~output_o\;

ww_PC_goto_add4(3) <= \PC_goto_add4[3]~output_o\;

ww_PC_goto_add4(4) <= \PC_goto_add4[4]~output_o\;

ww_PC_goto_add4(5) <= \PC_goto_add4[5]~output_o\;

ww_PC_goto_add4(6) <= \PC_goto_add4[6]~output_o\;

ww_PC_goto_add4(7) <= \PC_goto_add4[7]~output_o\;
END structure;


