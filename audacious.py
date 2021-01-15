'''
OPEN aeiou SOUNDS THE USER PUT IN THE DIR
OPEN CONSONANT SOUNDS OR IMPORT DEFAULTS (bcdfghjklmnpqrstvwxy?z)
INPUT TEXT FROM USER
STICK SOUNDS TOGETHER SOMEHOW
#SOMETHING IDK
#EBIN PROFIT
OUTPUT AUDIO SPEECH AS WAV


 USE  ORD AND .LOWER
 EITHER USE PYDUB(SHORT BUT REMAKE) OR WAVE(LONG BUT KEEP SAME)
PYDUB:
x_version = AudioSegment.from_file("y.x", "x")
wave = AudioSegment.from_file(i+"."+format, format)
'''
from pydub import AudioSegment
waves = []
caca = [] 
doodoo = []
comb = None

def initLetters(text, format1):
  for i in "abcdefghijklmnopqrstuvwxyz": #get files and puts in waves
    waves.append(AudioSegment.from_file(i+"."+format1, format1))
  for i in text:
    letter = ord(i)-65
    caca.append(letter)
  for i in caca:#FOR EVERY LETTER IN OUR TEXT (represented by a number) in caca, we are going to take the sound bytes for that letter (from waves list) and put it in doodoo (hehe xd)
    doodoo.append(waves[i])
  for i in doodoo: # FOR EVERY WAVE FILE IN OUR ORDERED LIST, we add it up to make one big file and export it
    comb = comb+i
  comb.export("output."+format1, format=format1)   

def menu(): 
  print("WELCOME TO MY PROGRAM THAT ISN'T CREEPY, I hope you're having a good day.\nName every file you put in the directory in the format: [letter_in_lowercase].[format], for example: a.wav")
  format = input("What audio format do you want to use?\n")
  text = input("Enter the text you want them to say:\n")
  text = text.upper()
  initLetters(text, format)  
    
