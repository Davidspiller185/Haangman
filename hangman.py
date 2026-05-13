import random
def lst_words():#רשימת המילים
     words=["banana", "apple", "eggplant", "tomato", "cucumber", "computer", "mouse", "keyboard", "monitor", "phone",
        "window", "door", "wall", "table", "chair", "notebook", "pen", "pencil", "bag", "book"]
     return words
    
def choose_secret_word(words:list):#  בחירת המילה
    word=random.choice(words)
    return word
def init_state(secret:str,max_tries:int):#יוצר מצב משחק
    lst_str="_" .split() * len(secret)
    my_guess=[]
    dic={"secret":secret,
         "display":lst_str,
         "guessed":my_guess,
         "wrong_guesses":0,
         "max_tries":max_tries}
    return dic
def prompt_guess():
    letter=input(" Enter a leeter please ")
    return letter
def validate_guess(ch:str,gussed:list[str]):#אחראי על הבדיקת ולידציה
    if (not ch.isalpha()) or (len(ch)>1) :
        return False,"you need to choice one letter"
    elif ch in gussed:
        return False,"the letter already choice"
    elif not ch.isascii():
        return False,"the leeter need to be in englich"
    elif ch !=ch.lower():
        return False,"the leeter need to be lower"
    else:
        return True,"your choice is valid"
def apply_guess(state:dict,ch:str):#בדיקה אם האות קיימת במילה 
    state["guessed"].append((ch))
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
def print_status(state:dict):#הדפסת הסטטוס כולל המילה לתצוגה והאותיות שנוחשו והניחושים שנותרו
    remaining_guesses=state["max_tries"] - state["wrong_guesses"]
    print(f"the display is:{state["display"]},the guessed is:{state["guessed"]},the remaining_guesses:{remaining_guesses}")
def is_won(state:dict):#בדיקת ניצחון אם כל האותיות נחשפו 
    if "".join(state["display"])==state["secret"]:
        return True
    else:
        return False
def is_lost(state:dict):#בדיקת הפסד אם נגמרו הניחושים המותרים 
    if state["wrong_guesses"]>=state["max_tries"]>=state["max_tries"]:
        return True
    else:
        return False
def print_result(state:dict):#הדפסת הודעה בסוף המשחק והמגת המילה הסודית והאותיות שנוחשו 
    if is_won(state):
        print("you win the game because you guessed all the right letter")
        print(f"yhe word is {state["secret"]},and your guessed letter was:{state["guessed"]}")
    elif is_lost(state):
        print("you lost the game because your max tries is finish")
        print(f"yhe word is {state["secret"]},and your guessed letter was:{state["guessed"]}")
def main(words:list[str],max_tries:int=6):#הפונקציה המרכזית שמעילה את המשחק עם שאר הפונקציות 
    word=choose_secret_word(words)
    dic=init_state(word,max_tries)
    while dic["max_tries"]-dic["wrong_guesses"]>0 and "".join(dic["display"])!=dic["secret"]:
        print_status(dic)
        letter=prompt_guess()
        tup_valid=validate_guess(letter,dic["guessed"])
        while not tup_valid[0]:
            print(tup_valid[1])
            letter=prompt_guess()
            tup_valid=validate_guess(letter,dic["guessed"])
        print(tup_valid[1])
        result_guesses=apply_guess(dic,letter)
        if result_guesses:
            print({"successes": "the letter is in the word"})
        else:
            print({"failed": "the letter is not in the word"})
    print_result(dic)

if __name__=="__main__":
      words=lst_words()
      main(words,5)







    



    