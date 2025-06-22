import random

m=int(input("No. of trials"))

no = random.randint(1,10)
while(m>0):
  n=int(input("Guess the Number"))
  no = random.randint(1,10)
  if(no==n):
    print("Correct")
  elif(no<n):
    print("Guess lower")
  elif(no>n):
    print("Guess higher")

  print(f"Random Number was {no}")
  m=m-1