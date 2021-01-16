'''
if i'm bothered, I will differentiate between stressed and non-stressed vowels by taking a word and seeing if it contains: [CONSONANT][VOWEL][CONSONANT][VOWEL]
but to do that I will have to remake it___   
if sentence[i] contains any consonant:    |
  if sentence[i][c+1] == any vowel:       |
    if sentence[i][c+2] == any consonant: |<------long, inefficient, stupid
      if sentence[i][c+3] == any vowel:   |
        WOOWWWWWW!!!! YAYYYY!!!___________|
'''
from pydub import AudioSegment
def initLetters(text, audioFormat):
  soundAlphabet = []
  textNumbers = [] 
  textSounds = []
  combiner = None
  
  for i in "abcdefghijklmnopqrstuvwxyz": # GET FILES IN ALPHABETICAL ORDER > soundAlphabet
    soundAlphabet.append(AudioSegment.from_file(i+"."+audioFormat, audioFormat))
    
  for i in text: # TRANSLATES THE USER'S TEXT TO A0Z25 > textNumbers   
    letter = ord(i)-65
    textNumbers.append(letter) #USE textNumbers TO INDEX THE SOUND ALPHABET soundAlphabet > textSounds  
    
  for i in textNumbers:
    if i == -33:
      textSounds.append(AudioSegment.from_file("space."+audioFormat, audioFormat))
      continue
    elif i == -19:
      textSounds.append(AudioSegment.from_file("period."+audioFormat, audioFormat))
      continue
    else:
      textSounds.append(soundAlphabet[i])
      
  for i in textSounds: # Add up all the sound files to make one big sound file named 'output.[format]'
    combiner = combiner+i
    
  combiner.export("output."+audioFormat, format=audioFormat)  
  
def menu(): 
  print("WELCOME TO MY PROGRAM THAT ISN'T CREEPY, I hope you're having a good day.\nName every file you put in the directory in the format: [letter_in_lowercase].[format], for example: 'a.wav'")
  print("P.S: The period/full stop file should be named 'period.[format]' and will ideally be a breath. The space file should be named 'space.[format]' and will ideally be half a second of no noise. This only supports letters A-Z and characters space: ' ' and periods: '.'")

  audioFormat = input("What audio format do you want to use?\n") #OPTIONS: wav, mp4, mp3, ogg, flv, wma, "anything ffmpeg supports" - PyDub Team.
  text = input("Enter the text you want them to say:\n")
  text = text.upper()     #TEXT CONVERTED TO ALL CAPS SO I CAN ORD THEN -65 TO GET ALPHABET
  initLetters(text, audioFormat)  
    
