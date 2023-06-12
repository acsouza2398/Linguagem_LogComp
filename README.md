# Linguagem_LogComp

## Contexto
A linguagem proposta modela receitas culinárias com loops, condicionais, declaração de variáveis e funções. A análise Léxica e Sintática foi feita usando RPly.
Cada receita é considerada uma função e um programa principal é o cardápio a ser servido. Cada cardápio precisa conter no mínimo uma receita, mas quantas quiser. O output esperado são instruções de preparo do cardápio para uma máquina imaginária de culinária que executaria a refeição planejada na ordem desejada, desde a separação dos ingredientes até o preparo da receita.

## EBNF
 ```
 LETTER = ("a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" |
            "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z" |
             "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J' | "K" | "L" | "M" | "N" | "O" | "P" 
             | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" )

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 )

IMPERIAL_TYPE = ("CUPS", "TBSP", "TSP", "OUNCES", "UNIT")

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

CONDITIONAL_DECLARATION = "IF", STRING, (STATUS_TEMP | STATUS_SIZE), "THEN" ((STATUS_ACTION, ("IN" | "ON"), STATUS_PLACE, ("FOR"| "UNTIL"), ((INT | FLOAT), TIME_TYPE) | STATUS_TEMP)) | (STATUS_ACTION, "WITH", STATUS_UTENSIL)

STEP_DECLARATION = ["IN", [STATUS_SIZE], (STATUS_UTENSIL | STATUS_PLACE)], STATUS_ACTION, [{(STRING | STATUS_PLACE), "AND"}], [("UNTIL" | "FOR" | "TO"), (((INT | FLOAT), (TIME_TYPE | TEMPERATURE_TYPE)) | (STATUS_TEMP | ([STATUS_SIZE], STATUS_UTENSIL))), COMMA, "\n"]

BATCH_DECLARATION = "FOR", INT, "BATCHES:", "\n", {STEP_DECLARATION}, "\n", "REPEAT" 

RECIPE_DECLARATION = "MAKE", STRING, "\n", "WITH:", "\n", {INGREDIENT_DECLARATION}, "\n", "DO:", "\n", {BATCH_DECLARATION | STEP_DECLARATION | CONDITIONAL_DECLARATION}, "FINISHED", "\n", "ENJOY"

MEAL_DECLARATION = "START", {STRING, "COMMA"}, "SERVE!"  
 ```
 
 ## Exemplo de Código
 ```
MAKE cheesecake_for_two
WITH:
NEED grahamCrackers 0.25 CUPS
NEED butter 1 TBSP
NEED sugar 2 TBSP
NEED creamCheese 128 GRAMS
NEED eggYolk 1 UNIT
NEED vanillaExtract 0.25 TSP
NEED strawberry 100 GRAMS
DO:
HEAT OVEN TO 180 CELSIUS,
IN MICROWAVE HEAT butter UNTIL MELTED,
CRUSH grahamCrackers,
IN SMALL BOWL MIX grahamCrackers AND butter,
FOR 2 BATCHES:
ADD TO SMALL RAMEKIN,
REPEAT
IF creamCheese COLD THEN HEAT IN MICROWAVE FOR 30 SECONDS,
IN LARGE BOWL BEAT creamCheese AND sugar FOR 1.5 MINUTES,
MIX_IN eggYolk FOR 1 MINUTE,
ADD vanillaExtract,
FOR 2 BATCHES:
IN SMALL RAMEKIN POUR,
REPEAT
IN OVEN BAKE FOR 20 MINUTES,
IN FRIDGE COOL FOR 2 HOURS,
CHOP strawberry,
FOR 2 BATCHES:
ADD strawberry TO SMALL RAMEKIN,
REPEAT
FINISHED
ENJOY

MAKE whipped_cream
WITH:
NEED heavyCream 1 CUPS
NEED sugar 2 TBSP
NEED vanillaExtract 0.5 TSP
DO:
IN LARGE BOWL ADD heavyCream AND sugar AND vanillaExtract,
WHIP heavyCream FOR 4 MINUTES,
IN FRIDGE COOL FOR 24 HOURS,
FINISHED
ENJOY

START
cheesecake_for_two,
whipped_cream,
SERVE
 ```
 ## Exemplo de Output
 ```
Recipe cheesecake_for_two written down
Recipe whipped_cream written down

Meal to be prepared with 2 recipes:

Recipe to be followed: cheesecake_for_two
 Separating Ingredients
   Get Ingredient: grahamCrackers with amount: 0.25 CUPS
   Get Ingredient: butter with amount: 1 TBSP
   Get Ingredient: sugar with amount: 2 TBSP
   Get Ingredient: creamCheese with amount: 128 GRAMS
   Get Ingredient: eggYolk with amount: 1 UNIT
   Get Ingredient: vanillaExtract with amount: 0.25 TSP
   Get Ingredient: strawberry with amount: 100 GRAMS
 Ingredients Separated 

 Steps to follow
   HEAT OVEN TO 180 CELSIUS 
   IN MICROWAVE HEAT butter UNTIL MELTED 
   CRUSH grahamCrackers 
   IN SMALL BOWL MIX grahamCrackers AND butter 
   Repeat 2 times:
   ADD TO SMALL RAMEKIN 
   End repeat
   If creamCheese COLD:
   HEAT IN MICROWAVE FOR 30 SECONDS 
   End if
   LARGE BOWL BEAT creamCheese AND sugar FOR 1.5 MINUTES 
   MIX_IN eggYolk FOR 1 MINUTE 
   ADD vanillaExtract 
   Repeat 2 times:
   IN SMALL RAMEKIN POUR 
   End repeat
   IN OVEN BAKE FOR 20 MINUTES 
   IN FRIDGE COOL FOR 2 HOURS 
   CHOP strawberry 
   Repeat 2 times:
   ADD strawberry TO SMALL RAMEKIN 
   End repeat
 Steps Done 

Recipe cheesecake_for_two finished 


Recipe to be followed: whipped_cream
 Separating Ingredients
   Get Ingredient: heavyCream with amount: 1 CUPS
   Get Ingredient: sugar with amount: 2 TBSP
   Get Ingredient: vanillaExtract with amount: 0.5 TSP
 Ingredients Separated 

 Steps to follow
   IN LARGE BOWL ADD heavyCream AND sugar AND vanillaExtract 
   WHIP heavyCream FOR 4 MINUTES 
   IN FRIDGE COOL FOR 24 HOURS 
 Steps Done 

Recipe whipped_cream finished 


Meal Done
Enjoy your meal!

 ```
