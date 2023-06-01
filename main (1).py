#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

# test_seed = input("type any number under 5 digit\n")

# random.seed(test_seed)

# random_side = random.randint(0 , 1)

# if random_side == 0 :
#   print("Heads")
# else: print("Tails")

random_number = random.randint(20,100)

your_name = input("Tomar nam ki? \n")

their_name = input("Tomar partner er nam ki? \n")

if random_number <= 50 :
  print(f"Tomader Valobasa matro {random_number}%, Mone hosse beshi valobasa nei.",)
elif random_number >= 50 and random_number<= 75 : 
  print(f"Tomader Valobasa motamuti {random_number}%, Motamuti valobasa ase bola jai")
else: print(f"Tomader valobasa onek valo {random_number}%, Tomra sarajibon sathe thakbe")





