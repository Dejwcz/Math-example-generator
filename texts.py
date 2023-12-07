"""
Texts displayed in the program
"""

#dict is used for easy language change

language_list = {"1":"1: pro češtinu",
                 "2":"2: for english"}

lng_choice = {"cz":"Vyber jazyk: ",
              "en":"Choose language: "}

bad_choice = {"cz": "Vaše volba neodpovídá možnostem. Zvolte znovu: ",
              "en": "Your choice is wrong. Choose again:"}

greetings = {"cz":"Vítejte v generátoru matematických příkladů",
             "en":"Welcome in math excercises generator" }

info = {"cz":"Tento program slouží pro vygenerování příkladů určených pro \
procvičování. Po zadání parametrů vygeneruje požadovaný počet \
příkladů v definovaném intervalu. Pro více informací zadejte \
požadovaný operátor(+,-,*,/) a otazník. Pro pokračování stiskni ENTER. Pro \
změnu jazyka zadejte L a pro ukončení zadejte E.",
        "en":"This program is intended to generate examples give for \
practicing. After entering the parametres it will generate the required \
number of examples in defined interval. For more information enter \
the requred operator(+,-,*,/) and question mark. To continue press \
ENTER, type L for language change, and type E to exit."}

examlpes_number = {"cz":"Zadej požadovaný počet příkladů: ",
                  "en":"Enter the required number of examples: "}

operands_number = {"cz":"Zadej požadovaný počet operandů: ",
                  "en":"Enter the required number of operands: "}

wrong_enter = {"cz":"Špatné zadání. ",
               "en":"Wrong enter. "}

are_sure_ex = {"cz":"Jste si jistí zvoleným počtem? Generování velkého počtu \
příkladu může chvíli trvat. Zmáčkni ENTER pro pokračování. Zvolený počet: ",
               "en":"Are you sure? Generating a lot of excercise can take \
a lot of time. Press ENTER to continue. Your number of excercise : "}

are_sure_operands = {"cz":"Jste si jisí zvoleným počtem? Při použití velkého \
počtu operandů budou příklady příliš dlouhé a generování může chvíli trvat. \
Zmáčkni ENTER pro pokračování. Zvolený počet: ",
                     "en":"Aro you sure? If many operands are used, examples \
they will be too long and generating can take a lot of time. Press ENTER to \
continue. Your number of excercise :"}

help_add = {"cz":"Vygeneruje příklady na sčítání pro určený počet čísel.",
             "en":"Generates excercises for addition for a \
given number of numbers"}

help_sub = {"cz":"Vygeneruje příklady na odčítání pro určený počet čísel.",
            "en":"Generates excercises for substraction for a \
given number of numbers"}

help_mul = {"cz":"Vygeneruje příklady na násobení pro určený počet čísel.",
            "en":"Generates excercises for multiplication for a \
given number of numbers"}

help_div = {"cz":"Vygeneruje příklady na dělení pro určený počet čísel.",
            "en":"Generates excercises for division for a \
given number of numbers"}

operator_choice = {"cz":"Zadej požadované operátory pro příklady(+,-,*,/): ",
                   "en":"Enter the requred operators(+,-,*,/) "}

end_prem = {"cz":"Děkujeme za požití našeho programu a přejeme krásný den.",
            "en":"Thank you for using our program and have a nice day."}

interval_choice = {"cz":"Zadej interval pro příklady: V základu je interval \
od 0 do 1000. Pokud nechceš interval měnit, nechej volby prázdné.",
                  "en":"Enter an interval for examples. In default is the \
interval from 0 to 1000. If you don't want interval change leave the \
options blank."}

begin_interval = {"cz":"Začátek intervalu: ",
                  "en":"Start of interval: "}

end_interval = {"cz":"Konec intervalu: ",
                "en":"End of interval: "}

bad_interval = {"cz":"Konec intervalu musí být větší než jeho začátek. \
Zkus to znovu!",
                "en":"End of interval must be bigger than the start. \
Try it again!"}

decimal_coice = {"cz":"Zadej počet desetiných míst(Max: 15). Pro celá čísla \
stiskni ENTER: ",
                 "en":"Enter decimal numbers(Max: 15). For integers press \
ENTER: "}

file_examples = {"cz":"priklady.txt", 
                 "en":"examples.txt"}
file_results = {"cz":"vysledky.txt",
                "en":"results.txt"}
two_txt_saved = {"cz":"Vaše příklady a výsledky byly uloženy do dvou \
souborů: ",
                 "en":"Your examples and results have been saved to \
two files: "}

and_text = {"cz":" a ",
            "en":" and "}