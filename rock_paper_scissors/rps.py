# #!/usr/bin/python

# import sys

# def rock_paper_scissors(n):
#   pass 


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')

import random
import time
x=     "                (  )"
a=     "               /  /"
e=     "    __________/  /________"
r=     "                  ________)_"
t=     "                     ________)"
h=     "      _____       __________)"
u=     "           \_______________)"      
  
i="                 __    "
o="               _/ /     "
p="            __/ /       "
q="      _____/   /_______ "
s=" ____/         ________)"
d="                __)     "
f="              __)       "
g=" ______________)        "

j="               __       "
k="         _____/  )_     "
l="    ____/       ¤ _)    "
m="                ¤ _)    "
b="                ¤ _)    "
n="    ____________¤_)     "


z =input("tap '1' to play with the bot and '2' to play with a friend")
if z =="1":
 while(1<2):
  
  CPURPS = ['rock', 'paper', 'scissors']
  y = random.choice(CPURPS)

  z =input("rock, paper or scissors?")
  print("beat the bot!")
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)

 
 
  if z=="scissors":

    print (i)
    print (o)
    print (p)
    print (q)
    print (s)
    print (d)
    print (f)
    print (g)
    
  if z=="paper":

    print (x)
    print (a)
    print (e)
    print (r)
    print (t)
    print (h)
    print (u)

  if z=="rock":

    print (j)
    print (k)
    print (l)
    print (m)
    print (b)
    print (n)



  if y=="scissors":

    print (i)
    print (o)
    print (p)
    print (q)
    print (s)
    print (d)
    print (f)
    print (g)

  if y=="rock":

    print (j)
    print (k)
    print (l)
    print (m)
    print (b)
    print (n)

  if y=="paper":

    print (x)
    print (a)
    print (e)
    print (r)
    print (t)
    print (h)
    print (u)


  if y=="paper":
   if z=="scissors":
     print("wins!!")
   else:
     if z=="paper":
       print("tie")
     else:
       print("lost")


  if y=="scissors":
   if z=="scissors":
     print("tie")
   else:
     if z=="paper":
       print("lost")
     else:
       print("wins!!")

  if y=="rock":
   if z=="scissors":
     print("lost")
   else:
     if z=="paper":
       print("wins!!")
     else:
       print("tie")
if z =="2":
 while(1<2):
  z =input("rock, paper or scissors?")
  for i in range (50):
    print("")
  y =input("rock, paper or scissors?")
  for i in range (50): 
    print("")
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
 
  if z=="scissors":

    print (i)
    print (o)
    print (p)
    print (q)
    print (s)
    print (d)
    print (f)
    print (g)
  if z=="paper":

    print (x)
    print (a)
    print (e)
    print (r)
    print (t)
    print (h)
    print (u)
  if z=="rock":

    print (j)
    print (k)
    print (l)
    print (m)
    print (b)
    print (n)

  if y=="scissors":

    print (i)
    print (o)
    print (p)
    print (q)
    print (s)
    print (d)
    print (f)
    print (g)
  if y=="rock":

    print (j)
    print (k)
    print (l)
    print (m)
    print (b)
    print (n)
  if y=="paper":

    print (x)
    print (a)
    print (e)
    print (r)
    print (t)
    print (h)
    print (u)


  if y=="paper":
   if z=="scissors":
     print("player 1 wins")
   else:
     if z=="paper":
       print("tie")
     else:
       print("player 2 wins")
  if y=="scissors":
   if z=="scissors":
     print("tie")
   else:
     if z=="paper":
       print("player 2 wins")
     else:
       print("player 1 wins!")
  if y=="rock":
   if z=="scissors":
     print("player 2 wins!")
   else:
     if z=="paper":
       print("player 1 wins!")
     else:
       print("tie")



 
