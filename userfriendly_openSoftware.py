import os
import pyttsx3 as p

p.speak("Can I know your name please")
name=input("Can I know your name please?: ")
print()
print("***********************************************************************************")
print("Greetings! Welcome to Automated Menu Driven Program to open applications from MacOS")
print("***********************************************************************************")

print()
print("Hello! "+name+"! Let's Start!")
p.speak("Hello!"+ name+" Welcome to Automated Menu Driven Program to open applications from Mac operating system")
ch = 'yes'
while ch=='yes':
    
    choice = input("Choose what you want to do?:").lower()
    
    if(("don't" in choice) or ("not" in choice) or ("dont" in choice)):
        p.speak("Okay "+name+" will not open!")
        print("Okay "+name+" will not open!")
    
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("google" in choice) and ("chrome" in choice) and ("browser" in choice)) or (("open" in choice) and ("chrome" in choice)) or (("launch" in choice) and ("chrome" in choice))):
        p.speak("opening chrome browser for you")
        os.system("open -a Chrome.app")
        
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("calculator" in choice)) or (("launch" in choice) and ("calculator" in choice)) or ("calculate" in choice)):
        p.speak("opening calculator for you")
        os.system("open -a Calculator.app")
        
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("camera" in choice)) or ('3' in choice) or (("launch" in choice) and ("camera" in choice)) or ("pictures" in choice) or ("photos" in choice)):
        p.speak("opening camera for you")
        os.system("open -a FaceTime.app")

    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("textedit" in choice)) or (("launch" in choice) and ("textedit" in choice)) or ("editor" in choice)):
        p.speak("opening text editor for you")
        os.system("open -a TextEdit.app")
        
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("siri" in choice) and ("assisstant" in choice)) or (("launch" in choice) and ("siri" in choice)) or ("siri" in choice)):
        p.speak("opening siri assisstant for you")
        os.system("open -a Siri.app")
        
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("quicktime" in choice) and ("player" in choice)) or (("launch" in choice) and ("quicktime" in choice)) or ("media" in choice) or ("player" in choice)):
        p.speak("opening quick time player for you")
        os.system("open -a QuickTime\ Player.app")
        
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("podcasts" in choice)) or (("launch" in choice) and ("podcasts" in choice)) or ("podcasts"in choice)):
        p.speak("opening podcasts for you")
        os.system("open -a Podcasts.app")
           
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("imovies" in choice)) or (("watch" in choice) and (("movies" in choice) or ("movie" in choice) ))):
        p.speak("opening imovies for you")
        os.system("open -a iMovie.app")
               
    elif(((("open" in choice) or ("run" in choice) or ("execute" in choice)) and ("whatsapp" in choice)) or (("launch" in choice) and ("whatsapp" in choice)) or ("chat" in choice) or ("whatsapp" in choice)):
        p.speak("opening whatsapp for you")
        os.system("open -a WhatsApp.app")
               
    elif(((("run" in choice) or ("display" in choice) or ("display" in choice)) and ("calendar" in choice)) or (("open" in choice) and ("calendar" in choice))):
        p.speak("showing calender")
        os.system("cal")
        
    elif(((("open" in choice) or ("run" in choice) or ("display" in choice)) and ("date" in choice)) or ('b' in choice) or (("show" in choice) and ("date" in choice))):
        p.speak("showing today's date")
        os.system("date")
        
    else:
        p.speak("Application or software is not listed in the menu")
        
    print()
    p.speak("Do you wish to continue chatting with me yes or no")
    ch=input("Do you wish to continue chatting with me(yes/no): ").lower()
    if(ch!='yes'):
        break

