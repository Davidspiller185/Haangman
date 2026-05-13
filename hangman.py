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

    



    