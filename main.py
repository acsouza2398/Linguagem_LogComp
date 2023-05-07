from langLexer import Lexer
from langParser import Parser

text_input = """MAKE mini_cheesecake_for_two: WITH: NEED grahamCrackers 0.25 CUPS NEED butter 1 TBSP NEED sugar 2 TBSP NEED creamCheese 128 GRAMS NEED eggYolk 1 NEED vanillaExtract 0.25 TSP NEED strawberry 100 GRAMS DO: HEAT OVEN TO 180 CELSIUS IN MICROWAVE, HEAT butter UNTIL MELTED, CRUSH grahamCrackers IN SMALL BOWL, MIX grahamCrackers AND butter, FOR 2 BATCHES: ADD TO SMALL RAMEKIN, IF creamCheese COLD THEN HEAT IN MICROWAVE FOR 30 SECONDS, IN LARGE BOWL BEAT creamCheese AND sugar FOR 1.5 MINUTES, MIX_IN eggYolk FOR 1 MINUTE, ADD vanillaExtract, FOR 2 BATCHES: IN SMALL RAMEKIN POUR, IN OVEN BAKE FOR 20 MINUTES, IN FRIDGE COOL FOR 2 HOURS, CHOP strawberry, FOR 2 BATCHES: ADD strawberry TO SMALL RAMEKIN, ENJOY!"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)

""" for token in tokens:
    print(token) """