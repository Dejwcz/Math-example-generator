import texts
from os import system, name

LINE = 70*"="
language = "cz"
help_options = ["+?", "-?", "*?", "/?"]


def clrscr() -> None:
    """
    Clear screen for all OS.
    """
    if name == "nt":system("cls")
    else: system("clear")

def end_premature(language: str) -> None:
    """
    It says goodbye after ending the program early.
    """
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

def help_operator(option: str,language: str) -> None:
    """
    Shows help for selected operator.
    """
    print(LINE)
    if option == "+?":tw_print(texts.help_add[language],len(LINE))
    elif option == "-?":tw_print(texts.help_sub[language],len(LINE))
    elif option == "*?":tw_print(texts.help_mul[language],len(LINE))
    elif option == "/?":tw_print(texts.help_div[language],len(LINE))
    print(LINE)
    
def language_change(language: str) -> str:
    """
    Menu for language change. Return selected language.
    """
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

def start_menu(language: str) -> None:
    """
    Welcome menu. Shows starting information.
    """
    clrscr()
    print(LINE)
    print(texts.greetings[language].center(len(LINE)))
    print(LINE)
    print()
    tw_print(texts.info[language],len(LINE))
    print()

def choose_menu(language: str) -> None:
    """
    Menu for select parametres to examples.
    """

    numcount = ""
    go_next = False
    operators = []
    interval = [-1000,1000]
    decimal = 0

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

    go_next = False
    print(LINE)
    while not go_next:            
        print(texts.operator_choice[language])
        operators_in = input()
        if operators_in == "E":
           end_premature(language)
        if "+" in operators_in: operators.append(" + ")
        if "-" in operators_in: operators.append(" - ")
        if "*" in operators_in: operators.append(" * ")
        if "/" in operators_in: operators.append(" / ")
        if operators == []:
            print(texts.wrong_enter[language],end="")
            continue
        if operators: go_next = True
    
    go_next = False
    interval_temp = ""
    print(LINE)
    while not go_next:
        tw_print(texts.interval_choice[language],len(LINE))
        
        go_next2 = False
        while not go_next2:
            print(texts.begin_interval[language])
            interval_temp = input()
            if interval_temp == "E":
                end_premature(language)
            if interval_temp == "":
                break
            try: 
                interval_temp = int(interval_temp)
            except ValueError:
                print(texts.wrong_enter[language],end="")
                continue
            interval[0] = interval_temp
            go_next2 = True

        go_next2 = False
        while not go_next2:
            print(texts.end_interval[language])
            interval_temp = input()
            if interval_temp == "E":
                end_premature(language)
            if interval_temp == "":
                break
            try: 
                interval_temp = int(interval_temp)
            except ValueError:
                print(texts.wrong_enter[language],end="")
                continue
            interval[1] = interval_temp
            go_next2 = True
        
        if interval[0] >= interval[1]:
            tw_print(texts.bad_interval[language],len(LINE))
            print(LINE)
            continue
        go_next = True

    go_next = False
    while not go_next:
        tw_print(texts.decimal_coice[language],len(LINE))
        decimal = input()
        if decimal == "E":
            end_premature(language)
        if decimal == "":
            decimal = 0
            break
        try: 
            decimal = int(decimal)
        except ValueError:
            print(texts.wrong_enter[language])
            continue
        if not 0<= decimal <= 15:
            print(texts.wrong_enter[language])
            continue
        go_next = True







    print("finiš")
    print(numcount,operators,interval,decimal)
        
    






