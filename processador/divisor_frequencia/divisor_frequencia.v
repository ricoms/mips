module divisor_frequencia(
 clk_alta_f ,
 clk_baixa_f
);
 input clk_alta_f;
 parameter n = 26;
 // 26 eh o numero de registradores para que 50Mhz/(2^26) = 1Hz

 reg [n:0] flip_flop;

 // 50.000.000 em binario = 10111110101111000010000000
 wire [n:0] incremento = flip_flop[n] ? (1'b1):(1- 26'b10111110101111000010000000);
 wire [n:0] dN = flip_flop + incremento;

 always @( posedge clk_alta_f )
 begin
  flip_flop = dN;
 end
 output wire clk_baixa_f = ~flip_flop[n];
 // clock de saida ira mudar a cada 50M de mudancas do clock interno
endmodule
