import os
import pyttsx3 as p

p.speak("Can I know your name please")
name=input("Can I know your name please?: ")
print()
ch = 'yes'
while ch == 'yes':
    print("***********************************************************************************")
    print("Greetings! Welcome to Automated Menu Driven Program to open applications from MacOS")
    print("***********************************************************************************")
    
    print()
    print("Hello! "+name+"! Let's Start!")
    p.speak("Hello!"+ name+" Welcome to Automated Menu Driven Program to open applications from Mac operating system")
    print("1. Open Google Chrome Browser ")
    p.speak("Option one google chrome")
    print("2. Open Calculator ")
    p.speak("Option two calculator")
    print("3. Open Camera")
    p.speak("Option three camera")
    print("4. Open Text Editor(TextEdit) application")
    p.speak("Option four text editor")
    print("5. Open Siri Asssitant ")
    p.speak("Option five siri")
    print("6. Open QuickTime Player")
    p.speak("Option six quick time player")
    print("7. Open Podcasts")
    p.speak("Option seven podcasts")
    print("8. Open iMovies")
    p.speak("Option eight iMovies")
    print("9. Open WhatsApp")
    p.speak("Option nine whatsapp")
    print("10. Display Calendar ")
    p.speak("option ten display calendar")
    print("11. Display today's date")
    p.speak("option eleven displaying date")
    p.speak("Choose what you want to do?")
    print()
    choice = input("Choose what you want to do?:").lower()
    
    if((("open" in choice) and ("google" in choice) and ("chrome" in choice) and ("browser" in choice)) or (int(choice) == 1) or (("open" in choice) and ("chrome" in choice)) or (("launch" in choice) and ("chrome" in choice))):
        p.speak("opening chrome browser for you")
        os.system("open -a Chrome.app")
        
    elif((("open" in choice) and ("calculator" in choice)) or (int(choice) == 2) or (("launch" in choice) and ("calculator" in choice))):
        p.speak("opening calculator for you")
        os.system("open -a Calculator.app")
        
    elif((("open" in choice) and ("camera" in choice)) or (int(choice) == 3) or (("launch" in choice) and ("camera" in choice))):
        p.speak("opening camera for you")
        os.system("open -a FaceTime.app")

    elif((("open" in choice) and ("textedit" in choice)) or (int(choice) == 4) or (("launch" in choice) and ("textedit" in choice))):
        p.speak("opening text editor for you")
        os.system("open -a TextEdit.app")
        
    elif((("open" in choice) and ("siri" in choice) and ("assisstant" in choice)) or (int(choice) == 5) or (("launch" in choice) and ("siri" in choice))):
        p.speak("opening siri assisstant for you")
        os.system("open -a Siri.app")
        
    elif((("open" in choice) and ("quicktime" in choice) and ("player" in choice)) or (int(choice) == 6) or (("launch" in choice) and ("quicktime" in choice))):
        p.speak("opening quick time player for you")
        os.system("open -a QuickTime\ Player.app")
        
    elif((("open" in choice) and ("podcasts" in choice)) or (int(choice) == 7) or (("launch" in choice) and ("podcasts" in choice)) or (("listen" in choice) and ("to" in choice) and ("podcasts"in choice))):
        p.speak("opening podcasts for you")
        os.system("open -a Podcasts.app")
           
    elif((("open" in choice) and ("imovies" in choice)) or (int(choice) == 8) or (("watch" in choice) and ("imovies" in choice))):
        p.speak("opening imovies for you")
        os.system("open -a iMovie.app")
               
    elif((("open" in choice) and ("whatsapp" in choice)) or (int(choice) == 9) or (("launch" in choice) and ("whatsapp" in choice))):
        p.speak("opening whatsapp for you")
        os.system("open -a WhatsApp.app")
               
    elif((("display" in choice) and ("calendar" in choice)) or (int(choice) == 10) or (("open" in choice) and ("calendar" in choice))):
        p.speak("showing calender")
        os.system("cal")
        
    elif((("display" in choice) and ("date" in choice)) or (int(choice) == 11) or (("show" in choice) and ("date" in choice))):
        p.speak("showing today's date")
        os.system("date")
        
    else:
        p.speak("Application or software is not listed in the menu")
        exit()

        
    print()
    p.speak("Do you wish to continue yes or no")
    ch=input("Do you wish to continue(yes/no): ").lower()
    if(ch!='yes'):
        break

