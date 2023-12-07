import UItext as UI
from example import Example
import texts

language = "cz"
run = ""
numexamples = 0
numcount = 0
operators = []
interval = []
decimal = 0
examples_temp = []
examples_gen = []
results_gen = []



def write_2_files_txt(examples: list, results: list, language: str) -> None:
    """
    Writes two files. One with examples and second with results.
    """ 
    with open(texts.file_examples[language], 'w') as file:
        file.writelines('\n'.join(examples))
    with open(texts.file_results[language], 'w') as file:
        file.writelines('\n'.join(results))
    UI.tw_print(texts.two_txt_saved[language]+texts.file_examples[language]\
+texts.and_text[language]+texts.file_results[language],len(UI.LINE))
    

while not run == "E":
# shows starting menu, time for language change
    UI.start_menu(language)
    option = input()
    if option == "E":
        UI.end_premature(language)
    if option in UI.help_options: 
        UI.help_operator(option,language)
        input()
        continue
    elif option == "L":
        language = UI.language_change(language)
    else:
        print(UI.LINE)
        break

# gets parametres and number of future examples
numexamples = UI.get_num_of_examples(language)
numcount = UI.get_numcount(language)
operators = UI.get_operators(language)
interval = UI.get_interval(language)
decimal = UI.get_decimal(language)

# i don't know how to do it in texts.py now
UI.clrscr()
print(UI.LINE)
if language == "cz":
    UI.tw_print(f"Počet příkladů: {numexamples}, počet operandů: {numcount}, \
operátory: {operators}, interval = <{interval[0]},{interval[1]}>, \
počet desetiných míst: {decimal}",len(UI.LINE))
if language == "en":
    UI.tw_print(f"Number of examples: {numexamples}, number of operands: \
{numcount}, operators: {operators}, interval = <{interval[0]},{interval[1]}>,\
 number of decimals: {decimal}",len(UI.LINE))
    
# generates list of examples according to obtain parametres
for i in range(numexamples):
    example = Example(numcount,operators,interval,decimal)
    examples_temp.append(example)
    examples_gen.append(str(example))
    results_gen.append(str(example.solve_it()))

write_2_files_txt(examples_gen,results_gen,language)
