import pyttsx3
import speechrecognition as sr

class AI():
    __name = " "
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

            print("Listening")
            with self.m as source:
                self.r.adjust_for_ambient_noise(source)

        @property
        def name(self,value):
            sentence = "Hello,my name is"+self.__name
            self.__name = value
            self.engine.say(sentence)
            self.engine.runAndWait()
            
        def say(self, sentence):
            self.engine.say(sentence)
            self.engine.runAndWait()

        def listen(self):
            print("say something")
            with self.m as source:
                audio = self.r.listen(source)
            print("got it")    
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language=en)
            sentence = "Got it,you said" + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except as error:
            print("sorry, didnt catch that",e)  
            self.engine.say("sorry didnt catch that")
            self.engine.runAndWait()
        print("You Said", phrase)  

