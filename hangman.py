import random
def choose_secret_word():# רשימת המילים ובחירת המילה
    words=["Banana", "Apple", "Eggplant", "Tomato", "Cucumber", "Computer", "Mouse", "Keyboard", "Monitor", "Phone",
        "Window", "Door", "Wall", "Table", "Chair", "Notebook", "Pen", "Pencil", "Bag", "Book"]
    word=random.choice(words)
    return word
def init_state(secret:str,max_tries:int):#יוצר מצב משחק
    lst_str="_" .split * len(secret)
    my_set=set()
    dic={"secret":secret,
         "display":lst_str,
         "guessed":my_set,
         "wrong_guesses":0,
         "max_tries":max_tries}
    return dic
def prompt_guess():
    letter=input("Enter a leeter please")
    return letter
def validate_guess(ch:str,gussed:set[str]):#אחראי על הבדיקת ולידציה
    if (not ch.isalpha()) or (len(ch)>1) or (ch in gussed):
        return False,"you need to choice one letter"
    else:
        return True,"your choice is valid"
def apply_guess(state:dict,ch:str):
    state["guesses"].add(ch)
    flag=False
    for i in range(len(state["secret"])):
        if state["secret"][i]==ch:
            state["display"][i]=ch
            flag=True
    if flag:
        return True
    else:
        state["wrong_guesses"]+=1
        return False
def print_status(state:dict):
    remaining_guesses=state["max_tries"] - state["wrong_guesses"]
    print(f"the display is:{state["display"]},the guessed is:{state["guessed"]},the remaining_guesses:{remaining_guesses}")
def is_won(state:dict):
    if state["display"]==state["secret"]:
        return True
    else:
        return False
def is_lost(state:dict):
    if state["wrong_guesses"]>=state["max_tries"]>=state["max_tries"]:
        return True
    else:
        return False
def print_result(state:dict):
    if is_won(state):
        print("you win the game because you guessed all the right letter")
        print(f"yhe word is {state["secret"]},and your guessed letter was:{state["guessed"]}")
    elif is_lost(state):
        print("you lost the game because your max tries is finish")
        print(f"yhe word is {state["secret"]},and your guessed letter was:{state["guessed"]}")
def play(words:list[str],max_tries:int=6):
    word=choose_secret_word(words)
    dic=init_state(word,max_tries)       





    



    