import re

from . import c_ast
from .c_lexer import CLexer
from .plyparser import PLYParser, Coord, ParseError, parameterized, template
from .ast_transforms import fix_switch_cases


@template
class CParser(PLYParser):
    