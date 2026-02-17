secrete_number =9
i=0
chance =int(input("Eneter the number cances you needed to win the game"))
while(i<chance):
   guess =int(input("guess the number"))
   i +=1
   if guess == secrete_number:
    print("you won the game ")
    break
else:
   print("you lost")


