from cminus_lexer import main as lexer
from cminus_parser import main as parser


if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'examples/gcd.c'

	lexer(fin)
    parser(fin)