from tkinter import *
#import speech
import speech_recognition as sr
import pyttsx3
def weather():
    import api
    api.mains()
def tomorrow():
    import rainfall
    rainfall.possible_rain()
def analyze():
    import rainfall
    rainfall.analyze()
def pred():
    import temp
    temp.predict()
def ori():
    import temp
    temp.original() 
def main():
    root = Tk() #makes a blank popup, under the variable name 'root'
    topFrame = Frame(root,bg="#837E7C")
    root.geometry("1000x900")
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    root.title("Weather App")
    root.configure(bg='#2C3539')
    f = ("poppins", 15, "bold")
    t = ("poppins", 35, "bold")
    label1 = Label(topFrame,borderwidth = 1,font = t)
    label1.pack()
    title = "\n" + "WEATHER REPORT " + "\n"
    label1.config(text = title,foreground = "white",bg="#837E7C",width = 20) 
    button3 = Button(topFrame, text='Analyze avarage rainfall every month for india', fg='green',command = analyze,font = f,bg='#0C090A')
    button1 = Button(topFrame, text='Current weather report for specific city	',command = weather, fg='red',font = f,bg='#0C090A')
    button2 = Button(topFrame, text='Do you need to predict rainfall tomorrow	?', fg='blue',command = tomorrow,font = f,bg='#0C090A')
    button4 = Button(topFrame,	text='Predict the temparature for year.	', fg='pink',command = pred,font = f,bg='#0C090A')
    button5 = Button(topFrame,	text='original vs prected temparature.	', fg='yellow',command = ori,font = f,bg='#0C090A')
    button5.pack(side=BOTTOM,padx=20, pady=20)
    button4.pack(side=BOTTOM,padx=20, pady=20)
    button2.pack(side=BOTTOM,padx=20, pady=20)
    button3.pack(side=BOTTOM,padx=20, pady=20)
    button1.pack(side=BOTTOM,padx=20, pady=20)
    root.mainloop() #loops the program forever until its closed
listener = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Hi I am alexa")
engine.say("Are you blind")
engine.runAndWait()
count = 0
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take():
    try:
        with sr.Microphone() as source:
            print("Listening	")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        command = 'pls say correctly'
    return command 
def run_alexa(count):
    if count == 1:
        talk("say yes or no")
    else:
        talk("Do you want again")
    command = take()
    if 'yes' in command or 's' in command:
        talk("What is your query")
        command = take()
        if 'city' in command:
            weather()
        elif 'tomorrow' in command:
            tomorrow()
        elif 'analyze' in command:
            analyze()
        elif 'predict' in command:
            pred()
        elif 'original' in command:
            ori()
    else:
         main()
while True:
    count += 1
    run_alexa(count)
