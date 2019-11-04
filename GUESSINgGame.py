
import random
rnum = random.randint (1000, 9999)
print (rnum)

strnum = str (rnum)
rnumlist = []
guesslist = []
for digit in strnum:
    rnumlist.append (int(digit))
print (rnumlist)

#nothing for now
userinput1 = input ("Enter 4 numbers: ")
if int(userinput1) == rnumlist:
    print ("correct")

for digit in userinput1 :
    guesslist.append(int(digit))

for i in rnumlist:
    for j in guesslist:
        if i == j :
            print (rnumlist.index(i))
        else:
            print ("incorrect")




