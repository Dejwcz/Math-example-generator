import texts
from os import system, name

LINE = 70*"="
language = "cz"
help_options = ["+?", "-?", "*?", "/?"]


def clrscr():
    if name == "nt":system("cls")
    else: system("clear")

def end_premature(language):
    print(LINE)
    tw_print(texts.end_prem[language],len(LINE))
    print(LINE)
    exit(2)

def tw_print(text: str, lenght: int, center=True ) -> None:
    """
    function for text wrapping depending on defined lenght
    and in default set center it. You can choose 
    to not center text.(ignores words lenght)
    """
    split_text = []
    x = 0
    while x < len(text):
        split_text.append(text[x:x+lenght])
        x = x + lenght
    split = ""
    for split in split_text:
        if center:print(str(split).center(lenght))
        else: print(str(split))

def help_operator(option,language):
    print(LINE)
    if option == "+?":tw_print(texts.help_add[language],len(LINE))
    elif option == "-?":tw_print(texts.help_sub[language],len(LINE))
    elif option == "*?":tw_print(texts.help_mul[language],len(LINE))
    elif option == "/?":tw_print(texts.help_div[language],len(LINE))
    print(LINE)
    
def language_change(language):
    option = ""
    print(LINE)
    print(texts.lng_choice[language])
    for choice in texts.language_list.values():
        print(choice)
    option = input()    
    while option not in texts.language_list.keys():
        tw_print(texts.bad_choice[language],len(LINE))
        option = input()
    if option == "1": return "cz"
    elif option == "2": return "en"

def start_menu(language):
    clrscr()
    print(LINE)
    print(texts.greetings[language].center(len(LINE)))
    print(LINE)
    print()
    tw_print(texts.info[language],len(LINE))
    print()

def choose_menu(language):
    numcount = ""
    go_next = False
    operators = []
    clrscr()
    print(LINE)
    while not go_next:
        print(texts.problem_number[language])
        numcount = input()
        if numcount == "E":
            end_premature(language)
        try: 
            numcount = int(numcount)
        except ValueError:
            print(texts.wrong_enter[language],end="")
            continue
        if numcount <= 0:
            print(texts.wrong_enter[language],end="")
            continue
        if numcount >= 1000:
            tw_print(texts.are_sure[language],len(LINE))
            print(numcount)
            temp = input()
            if temp == "":
                break
            else: 
                continue
        go_next = True

    print(LINE)            
    print(texts.operator_choice[language])
    operators_in = input()
    if "+" in operators_in: operators.append(" + ")
    if "-" in operators_in: operators.append(" - ")
    if "*" in operators_in: operators.append(" * ")
    if "/" in operators_in: operators.append(" / ")
    if operators == []: print("špatný vstup")
    






