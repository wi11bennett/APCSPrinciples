#selects random number that u guess
import random
rnum = random.randint (1000, 9999)
print (rnum)
#guesses vriable
guesses = 5
usersuccess = ["-", "-", "-", "-"]

#makes random nmber list so that it can be compared to the number that is guessed
strnum = str (rnum)
rnumlist = []
guesslist = []
for digit in strnum:
    rnumlist.append (int(digit))
print (rnumlist)

#user input
while guesses != 0:
    userinput1 = input ("Enter 4 numbers: ")

#checks if everything is correct, says congrats if it is
    for digit in userinput1 :
        guesslist.append(int(digit))
    if guesslist == rnumlist:
        print("Congrats")
        guesses = 0

#if it isnt right then it checks each index to see if they match and shows the player what numbrs match
    else:
        for i in guesslist:
            if i in rnumlist:
                indexnumber = 0
                for j in rnumlist:
                    if j == i:
                        usersuccess.pop(indexnumber)
                        usersuccess.insert(indexnumber, i)
                    indexnumber += 1

        guesses -= 1
        if guesses == 0:
            print ("out of guesses")
            userinput2: input ("Do you want to play again?")
            if userinput2.lower() == ("yes") :
                guesses = 5
            else:
                print ("thanks for playing")


        else:
            print("Sorry. You have " + str(guesses) + "  guesses left.")


        print(usersuccess)

    #     for i in guesslist:
    #         for j in rnumlist:
    #             if i == j :
    #                 rnumindex = rnumlist.index(j)
    #                 guessindex = guesslist.index(i)
    #                 if rnumindex == guessindex:
    #
    #                     guesses += 1
    #
    #                     rnumlist.pop(rnumindex)
    #                     rnumlist.insert(rnumindex, "-")
    # guesses -= 1
    # print (guesses, usersuccess)


    guesslist.clear ()








