# Linguagem_LogComp

## Contexto
A linguagem proposta modela receitas culinárias com loops, condicionais, declaração de variáveis e funções.

## EBNF
 ```
 LETTER = ("a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" |
            "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" |
             "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J' | "K" | "L" | "M" | "N" | "O" | "P" 
             | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" )

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 )

IMPERIAL_TYPE = ("CUPS", "TBSP", "TSP", "OUNCES")

METRIC_TYPE = ("GRAMS", "KILOGRAMS", "MILLILITERS", "LITERS")

TEMPERATURE_TYPE = ("CELSIUS", "FAHRENHEIT")

TIME_TYPE = ("SECONDS", "MINUTES", "HOURS")

STATUS_TEMP = ("COLD", "FROZEN", "ROOM_TEMP", "WARM", "HOT", "MELTED")

STATUS_SIZE = ("TINY", "SMALL", "MEDIUM", "BIG", "LARGE")

STATUS_ACTION = ("POUR", "ADD", "SHAPE", "STRAIN", "COOL", "HEAT", "FOLD", "MIX_IN", "BEAT", "CHOP", "CUT", "JULIENNE", "CUBE", "COARSE_CHOP", "FINELY_CUT", "DICE", "MINCE", "BAKE", "COOK", "CRUSH", "DECORATE_WITH")

STATUS_UTENSIL = ("SPOON", "KNIFE", "FORK", "RICER", "MIXER", "BLENDER", "SHEET", "RACK", "PLATE", "PAN", "POT", "SKILLET", "COLLANDER", "BOWL", "RAMEKIN")

STATUS_PLACE = ("FRIDGE", "OVEN", "STOVE", "COUNTER", "MICROWAVE")

STRING = {LETTER}

INT = {DIGIT}

FLOAT = {INT}, ".", INT

INGREDIENT_DECLARATION = "NEED", STRING, (INT | FLOAT), [IMPERIAL_TYPE, METRIC_TYPE]

CONDITIONAL_DECLARATION = "IF", STRING, (STATUS_TEMP | STATUS_SIZE), "THEN" ((STATUS_ACTION, ("IN" | "ON"), STATUS_PLACE, ("FOR"| "UNTIL"), ((INT | FLOAT), TIME_TYPE) | STATUS_TEMP)) | (STATUS_ACTION, "WITH", STATUS_UTENSIL))

STEP_DECLARATION = ["IN", [STATUS_SIZE], (STATUS_UTENSIL | STATUS_PLACE)], STATUS_ACTION, [{(STRING | STATUS_PLACE}, "AND"}], [("UNTIL" | "FOR" | "TO"), (((INT | FLOAT), (TIME_TYPE | TEMPERATURE_TYPE)) | (STATUS_TEMP | ([STATUS_SIZE], STATUS_UTENSIL)))]

BATCH_DECLARATION = "FOR", INT, "BATCHES:", "\n"

RECIPE_DECLARATION = "MAKE", STRING, ":", "\n", "WITH:", "\n", {INGREDIENT_DECLARATION}, "\n", "DO:", "\n", {BATCH_DECLARATION | STEP_DECLARATION | CONDITIONAL_DECLARATION}, "\n", "ENJOY!"
 ```
 
 ## Exemplo de Código
 ```
 MAKE mini_cheesecake_for_two:
    WITH:
        NEED grahamCrackers 0.25 CUPS
        NEED butter 1 TBSP
        NEED sugar 2 TBSP
        NEED creamCheese 128 GRAMS
        NEED eggYolk 1
        NEED vanillaExtract 0.25 TSP
        NEED strawberry 100 GRAMS

    DO:
        HEAT OVEN TO 180 CELSIUS
        IN MICROWAVE HEAT butter UNTIL MELTED
        CRUSH grahamCrackers
        IN SMALL BOWL MIX grahamCrackers AND butter
        FOR 2 BATCHES:
            ADD TO SMALL RAMEKIN
        IF creamCheese COLD THEN HEAT IN MICROWAVE FOR 30 SECONDS
        IN LARGE BOWL BEAT creamCheese AND sugar FOR 1.5 MINUTES
        MIX_IN eggYolk FOR 1 MINUTE
        ADD vanillaExtract
        FOR 2 BATCHES:
            IN SMALL RAMEKIN POUR
        IN OVEN BAKE FOR 20 MINUTES
        IN FRIDGE COOL FOR 2 HOURS
        CHOP strawberry
        FOR 2 BATCHES:
            ADD strawberry TO SMALL RAMEKIN
ENJOY!
 ```
