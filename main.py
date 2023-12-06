import UItext as UI

language = "cz"
run = ""

while not run == "E":
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
UI.choose_menu(language)






