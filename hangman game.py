import random
name=input("what is your name: ")
print("😎good luck!!",name)
words=["computer" , "laptop" , "mouse" , "keyboard" , "speaker" , "printer"]
word=random.choice(words)
guessess='' 
turns=6
while turns>0:
    failed=0
    for i in word:
        if i in guessess:
            print(i)
        else:
            print("_")
            failed+=1
    if failed == 0:
        print("🤩",name," YOU WON!!!")
        print("the word is: ",word)
        break

    guess=input("guess the character: ")
    guessess=guess+guessess
    if guess not in word:
        turns-=1
        print("🙁worng")
        print("you have",turns,"more gussess")

    if turns == 0:      

        print("☠",name,".....you died")
        print("GAME OVER")
    
            

     

            


