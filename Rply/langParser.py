from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(['MAKE', 'ENJOY', 'WITH', 'DO', 'IF', 'THEN', 'FOR', 'BATCHES', 'NEED', 'UNIT', 'STATUS', 'REPEAT', 'FINISHED', 'START', 'SERVE', 'STRING', 'NEWLINE', 'FLOAT', 'INT', 'COLON', 'COMMA'])

    def parse(self):
        @self.pg.production('structure : recipe START meal SERVE')
        def structure(p):
            print(p)
            print("Program parsed")
            return p
        
        @self.pg.production('meal : STRING COMMA meal')
        @self.pg.production('meal : STRING COMMA')
        def meal(p):
            print(p)
            print("Meal parsed")
            return p
        
        @self.pg.production('recipe : MAKE STRING WITH COLON ingredients DO COLON steps ENJOY recipe')
        @self.pg.production('recipe : ')
        def recipe(p):
            print(p)
            print("Recipe parsed --------------------")
            return p
        
        @self.pg.production('ingredients : NEED STRING INT UNIT ingredients')
        @self.pg.production('ingredients : NEED STRING INT UNIT')
        @self.pg.production('ingredients : NEED STRING FLOAT UNIT ingredients')
        @self.pg.production('ingredients : NEED STRING FLOAT UNIT')
        @self.pg.production('ingredients : ')
        def ingredients(p):
            print("All Ingredients parsed --------------------")
            #print(p)
            return p
        
        @self.pg.production('steps : action steps')
        @self.pg.production('steps : action')
        @self.pg.production('steps : loop steps')
        @self.pg.production('steps : loop')
        @self.pg.production('steps : if_ steps')
        @self.pg.production('steps : if_')
        @self.pg.production('steps : FINISHED')
        def steps(p):
            print("All Steps parsed --------------------")
            print(p)
            return p
        
        @self.pg.production('action : STRING COMMA')
        @self.pg.production('action : INT COMMA')
        @self.pg.production('action : FLOAT COMMA')
        @self.pg.production('action : UNIT COMMA')
        @self.pg.production('action : STATUS COMMA')
        @self.pg.production('action : STRING action')
        @self.pg.production('action : INT action')
        @self.pg.production('action : FLOAT action')
        @self.pg.production('action : UNIT action')
        @self.pg.production('action : STATUS action')
        @self.pg.production('action : REPEAT')
        def action(p):
            print("All Actions parsed --------------------")
            print(p)
            return p
        
        @self.pg.production('loop : FOR INT BATCHES COLON action')
        def loop(p):
            print("Loop parsed --------------------")
            print(p)
            return p
        
        @self.pg.production('if_ : IF STRING STATUS THEN action')
        def if_(p):
            print("If parsed --------------------")
            print(p)
            return p
        
        @self.pg.error
        def error_handle(token):
            print("Ran into a %s where it wasn't expected" % token.gettokentype())
            raise ValueError(token)
        
    def get_parser(self):
        return self.pg.build()
        
