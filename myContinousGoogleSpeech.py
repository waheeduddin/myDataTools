import pyaudio,os
import speech_recognition as sr


def mainfunction(source):
    audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print(r.recognize_google(audio))#,language = "nl-NL"))#, show_all=True))
        #print("You said: " + r.recognize_google(audio,language="nl-NL"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    r = sr.Recognizer()
    print("you can speak now....")
    with sr.Microphone() as source:
      #  r.adjust_for_ambient_noise(source)
        while 1:
            mainfunction(source)
