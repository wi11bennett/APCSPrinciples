#selects random number that u guess
import random
rnum = random.randint (1000, 9999)
print (rnum)
#guesses vriable
guesses = 5
usersuccess = ["-,-,-,-"]

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
        for i in rnumlist:
            for j in guesslist:
                if i == j :
                    rnumindex = rnumlist.index(i)
                    guessindex = guesslist.index(j)
                    print(rnumindex, guessindex)
                    if rnumindex == guessindex:
                        print ("One of Your numbers matches")
                        usersuccess.pop(rnumindex)


                        print (usersuccess)
                    else:
                        pass
                else:
                    print ("-")
    guesslist.clear ()



