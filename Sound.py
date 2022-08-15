def sound():
    from playsound import playsound
    print('Abdul kalam speaking')
    playsound('D:\sih\ham.mp3')
    return
sound()
print("\n These are the questions: ")
print("\n 1.Where were you born and brought up?")
print("\n 2.What are the educational institutions that you studied in?")
print("\n 3.When did you join the DRDO?")
print("\n 4.How was your experience as the President of India?")
print("\n 5.What are your most treasured awards?")
print("\n 6.Exit")
from playsound import playsound
def q1():
    from playsound import playsound
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say('\n Where were you born and brought up?')
    engine.runAndWait()
    return
def q2():
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say('What are the educational institutions that you studied in? ')
    engine.runAndWait()
    return
def q3():
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say(' \n When did you join the DRDO?')
    engine.runAndWait()
    return
def q4():
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say('\n How was your experience as the President of India?')
    engine.runAndWait()
    return
def q5():
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say('What are your most treasured awards?')
    engine.runAndWait()
    return
def exit1():
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say('You have successfully exited')
    engine.runAndWait()
    return
def invalid():
    import pyttsx3
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',135)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',1)
    engine.say('Provide a valid input from 1 to 6')
    engine.runAndWait()
    return
def loop():
    n='zero'
    while(n=='zero' or 'one' or 'two' or 'three' or 'four' or 'five' or 'six'):
        #n=int(input('Please enter the question number to get the reply: '))
        import speech_recognition as sr
        recognizer = sr.Recognizer()

        ''' recording the sound '''

        with sr.Microphone() as source:
            print("Adjusting noise ")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Please tell the question number to get the reply")
            recorded_audio = recognizer.listen(source, timeout=10)
            #print("Done recording")

        ''' Recorgnizing the Audio '''
        try:
            print("Recognizing the text")
            text = recognizer.recognize_google(
                    recorded_audio, 
                    language="en-US"
                    )
            print("You have asked for question number : {}".format(text))
        except sr.UnknownValueError:
            print("Could not understand audio")
            loop()
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            loop()
        n=text
        if n=='1' or 'one':
            print("\n Where were you born and brought up?")
            print('I was born on 15th october 1931, to a Tamil Muslim family in the pilgrimage centre of Rameswaram on Pamban Island.')
            q1()
            playsound('D:\sih\Q1.mp3')
        elif n=='t2' or 'two':
            print('\n What are the educational institutions that you studied in?')
            print('I did my schooling at the Schwartz Higher Secondary School, Ramanathapuram, and went on to attend Saint Josephs College, Trichy, then affiliated with the University of Madras, from where I graduated in Physics in 1954.I moved to Madras in 1955 to study Aerospace engineering in Madras Institute of Technology.')
            q2()
            playsound('D:\sih\Q2.mp3')
        elif n=='3' or 'three':
            print('\n When did you join the DRDO?')
            print('After Graduating from the Madras Institute of Technology in 1960, I joined the Aeronautical Development Establishment of the Defence Research and Development Organization as a scientist after becoming a member of the Defence Research and Development Service.')
            q3()
            playsound('D:\sih\Q3.mp3')
        elif n=='4' or 'four':
            print('\n How was your experience as the President of India?')
            print('During my Presidency, I was affectionately known as the People\'s President. Signing the Office of Profit Bill was the toughest decision I had to take during my tenure. I also supported the need of Uniform Civil Code in India, keeping in view the population of the country.')
            q4()
            playsound('D:\sih\Q4.mp3')
        elif n=='5' or 'five':
            print('What are your most treasured awards?')
            print('I consider the affection of my fellow citizens and the youth as my greatest honour. Apart from this privilege, I have received 7 honorary doctorates from 40 universities, The Government of India honoured me with the Padma Bhushan in 1981 and the Padma Vibhushan in 1990, and the Bharat Ratna in 1997.')
            q5()
            playsound('D:\sih\Q5.mp3')
        elif n=='6' or 'six':
            print('You have successfully exited')
            exit1()
            break
        else:
            print('Please provide a valid input from 1 to 6')
            invalid()
loop()
