import os
import pyttsx3 as p
p.speak("Hello user! Please enter your name: ")
name=input("Hello user! Please enter your name: ")

#Using the concept of lists

print("******************************************************************************************************************************")
print("Welcome "+ name+" to the user friendly chat engine where you can open applications of your choice from a Mac Operating System")
print("******************************************************************************************************************************")

p.speak("Welcome "+ name+" to the user friendly chat engine where you can open applications of your choice from a Mac Operating System")

ch = 'yes'
while ch == 'yes':
    words=["run","open","launch","listen","display","show","use","talk","assisstant","want","click","pictures","player","play","watch"]
    negativeWords=["dont","don't","not"]
    choice=input("Enter your choice:").lower()
    flag = True
    
    #Handling negative words
    for j in negativeWords:
        flag=False
        
        
    for i in words:
            if((i in choice) or ("chrome" in choice) and (flag != False)):
                p.speak("opening google chrome for you")
                os.system("open -a Chrome.app")
                break
                
            if((i in choice) or ("gmail" in choice) and (flag != False)):
                p.speak("opening gmail for you")
                os.system("open -a Chrome.app http://gmail.com")
                break
                
            if((i in choice) or ("calculator" in choice) or ("calculate" in choice) and (flag != False)):
                p.speak("opening calculator")
                os.system("open -a Calculator.app")
                break
                
            if((i in choice) or ("podcasts" in choice) and (flag != False)):
                p.speak("opening podcasts for you")
                os.system("open -a Podcasts.app")
                break
            
            if((i in choice) or ("siri" in choice) and (flag != False)):
                p.speak("opening siri assisstant for you")
                os.system("open -a Siri.app")
                break
            
            if((i in choice) or ("camera" in choice) or ("pictures" in choice) and (flag != False)):
                p.speak("opening camera for you")
                os.system("open -a FaceTime.app")
                break
                
            if((i in choice) or ("media" in choice) and (flag != False)):
                p.speak("opening quick time player for you")
                os.system("open -a QuickTime\ Player.app")
                break
                
            if((i in choice) or ("movie" in choice) or ("movies" in choice) and (flag != False)):
                p.speak("opening iMovies for you")
                os.system("open -a iMovie.app")
                break
            
            else:
                p.speak("Oops! Sorry! Cannot open the application that you are asking for!")
                print("Sorry")
                break
            
    p.speak("Do you wish to continue chatting with me yes or no? ")
        
    ch = input("Do you wish to continue chatting with me (yes/no)?: ").lower()
    if(ch!='yes'):
        break
