from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('MAKE', r'MAKE')
        self.lexer.add('ENJOY', r'ENJOY')
        self.lexer.add('WITH', r'WITH')
        self.lexer.add('DO', r'DO')
        self.lexer.add('IF', r'IF')
        self.lexer.add('THEN', r'THEN')
        self.lexer.add('FOR', r'FOR')
        self.lexer.add('BATCHES', r'BATCHES')
        self.lexer.add('NEED', r'NEED')
        self.lexer.add('REPEAT', r'REPEAT')
        self.lexer.add('FINISHED', r'FINISHED')
        self.lexer.add('START', r'START')
        self.lexer.add('SERVE', r'SERVE')
        self.lexer.add('UNIT', r'CUPS|TBSP|TSP|OUNCES|UNIT|GRAMS|KILOGRAMS|MILLILITERS|LITERS|FAHRENHEIT|CELSIUS|SECONDS|MINUTES|HOURS|SECOND|MINUTE|HOUR')
        self.lexer.add('STATUS', r'COLD|FROZEN|ROOM_TEMP|WARM|HOT|MELTED|TINY|SMALL|MEDIUM|BIG|LARGE|POUR|ADD|SHAPE|STRAIN|COOL|HEAT|FOLD|MIX_IN|BEAT|CHOP|CUT|JULIENNE|CUBE|COARSE_CHOP|FINELY_CUT|DICE|MINCE|BAKE|COOK|CRUSH|DECORATE_WITH|MIX|SPOON|KNIFE|FORK|RICER|MIXER|BLENDER|SHEET|RACK|PLATE|PAN|POT|SKILLET|COLLANDER|BOWL|RAMEKIN|FRIDGE|OVEN|STOVE|COUNTER|MICROWAVE|AND|UNTIL|IN|TO')
        self.lexer.add('STRING', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.add('NEWLINE', r'\n')
        self.lexer.add('FLOAT', r'\d+[.]\d+')
        self.lexer.add('INT', r'\d+')
        self.lexer.add('COLON', r':')
        self.lexer.add('INDENT', r'\t')
        self.lexer.add('COMMA', r',')
        self.lexer.ignore(r'[ \t]+')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()