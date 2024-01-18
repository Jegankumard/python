import random

def guessnum(x,guesses):
    randomcom=random.randint(1,x)
    for attempt in range(1,guesses+1):
        print(f"=======================")
        print(f" Attempt - #{attempt}/{guesses}")
        print(f"=======================")
        guessuser=int(input(f"Guess any number between 1 and {x} : "))
        if (randomcom == guessuser):
            print(f"VOILA!!! :-) Your GUESS {randomcom} is correct in #{attempt} Attempt")
            break        
        elif (randomcom-guessuser) < 0 and abs(randomcom-guessuser) <= 5:
            print("Sorry Guess again. > HINT:-your guess is higher and very closer(+/-5)")
        elif (randomcom-guessuser) < 0:
            print("Sorry Guess again. > HINT:-your guess is higher")
        elif (randomcom-guessuser) > 0 and abs(randomcom-guessuser) <= 5:
            print("Sorry Guess again. > HINT:-your guess is lower and very closer(+/-5)")
        elif (randomcom-guessuser) > 0:
            print("Sorry Guess again. > HINT:-your guess is lower")
    print(f"                                                           ")
    print(f"=====< Random number chosen by system is {randomcom} >=====")
    print(f"                                                           ")

def compguess(h,guesses):
    l=1
    usernum=int(input(f"Enter the number which you want computer to guess between 1 to {h}: "))
    for attempt in range(1,guesses+1):
        print(f"=======================")
        print(f" Attempt - #{attempt}/{guesses}")
        print(f"=======================")
        compnum=random.randint(l,h)
        print(f"Computer guess is {compnum}")
       
        if (compnum == usernum):
            print(f"VOILA!!! :-) Computer GUESS {compnum} is correct in #{attempt} Attempt")
            break
        elif (compnum-usernum)<0 and abs(compnum-usernum) <= 5:
            userhint=str(input(f"Computer guess is {compnum} higher or lower [Hint: l]: "))
            print("Sorry Guess again. > HINT:-Computer guess is lower and very closer(+/-5)")
            l,h=compnum+1 if l==compnum else compnum, min(h,compnum+5)
            print(f"Now Computer will guess in range between {l} and {h}")
        elif (compnum-usernum)<0:
            userhint=str(input(f"Computer guess is {compnum} higher or lower [Hint: l]: "))
            print("Sorry Guess again. > HINT:-Computer guess is lower")
            l=compnum
            print(f"Now Computer will guess in range between {l} and {h}")
        elif (compnum-usernum)>0  and abs(compnum-usernum) <= 5:
            userhint=str(input(f"Computer guess is {compnum} higher or lower [Hint: h]: "))
            print("Sorry Guess again. > HINT:-Computer guess is higher and very closer(+/-5)")
            l,h=max(l,compnum-5), compnum
            print(f"Now Computer will guess in range between {l} and {h}")
        elif (compnum-usernum)>0:
            userhint=str(input(f"Computer guess is {compnum} higher or lower [Hint: h]: "))
            print("Sorry Guess again. > HINT:-Computer guess is higher")
            h= compnum
            print(f"Now Computer will guess in range between {l} and {h}")
        
    print(f"                                                           ")
    print(f"=====< Number given by user is {usernum} >=====")
    print(f"                                                           ")

whoguess = (input("Do you want to guess(y/n): "))
limit = int(input("Enter the upper limit range to guess: "))
oppurtunity = int(input("Enter the number of times to guess the number: "))
if whoguess == "y":
    execute = guessnum(limit,oppurtunity)
else:
    execute = compguess(limit,oppurtunity)
     
