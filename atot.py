#import re
import sys
import nltk
#from tqdm import tqdm
import speech_recognition as sr
#with open("api-key.json") as f:
 #   GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

r = sr.Recognizer()
with sr.AudioFile("out000.wav") as source:
    audio1 = r.listen(source)
with sr.AudioFile("out001.wav") as source:
    audio2 = r.listen(source)
try:
    s=r.recognize_google(audio1)
    #se=re.sub(r'(?<=[.,])(?=[^\s])', r' ', s)
    #n = nltk.tokenize.punkt.PunktSentenceTokenizer()
    #k=n.sentences_from_text(s)
    
    file = open('rtr1.txt', 'w')
    
    file.write(str(s))
    s=r.recognize_google(audio2)
    file.write(str(s))
    file.close()
except Exception as e:
    print("Exception: "+str(e))

