module Output(clock, binary, ones, tens, hundreds, thousands);

  input clock;
  input [31:0] binary;
  output [6:0] ones, tens, hundreds, thousands;
  wire [3:0] binOnes, binTens, binHundreds, binThousands;

  BCD converter(binary, binOnes, binTens, binHundreds, binThousands);

  sevenSegmentsDisplay displayA(clock, binOnes, ones[0], ones[1], ones[2],
  ones[3], ones[4], ones[5], ones[6]);
  sevenSegmentsDisplay displayB(clock, binTens, tens[0], tens[1], tens[2],
  tens[3], tens[4], tens[5], tens[6]);
  sevenSegmentsDisplay displayC(clock, binHundreds, hundreds[0], hundreds[1], hundreds[2],
  hundreds[3], hundreds[4], hundreds[5], hundreds[6]);
  sevenSegmentsDisplay displayD(clock, binThousands, thousands[0], thousands[1], thousands[2],
  thousands[3], thousands[4], thousands[5], thousands[6]);
  
endmodule // Output