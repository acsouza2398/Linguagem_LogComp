import sys
import re

#O sintático/parser está sempre olhando para o próximo token, e o léxico está sempre olhando para o token atual
#O tokenizer sempre começa no primeiro token, e o parser sempre começa no segundo token

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890.'
reserved = ["CUPS", "TBSP", "TSP", "OUNCES", "GRAMS", "KILOGRAMS", "MILLILITERS", "LITERS", "CELSIUS", "FAHRENHEIT", "SECONDS", "MINUTES", "HOURS", "COLD", "FROZEN", "ROOM_TEMP", "WARM", "HOT", "MELTED", "TINY", "SMALL", "MEDIUM", "BIG", "LARGE", "POUR", "ADD", "SHAPE", "STRAIN", "COOL", "HEAT", "FOLD", "MIX_IN", "BEAT", "CHOP", "CUT", "JULIENNE", "CUBE", "COARSE_CHOP", "FINELY_CUT", "DICE", "MINCE", "BAKE", "COOK", "CRUSH", "DECORATE_WITH", "SPOON", "KNIFE", "FORK", "RICER", "MIXER", "BLENDER", "SHEET", "RACK", "PLATE", "PAN", "POT", "SKILLET", "COLLANDER", "BOWL", "RAMEKIN", "FRIDGE", "OVEN", "STOVE", "COUNTER", "MICROWAVE", "NEED", "IN", "FOR", "MAKE", "WITH", "BATCHES", "ENJOY", "BEGIN", "END", "DO", "IF", "THEN", "AND", "UNTIL", "TO", "REPEAT", "FINISHED"] 

measurement = ["CUPS", "TBSP", "TSP", "OUNCES", "GRAMS", "KILOGRAMS", "MILLILITERS", "LITERS", "UNIT"]

time_temp = ["CELSIUS", "FAHRENHEIT", "SECONDS", "MINUTES", "HOURS"]

status = ["COLD", "FROZEN", "ROOM_TEMP", "WARM", "HOT", "MELTED", "TINY", "SMALL", "MEDIUM", "BIG", "LARGE","POUR", "ADD", "SHAPE", "STRAIN", "COOL", "HEAT", "FOLD", "MIX_IN", "BEAT", "CHOP", "CUT", "JULIENNE", "CUBE", "COARSE_CHOP", "FINELY_CUT", "DICE", "MINCE", "BAKE", "COOK", "CRUSH", "DECORATE_WITH", "SPOON", "KNIFE", "FORK", "RICER", "MIXER", "BLENDER", "SHEET", "RACK", "PLATE", "PAN", "POT", "SKILLET", "COLLANDER", "BOWL", "RAMEKIN", "FRIDGE", "OVEN", "STOVE", "COUNTER", "MICROWAVE"]

action = ["IN", "FOR", "UNTIL", "TO", "ADD"]

declare = ["NEED", "IF", "FOR", "MAKE", "WITH", "DO", "START"]

end = ["ENJOY", "REPEAT", "FINISHED", "SERVE"]


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None

    def selectNext(self):
        if self.position < len(self.source):
            if self.source[self.position].isdigit():
                i = self.position
                a = ''
                while i < len(self.source) and self.source[i].isdigit():
                    a += self.source[i]
                    i += 1
                    if i < len(self.source) and self.source[i] == '.':
                        a += self.source[i]
                        i += 1
                self.position = i
                self.next = Token('NUMBER', a)
            elif self.source[self.position] in alpha:
                i = self.position
                a = ''
                while i < len(self.source) and self.source[i] in alpha:
                    a += self.source[i]
                    i += 1
                self.position = i
                self.next = Token('WORD', a)
            elif self.source[self.position] == '\n':
                self.next = Token('NEWLINE', self.source[self.position])
                self.position += 1
            elif self.source[self.position] == ':':
                self.next = Token('COLON', self.source[self.position] + self.source[self.position+1])
                self.position += 1
            elif self.source[self.position] == ',':
                self.next = Token('COMMA', self.source[self.position])
                self.position += 1
            elif self.source[self.position] != ' ':
                raise Exception("Símbolo inválido")
            elif self.source[self.position] == ' ':
                self.next = Token('SPACE', ' ')
                self.position += 1
        elif len(self.source) == 0:
            raise Exception("Entrada vazia")
        else:
            self.next = Token('EOF', '')
        #print(self.next.type, self.next.value)

    def peek(self):
        p = self.position
        n = self.next
        self.selectNext()
        r = self.next
        self.position = p
        self.next = n
        return r

class Parser:
    @staticmethod
    def parseTerm(tokenizer):
        a = Parser.parseFactor(tokenizer)
        return a
        
    @staticmethod
    def parseExpression(tokenizer):
        a = Parser.parseTerm(tokenizer)
        return a
    
    @staticmethod
    def parseRelExpression(tokenizer):
        a = Parser.parseExpression(tokenizer)
        return a
    
    @staticmethod
    def parseFactor(tokenizer):
        if tokenizer.next.type == "NUMBER":
            n = IntVal(tokenizer.next.value)
            tokenizer.selectNext()
            return n
        elif tokenizer.next.type == "WORD":
            str = StrVal(tokenizer.next.value)
            tokenizer.selectNext()
            return str
        else:
            raise Exception("Símbolo inválido")
        
    @staticmethod
    def parseBlock(tokenizer):
        children = []
        while tokenizer.next.type != "EOF":
            children.append(Parser.parseStatement(tokenizer))
            if tokenizer.next.value == "REPEAT" or tokenizer.next.value == "ENJOY" or tokenizer.next.value == "FINISHED" or tokenizer.next.type == "EOF" or tokenizer.next.type == "SERVE":
                break
            tokenizer.selectNext()
        return BlockOp(children)

    @staticmethod
    def parseStatement(tokenizer):
        if tokenizer.next.type == "WORD":
            if tokenizer.next.value in declare:
                if tokenizer.next.value == "WITH":
                    tokenizer.selectNext()
                    if tokenizer.next.type == "COLON":
                        tokenizer.selectNext()
                        if tokenizer.next.type == "NEWLINE":
                            tokenizer.selectNext()
                            c = []
                            while tokenizer.next.value == "NEED":
                                tokenizer.selectNext()
                                tokenizer.selectNext()
                                i = Parser.parseRelExpression(tokenizer)
                                tokenizer.selectNext()
                                a = Parser.parseRelExpression(tokenizer)
                                tokenizer.selectNext()
                                b = Parser.parseRelExpression(tokenizer)

                                c.append(VarDeclOp("Ingredient",[i, a, b]))
                                if tokenizer.next.type == "NEWLINE" and tokenizer.peek().value == "NEED":
                                    tokenizer.selectNext()
                                elif tokenizer.peek().value == "DO":
                                    pass
                                else:
                                    raise Exception("Símbolo inválido")
                            return IngredientDeclOp(c)
                        else:
                            raise Exception("Símbolo inválido")
                    else:
                        raise Exception("Símbolo inválido")
                elif tokenizer.next.value == "MAKE":
                    tokenizer.selectNext()
                    tokenizer.selectNext()
                    i = IdentifierOp(tokenizer.next.value)
                    tokenizer.selectNext()
                    if tokenizer.next.type == "NEWLINE":
                        tokenizer.selectNext()
                        b = Parser.parseBlock(tokenizer)
                        if tokenizer.next.type == "WORD":
                            if tokenizer.next.value == "ENJOY":
                                tokenizer.selectNext()
                                return FuncDecOp(i, b)
                            else:
                                raise Exception("Símbolo inválido")
                        else:
                            raise Exception("Símbolo inválido")
                elif tokenizer.next.value == "FOR":
                    tokenizer.selectNext()
                    tokenizer.selectNext()
                    n = Parser.parseRelExpression(tokenizer)
                    tokenizer.selectNext()
                    if tokenizer.next.value == "BATCHES":
                        tokenizer.selectNext()
                        if tokenizer.next.type == "COLON":
                            tokenizer.selectNext()
                            if tokenizer.next.type == "NEWLINE":
                                b = Parser.parseBlock(tokenizer)
                                if tokenizer.next.type == "WORD":
                                    if tokenizer.next.value == "REPEAT":
                                        tokenizer.selectNext()
                                        return WhileOp([n, b])
                                    else:
                                        raise Exception("Símbolo inválido")
                                else:
                                    raise Exception("Símbolo inválido")
                            else:
                                raise Exception("Símbolo inválido")
                        else:
                            raise Exception("Símbolo inválido")
                    else:
                        raise Exception("Símbolo inválido")
                elif tokenizer.next.value == "IF":
                    a = []
                    tokenizer.selectNext()
                    tokenizer.selectNext()
                    a.append(Parser.parseRelExpression(tokenizer))
                    tokenizer.selectNext()
                    if tokenizer.next.value in status:
                        a.append(Parser.parseRelExpression(tokenizer))
                        tokenizer.selectNext()
                        if tokenizer.next.value == "THEN":
                            tokenizer.selectNext()
                            tokenizer.selectNext()
                            s = []
                            while tokenizer.next.type == "WORD" or tokenizer.next.type == "NUMBER":
                                s.append(Parser.parseRelExpression(tokenizer))
                                if tokenizer.next.type != "COMMA":
                                    tokenizer.selectNext()
                            if tokenizer.next.type == "COMMA":
                                tokenizer.selectNext()
                                if tokenizer.next.type == "NEWLINE":
                                    b =  ActionDecOp(s)
                                    tokenizer.selectNext()
                                    return IfOp([a, b])
                                else:
                                    raise Exception("Símbolo inválido")
                            else:
                                raise Exception("Símbolo inválido")
                        else:
                            raise Exception("Símbolo inválido")
                    else:
                        raise Exception("Símbolo inválido")
                elif tokenizer.next.value == "DO":
                    tokenizer.selectNext()
                    if tokenizer.next.type == "COLON":
                        tokenizer.selectNext()
                        if tokenizer.next.type == "NEWLINE":
                            tokenizer.selectNext()
                            b = Parser.parseBlock(tokenizer)
                            if tokenizer.next.type == "WORD":
                                if tokenizer.next.value == "FINISHED":
                                    tokenizer.selectNext()
                                    return StepsDecOp(b)
                                else:
                                    raise Exception("Símbolo inválido")
                        else:
                            raise Exception("Símbolo inválido")
                    else:
                        raise Exception("Símbolo inválido")
                elif tokenizer.next.value == "START":
                    tokenizer.selectNext()
                    if tokenizer.next.type == "NEWLINE":
                        tokenizer.selectNext()
                        r = []
                        while tokenizer.next.type == "WORD" and tokenizer.next.value != "SERVE":
                            r.append(FuncCallOp(IdentifierOp(tokenizer.next.value)))
                            tokenizer.selectNext()
                            if tokenizer.next.type == "COMMA":
                                tokenizer.selectNext()
                                if tokenizer.next.type == "NEWLINE":
                                    tokenizer.selectNext()
                                else:
                                    raise Exception("Símbolo inválido")
                            else:
                                raise Exception("Símbolo inválido")
                        if tokenizer.next.value == "SERVE":
                            return MealOp(r)
                        else:
                            raise Exception("Símbolo inválido")
                    else:
                        raise Exception("Símbolo inválido")
            elif tokenizer.next.value in end:
                return NoOp()
            else:
                s = []
                while tokenizer.next.type == "WORD" or tokenizer.next.type == "NUMBER":
                    s.append(Parser.parseRelExpression(tokenizer))
                    if tokenizer.next.type != "COMMA":
                        tokenizer.selectNext()
                if tokenizer.next.type == "COMMA":
                    tokenizer.selectNext()
                    if tokenizer.next.type == "NEWLINE":
                        return ActionDecOp(s)
                    else:
                        raise Exception("Símbolo inválido")
                else:
                    raise Exception("Símbolo inválido")
        elif tokenizer.next.type == "NEWLINE" or tokenizer.next.type == "SPACE":
            return NoOp()
        else:
            raise Exception("Símbolo inválido")

    @staticmethod
    def run(code):
        c = PrePro.filter(code)
        tokenizer = Tokenizer(c)
        tokenizer.selectNext()
        a = Parser.parseBlock(tokenizer)
        if tokenizer.next.type == "EOF":
            return a
        else:
            raise Exception("Fim de arquivo inválido")

class PrePro:
    @staticmethod
    def filter(code):
        c = re.sub(r'#.*\n', '', code).replace("\s", "")
        #c = re.sub(r'#.*$', '', code).replace("\n", "").replace("\s", "")
        return code
    
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
    
    def evaluate(self, symbol_table):
        pass

        
class IntVal(Node):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, symbol_table):
        return ["Number", self.value]
    
class StrVal(Node):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, symbol_table):
        return ["String", str(self.value)]
    
class NoOp(Node):
    def __init__(self):
        self.value = None
        self.children = None
    
    def evaluate(self, symbol_table):
        pass

class AssignOp(Node):
    def __init__(self, children):
        self.value = None
        self.children = children
    
    def evaluate(self, symbol_table):
        symbol_table.setter(self.children, self.children[1].evaluate(symbol_table))

class BlockOp(Node):
    def __init__(self, children):
        self.children = children
    
    def evaluate(self, symbol_table):
        for child in self.children:
            if child is not None:
                child.evaluate(symbol_table)

class IdentifierOp(Node):
    def __init__(self, value):
        self.value = value
    
    def evaluate(self, symbol_table):
        return symbol_table.getter(self.value)

class WhileOp(Node):
    def __init__(self, children):
        self.children = children
        self.value = None
    
    def evaluate(self, symbol_table):
        print("   Repeat " + str(self.children[0].evaluate(symbol_table)[1]) + " times:")
        self.children[1].evaluate(symbol_table)
        print("   End repeat")

class IfOp(Node):
    def __init__(self, children):
        self.children = children
        self.value = None
    
    def evaluate(self, symbol_table):
        print("   If " + str(self.children[0][0].evaluate(symbol_table)[1]) + " " + str(self.children[0][1].evaluate(symbol_table)[1]) + ":")
        self.children[1].evaluate(symbol_table)
        print("   End if")

class VarDeclOp(Node):
    def __init__(self, value, children):
        self.children = children
        self.value = value
    
    def evaluate(self, symbol_table):
        a = []
        for i in self.children:
            a.append(i.evaluate(symbol_table))
        symbol_table.setter(a[0][1], [a[1][1], a[2][1]])
                
class IngredientDeclOp(Node):
    def __init__(self, children):
        self.children = children
        self.value = None
    
    def evaluate(self, symbol_table):
        print(" Separating Ingredients")
        for i in self.children:
            i.evaluate(symbol_table)
            print("   Get " + i.value + ": " + i.children[0].value + " with amount: " + i.children[1].value + " " + i.children[2].value)
        print(" Ingredients Separated \n")


class StepsDecOp(Node):
    def __init__(self, children):
        self.children = children
        self.value = None
    
    def evaluate(self, symbol_table):
        print(" Steps to follow")
        self.children.evaluate(symbol_table)
        print(" Steps Done \n")

class ActionDecOp(Node):
    def __init__(self, children):
        self.children = children
        self.value = None
    
    def evaluate(self, symbol_table):
        a = "   "
        for i in self.children:
            i.evaluate(symbol_table)
            a += i.value + " "
        print(a)
            
class MealOp(Node):
    def __init__(self, children):
        self.children = children
        self.value = None
    
    def evaluate(self, symbol_table):
        print("\nMeal to be prepared with " + str(len(self.children)) + " recipes:")
        for i in self.children:
            print("\nRecipe to be followed: " + i.value.value)
            i.evaluate(symbol_table)	
            print("Recipe " + i.value.value + " finished \n\n")
        print("Meal Done")
        print("Enjoy your meal!")

class FuncDecOp(Node):
    def __init__(self, value, children):
        self.children = children
        self.value = value
    
    def evaluate(self, symbol_table):
        print("Recipe " + self.value.value + " written down")
        FuncTable.create(self.value.value, self)

class FuncCallOp(Node):
    def __init__(self, value):
        self.children = None
        self.value = value
    
    def evaluate(self, symbol_table):
        args = []
        new_func = FuncTable.getter(self.value.value)
        new_table = SymbolTable()

        #print(new_func.children, " FuncCallOp")

        return new_func.children.evaluate(new_table)

class SymbolTable:
    def __init__(self):
        self.table = {}
    
    def setter(self, name, value):
        self.table[name] = value
    
    def getter(self, name):
        return self.table[name]
    
    def create(self, name, value):
        if name in self.table:
            raise Exception("Variável já declarada")
        self.table[name] = value

class FuncTable:
    table = {}
    
    def getter(name):
        return FuncTable.table[name]
    
    def create(name, value):
        FuncTable.table[name] = value

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    #code = read_file(sys.argv[1])
    code = read_file("exemplo_receita.txt")
    symbol_table = SymbolTable()
    c = Parser.run(code)
    c.evaluate(symbol_table)

main()