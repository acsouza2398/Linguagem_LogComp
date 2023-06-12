from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('BEGIN', r'MAKE')
        self.lexer.add('END', r'ENJOY!')
        self.lexer.add('WITH', r'WITH')
        self.lexer.add('DO', r'DO')
        self.lexer.add('IF', r'IF')
        self.lexer.add('THEN', r'THEN')
        self.lexer.add('FOR', r'FOR')
        self.lexer.add('BATCHES', r'BATCHES')
        self.lexer.add('AND', r'AND')
        self.lexer.add('UNTIL', r'UNTIL')
        self.lexer.add('IN', r'IN')
        self.lexer.add('TO', r'TO')
        self.lexer.add('NEED', r'NEED')
        self.lexer.add('IMPERAL_TYPE', r'CUPS|TBSP|TSP|OUNCES|UNIT')
        self.lexer.add('METRIC_TYPE', r'GRAMS|KILOGRAMS|MILLILITERS|LITERS')
        self.lexer.add('TEMPERATURE_TYPE', r'FAHRENHEIT|CELSIUS')
        self.lexer.add('TIME_TYPE', r'SECONDS|MINUTES|HOURS|SECOND|MINUTE|HOUR')
        self.lexer.add('STATUS_TYPE', r'COLD|FROZEN|ROOM_TEMP|WARM|HOT|MELTED')
        self.lexer.add('STATUS_SIZE', r'TINY|SMALL|MEDIUM|BIG|LARGE')
        self.lexer.add('STATUS_ACTION', r'POUR|ADD|SHAPE|STRAIN|COOL|HEAT|FOLD|MIX_IN|BEAT|CHOP|CUT|JULIENNE|CUBE|COARSE_CHOP|FINELY_CUT|DICE|MINCE|BAKE|COOK|CRUSH|DECORATE_WITH|MIX')
        self.lexer.add('STATUS_UTENSIL', r'SPOON|KNIFE|FORK|RICER|MIXER|BLENDER|SHEET|RACK|PLATE|PAN|POT|SKILLET|COLLANDER|BOWL|RAMEKIN')
        self.lexer.add('STATUS_PLACE', r'FRIDGE|OVEN|STOVE|COUNTER|MICROWAVE')
        self.lexer.add('STRING', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer.add('NEWLINE', r'\n')
        self.lexer.add('FLOAT', r'\d+[.]\d+')
        self.lexer.add('INT', r'\d+')
        self.lexer.add('COLON', r':')
        self.lexer.add('INDENT', r'\t')
        self.lexer.add('COMMA', r',')
        self.lexer.add('REPEAT', r'REPEAT')
        self.lexer.add('FINISHED', r'FINISHED')
        self.lexer.ignore(r'[ \t]+')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()