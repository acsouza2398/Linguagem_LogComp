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

UNIT = ("CUPS", "TBSP", "TSP", "OUNCES", "UNIT", "GRAMS", "KILOGRAMS", "MILLILITERS", "LITERS", "CELSIUS", "FAHRENHEIT", "SECONDS", "MINUTES", "HOURS")

STATUS = ("COLD", "FROZEN", "ROOM_TEMP", "WARM", "HOT", "MELTED", "TINY", "SMALL", "MEDIUM", "BIG", "LARGE", "POUR", "ADD", "SHAPE", "STRAIN", "COOL", "HEAT", "FOLD", "MIX_IN", "BEAT", "CHOP", "CUT", "JULIENNE", "CUBE", "COARSE_CHOP", "FINELY_CUT", "DICE", "MINCE", "BAKE", "COOK", "CRUSH", "DECORATE_WITH", "SPOON", "KNIFE", "FORK", "RICER", "MIXER", "BLENDER", "SHEET", "RACK", "PLATE", "PAN", "POT", "SKILLET", "COLLANDER", "BOWL", "RAMEKIN", "FRIDGE", "OVEN", "STOVE", "COUNTER", "MICROWAVE")

IDENTIFIER = {LETTER}

NUMBER = {DIGIT}, [".", {DIGIT}]

STRUCTURE = {RECIPE_DECLARATION}, MEAL_DECLARATION

MEAL_DECLARATION = "START", "\n", {IDENTIFIER, ",", \n"}, "SERVE"

RECIPE_DECLARATION = "MAKE", IDENTIFIER, "\n", INGREDIENT_DECLARATION, STEP_DECLARATION, "\n", "ENJOY", "\n"

INGREDIENT_DECLARATION = "WITH", ":", {"NEED", IDENTIFIER, NUMBER, UNIT, "\n"}

STEP_DECLARATION = "DO", ":", {(ACTION_DECLARATION, "\n") | (LOOP_DECLARATION, "\n") | (IF_DECLARATION, "\n")}, "FINISHED", "\n"

LOOP_DECLARATION = "FOR", NUMBER, "BATCHES", ":", "\n", {ACTION_DECLARATION, "\n"}, "REPEAT"

IF_DECLARATION = "IF", IDENTIFIER, STATUS, "THEN", ACTION_DECLARATION, "\n"

ACTION_DECLARATION = {STATUS, IDENTIFIER, NUMBER, UNIT}, ",", "\n" 
 ```

## Diagrama do EBNF

![Diagrama EBNF](EBNF_Receitas.svg)
 
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
