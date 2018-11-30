#import re
import sys
import nltk
#from tqdm import tqdm
import speech_recognition as sr
#with open("api-key.json") as f:
 #   GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

r = sr.Recognizer()
file = open('rtr2.txt', 'w')
for i in range(3):
    with sr.AudioFile("out00"+str(i)+".wav") as source:
        audio1 = r.listen(source)
    try:
    	s=r.recognize_google(audio1)
    #se=re.sub(r'(?<=[.,])(?=[^\s])', r' ', s)
    	n = nltk.tokenize.punkt.PunktSentenceTokenizer()
    	k=n.sentences_from_text(s)
    
    	
    
    	file.write(str(k))
	#file.write(str(k))
    except Exception as e:
        print("Exception: "+str(e))
file.close()
