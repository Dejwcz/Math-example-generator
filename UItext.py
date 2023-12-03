import texts
from os import system, name


LINE = 70*"="
language = "cz"

def clrscr():
    if name == "nt":system("cls")
    else: system("clear")


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

def help_operator(option):
    print(LINE)
    if option == "+?":tw_print(texts.help_add[language],len(LINE))
    elif option == "-?":tw_print(texts.help_sub[language],len(LINE))
    elif option == "*?":tw_print(texts.help_mul[language],len(LINE))
    elif option == "/?":tw_print(texts.help_div[language],len(LINE))
    print(LINE)
    


option = ""
help_options = ["+?", "-?", "*?", "/?"]

def start_menu(language):
    clrscr()
    print(LINE)
    print(texts.greetings[language].center(len(LINE)))
    print(LINE)
    print()
    tw_print(texts.info[language],len(LINE))
    print()

def choose_menu(language):
    clrscr()
    print(LINE)
    print(texts.problem_number[language])




start_menu(language)
option = input()
if option in help_options: 
    help_operator(option)
else:
    print(LINE)
choose_menu(language)
