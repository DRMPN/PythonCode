#lol i did it but how idk
print("The GAME has been started!")
print("Please think of a number between 0 and 100!")
low=0
high=100
answ=100
answ=(low+high)//2
print("Is your secret number " + str(answ) + "?")
lett="none"
while lett!="c":
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate if I guessed correctly.")
    lett=input("Write it right here: ")
    if lett=="c" or lett=="l" or lett=="h":
        while True:
            if lett=="h":
                low=answ
                answ=(low+high)//2
                print("Is your secret number " + str(answ) + "?")
                break
            elif lett=="l":
                high=answ
                answ=(low+high)//2
                print("Is your secret number " + str(answ) + "?")
                break
            elif lett=="c":
                print("Game over. Your secret number was: " + str(answ))
                break
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(answ) + "?")   
print("You need to worry less about your things and a little more about your debt to me. >:]")
