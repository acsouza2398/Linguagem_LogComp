from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(['BEGIN', 'END', 'WITH', 'DO', 'IF', 'THEN', 'FOR', 'BATCHES', 'AND', 'UNTIL', 'IN', 'TO', 'NEED', 'IMPERAL_TYPE', 'METRIC_TYPE', 'TEMPERATURE_TYPE', 'TIME_TYPE', 'STATUS_TYPE', 'STATUS_SIZE', 'STATUS_ACTION', 'STATUS_UTENSIL', 'STATUS_PLACE', 'STRING', 'NEWLINE', 'FLOAT', 'INT', 'COLON', 'COMMA'])

    def parse(self):
        @self.pg.production('program : BEGIN STRING COLON recipe END')
        def program(p):
            print(p)
            print("Program parsed")
            return p
        
        @self.pg.production('recipe : WITH COLON ingredients DO COLON steps')
        @self.pg.production('recipe : WITH COLON ingredients')
        def recipe(p):
            print(p)
            print("Recipe parsed --------------------")
            return p
        
        
        @self.pg.production('ingredients : ingredient ingredients')
        @self.pg.production('ingredients : ingredient')
        @self.pg.production('ingredients : ')
        def ingredients(p):
            print("All Ingredients parsed --------------------")
            print(p)
            return p
        
        @self.pg.production('ingredient : NEED STRING FLOAT IMPERAL_TYPE')
        @self.pg.production('ingredient : NEED STRING FLOAT METRIC_TYPE')
        @self.pg.production('ingredient : NEED STRING INT IMPERAL_TYPE')
        @self.pg.production('ingredient : NEED STRING INT METRIC_TYPE')
        @self.pg.production('ingredient : NEED STRING INT')
        @self.pg.production('ingredient : NEED STRING FLOAT')
        @self.pg.production('ingredient : ')
        def ingredient(p):
            print("Ingredient parsed")
            print(p)
            return p
        
        @self.pg.production('steps : step steps')
        @self.pg.production('steps : step')
        @self.pg.production('steps : ')
        def steps(p):
            print("All Steps parsed --------------------")
            print(p)
            return p
        
        @self.pg.production('step : IF status THEN status COMMA steps')
        @self.pg.production('step : status COMMA steps')
        @self.pg.production('step : FOR INT BATCHES COLON steps')
        @self.pg.production('step : ')
        def step(p):
            print("Step parsed -------------------- // --------------------")
            print(p)
            return p
        
        @self.pg.production('status : STATUS_TYPE status')
        @self.pg.production('status : STATUS_SIZE status')
        @self.pg.production('status : STATUS_ACTION status')
        @self.pg.production('status : STATUS_UTENSIL status')
        @self.pg.production('status : STATUS_PLACE status')
        @self.pg.production('status : STRING status')
        @self.pg.production('status : STATUS_TYPE')
        @self.pg.production('status : STATUS_SIZE')
        @self.pg.production('status : STATUS_ACTION')
        @self.pg.production('status : STATUS_UTENSIL')
        @self.pg.production('status : STATUS_PLACE')
        @self.pg.production('status : STRING')
        @self.pg.production('status : operator')
        @self.pg.production('status : timetemp')
        @self.pg.production('status : ')
        def status(p):
            print("Status parsed")
            print(p)
            return p
        
        @self.pg.production('operator : AND status')
        @self.pg.production('operator : IN status')
        @self.pg.production('operator : WITH status')
        @self.pg.production('operator : UNTIL status')
        @self.pg.production('operator : TO status')
        @self.pg.production('operator : ')
        def operator(p):
            print("Operator parsed")
            print(p)
            return p
        
        @self.pg.production('timetemp : FOR FLOAT TIME_TYPE status')
        @self.pg.production('timetemp : FOR INT TIME_TYPE status')
        @self.pg.production('timetemp : TO FLOAT TIME_TYPE status')
        @self.pg.production('timetemp : TO INT TIME_TYPE status')
        @self.pg.production('timetemp : UNTIL FLOAT TIME_TYPE status')
        @self.pg.production('timetemp : UNTIL INT TIME_TYPE status')
        @self.pg.production('timetemp : FOR FLOAT TEMPERATURE_TYPE status')
        @self.pg.production('timetemp : FOR INT TEMPERATURE_TYPE status')
        @self.pg.production('timetemp : UNTIL FLOAT TEMPERATURE_TYPE status')
        @self.pg.production('timetemp : UNTIL INT TEMPERATURE_TYPE status')
        @self.pg.production('timetemp : TO FLOAT TEMPERATURE_TYPE status')
        @self.pg.production('timetemp : TO INT TEMPERATURE_TYPE status')
        @self.pg.production('timetemp : ')
        def timetemp(p):
            print("Timetemp parsed")
            print(p)
            return p

        
        @self.pg.error
        def error_handle(token):
            print("Ran into a %s where it wasn't expected" % token.gettokentype())
            raise ValueError(token)
        
    def get_parser(self):
        return self.pg.build()
        
