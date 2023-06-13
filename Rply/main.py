from langLexer import Lexer
from langParser import Parser

text_input = """MAKE cheesecake_for_two WITH: NEED grahamCrackers 0.25 CUPS NEED butter 1 TBSP NEED sugar 2 TBSP NEED creamCheese 128 GRAMS NEED eggYolk 1 UNIT NEED vanillaExtract 0.25 TSP NEED strawberry 100 GRAMS DO: HEAT OVEN TO 180 CELSIUS, IN MICROWAVE HEAT butter UNTIL MELTED, CRUSH grahamCrackers, IN SMALL BOWL MIX grahamCrackers AND butter, FOR 2 BATCHES: ADD TO SMALL RAMEKIN, REPEAT IF creamCheese COLD THEN HEAT IN MICROWAVE DURING 30 SECONDS, IN LARGE BOWL BEAT creamCheese AND sugar DURING 1.5 MINUTES, MIX_IN eggYolk DURING 1 MINUTE, ADD vanillaExtract, FOR 2 BATCHES: IN SMALL RAMEKIN POUR, REPEAT IN OVEN BAKE DURING 20 MINUTES, IN FRIDGE COOL DURING 2 HOURS, CHOP strawberry, FOR 2 BATCHES: ADD strawberry TO SMALL RAMEKIN, REPEAT FINISHED ENJOY MAKE whipped_cream WITH: NEED heavyCream 1 CUPS NEED sugar 2 TBSP NEED vanillaExtract 0.5 TSP DO: IN LARGE BOWL ADD heavyCream AND sugar AND vanillaExtract, WHIP heavyCream DURING 4 MINUTES, IN FRIDGE COOL DURING 24 HOURS, FINISHED ENJOY START cheesecake_for_two, whipped_cream, SERVE"""

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)

""" for token in tokens:
    print(token) """