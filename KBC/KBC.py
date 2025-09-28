print("welcome to KBC")
from playsound import playsound
playsound(r"D:\games\kbc_theme.mp3")
print("Deviyo or sajjano aaj ka khel shuru karte he")
count=0
def countt(a): 
   if(a==0):
      m=0
   elif(a==1):
      m=10000
   elif(a==2):
      m=50000
   elif(a==3):
      m=1000000   
   elif(a==4):
      m=5000000
   elif(a==5):
      m=10000000
   elif(a==6):
      m=50000000
   return m

qb=['''Q.1  Which country is the largest by land area?

a.india       c.south africa
b.China       d.Russia''',


'''Q.2  Where is India Gate located?

a.Agra     c.Mumbai
b.Punjab   d.New Delhi''',


'''Q.3  Who wrote India's National Anthem?

a.Rabindranath Tagore
b.Lal Bahadur Shastri
c.Chetan Bhagat
d.RK Narayan''',

'''Q.4  Which city is known as the Pink City of India?

a.Banglore     b. Jaipur 

c.Maysore      d. Kochi''',
'''Q.5  Which city is known as the "Silicon Valley Of India"?

a.Delhi     b.Chennai

c.Bangalore    d.Mumbai''',

'''Q.6  Which of the following is known as the mans most useful tree?

a.Walnut      b.coconut
c.Teak        d.Mango ''',] 

i=0
while i<len(qb):
     print(qb[i])
     print("choose one option from above")
     x=input()
     if(i==0 and x=='d'):
         print("sahi jawab")
         count=count+1
     elif(i==1 and x=='d'):
         print("sahi jawab")
         count=count+1
     elif(i==2 and x=='a'):
         print("sahi jawab")
         count=count+1
     elif(i==3 and x=='b'):
         print("sahi jawab")
         count=count+1
     elif(i==4 and x=='c'):
         print("sahi jawab")
         count=count+1
     elif(i==5 and x=='b'):
         print("sahi jawab")
         count=count+1
     else:
        print("galat jawab")
     print("Aapki ab tk ki dhanrashi hai",countt(count),"rupaye")
     if(i<=(len(qb)-2)):
         print("Agala sawal ye raha aapki computer screen pr\n")
     i=i+1

import pygame 
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("D:\\games\\7_crore_meme_sound_kbc.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue


    
