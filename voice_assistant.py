# ==== Importing all the necessary libraries
import speech_recognition as sr

import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk


# ==== Class Assistant
class assistance_gui:
    def __init__(self,root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="frame_image.jpg")
        bg = Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="background.png")
        left = Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

        # ====start button
        start = Button(self.root, text='START', font = ("times new roman", 14), command=self.start_option).place(x=150, y=520)

        # ====close button
        close = Button(self.root, text='CLOSE', font = ("times new roman", 14), command=self.close_window).place(x=350, y=520)

    # ==== start assitant
    def start_option(self):
        listener = sr.Recognizer()
        # engine = pyttsx3.init()

        # ==== Voice Control
        def speak(text):
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()

        # ====Default Start
        def start():
            # ==== Wish Start
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                wish = "Good Morning!"
            elif hour >= 12 and hour < 18:
                wish = "Good Afternoon!"
            else:
                wish = "Good Evening!"
            speak('Hello ,' + wish+' I am your voice assistant. Please tell me how may I help you')
            # ==== Wish End

        # ==== Take Command
        def take_command():
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = listener.listen(data_taker)
                    instruction = listener.recognize_google(voice)
                    instruction = instruction.lower()
                    return instruction
            except:
                pass

        # ==== Run command
        def run_command():
            instruction = take_command() 
            print(instruction)
            # speak(instruction)
            try:
                if 'who are you' in instruction:
                    
                    speak('I am your personal voice Assistant')

                elif 'what can you do for me' in instruction:
                    speak('I can play songs, tell time, and help you go with wikipedia')

                elif 'current time' in instruction:
                    time = datetime.datetime.now().strftime('%I: %M %p')
                    print(time)
            

                    # engine.say(time)
                    # engine.runAndWait()

                    speak('current time is' + time)

                elif 'open google' in instruction:
                
                    speak('Opening Google')
                  
                    webbrowser.open('google.com')

                elif 'open youtube' in instruction:
                    speak('Opening Youtube')
                    webbrowser.open('youtube.com')

                elif 'open facebook' in instruction:
                    speak('Opening Facebook')
                    webbrowser.open('facebook.com')

                # elif 'open python geeks' in instruction:
                #     speak('Opening PythonGeeks')
                #     webbrowser.open('pythongeeks.org')

                elif 'open linkedin' in instruction:
                    speak('Opening Linkedin')
                    webbrowser.open('linkedin.com')

                elif 'open gmail' in instruction:
                    speak('Opening Gmail')
                    webbrowser.open('gmail.com')

                # elif 'open stack overflow' in instruction:
                #     speak('Opening Stack Overflow')
                #     webbrowser.open('stackoverflow.com')

                elif 'shutdown' in instruction:
                    speak('I am shutting down')
                    self.close_window()
                    return False
                # else:
                #     speak('I did not understand, can you repeat again')
            except:
                speak('Waiting for your response')
            return True

        # ====Default Start calling
        start()

        # ====To run assistance continuously
        while True:
            if run_command():
                run_command()
            else:
                break


    # ==== Close window
    def close_window(self):
        self.root.destroy()



# ==== create tkinter window
root = Tk()


# === creating object for class
obj=assistance_gui(root)

# ==== start the gui
root.mainloop()


# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# from PIL import ImageTk, Image

# class assistance_gui:
#     def __init__(self, root):  # THIS LINE IS CRUCIAL - ADD THIS METHOD
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')
        
#         # Use simple background without external images
#         self.bg_color = "lightblue"
#         self.center_color = "white"
        
#         bg = Label(self.root, bg=self.bg_color)
#         bg.place(x=0, y=0, relwidth=1, relheight=1)
        
#         center = Label(self.root, bg=self.center_color, text="Voice Assistant", 
#                       font=("Arial", 16))
#         center.place(x=100, y=100, width=400, height=400)

#         # Start button
#         start = Button(self.root, text='START', font=("Arial", 14), 
#                       command=self.start_option, bg="green", fg="white")
#         start.place(x=150, y=520)

#         # Close button
#         close = Button(self.root, text='CLOSE', font=("Arial", 14), 
#                       command=self.close_window, bg="red", fg="white")
#         close.place(x=350, y=520)

#     def start_option(self):
#         # Your assistant code will go here
#         print("Voice assistant started!")
        
#     def close_window(self):
#         self.root.destroy()

# # === create tkinter window
# root = Tk()
# # === creating object for class
# obj = assistance_gui(root)
# # === start the gui
# root.mainloop()




# # ==== Importing all the necessary libraries
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# from PIL import ImageTk, Image
# import time

# # ==== Class Assistant
# class assistance_gui:
#     def __init__(self, root):  # Added self parameter
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')

#         # Use simple background if images aren't available
#         try:
#             self.bg = ImageTk.PhotoImage(Image.open("background.png"))
#             bg_label = Label(self.root, image=self.bg)
#             bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
#             self.centre = ImageTk.PhotoImage(Image.open("frame_image.jpg"))
#             center_label = Label(self.root, image=self.centre)
#             center_label.place(x=100, y=100, width=400, height=400)
#         except:
#             # Fallback background
#             bg_label = Label(self.root, bg="lightblue")
#             bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
#             center_label = Label(self.root, bg="white", text="Voice Assistant", 
#                                font=("Arial", 16))
#             center_label.place(x=100, y=100, width=400, height=400)

#         # ====start button
#         start = Button(self.root, text='START', font=("Arial", 14), 
#                       command=self.start_option, bg="green", fg="white")
#         start.place(x=150, y=520)

#         # ====close button
#         close = Button(self.root, text='CLOSE', font=("Arial", 14), 
#                       command=self.close_window, bg="red", fg="white")
#         close.place(x=350, y=520)

#     # ==== start assistant
#     def start_option(self):
#         listener = sr.Recognizer()
#         engine = pyttsx3.init()
        
#         # Set voice properties for better sound
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
#         engine.setProperty('rate', 150)  

#         # ==== Voice Control
#         def speak(text):
#             engine.say(text)
#             engine.runAndWait()

#         # ====Default Start
#         def start():
#             # ==== Wish Start
#             hour = int(datetime.datetime.now().hour)
#             if hour >= 0 and hour < 12:
#                 wish = "Good Morning!"
#             elif hour >= 12 and hour < 18:
#                 wish = "Good Afternoon!"
#             else:
#                 wish = "Good Evening!"
#             speak('Hello Sir, ' + wish + ' I am your voice assistant. Please tell me how may I help you')
#             # ==== Wish End

#         # ==== Take Command
#         def take_command():
#             try:
#                 with sr.Microphone() as data_taker:
#                     print("Listening... Speak now")
#                     listener.adjust_for_ambient_noise(data_taker, duration=1)
#                     voice = listener.listen(data_taker, timeout=5)
#                     instruction = listener.recognize_google(voice)
#                     instruction = instruction.lower()
#                     print("You said:", instruction)
#                     return instruction
#             except sr.UnknownValueError:
#                 print("Could not understand audio")
#                 return ""
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")
#                 return ""
#             except Exception as e:
#                 print(f"Error: {e}")
#                 return ""

#         # ==== Run command
#         def run_command():
#             instruction = take_command()
#             if not instruction:
#                 return True
                
#             try:
#                 if 'who are you' in instruction:
#                     speak('I am your personal voice Assistant')

#                 elif 'what can you do for me' in instruction:
#                     speak('I can open websites like Google, YouTube, Facebook, and more. I can also tell you the current time.')

#                 elif 'current time' in instruction or 'time' in instruction:
#                     current_time = datetime.datetime.now().strftime('%I:%M %p')
#                     speak(f'Current time is {current_time}')

#                 elif 'open google' in instruction:
#                     speak('Opening Google')
#                     webbrowser.open('https://www.google.com')

#                 elif 'open youtube' in instruction:
#                     speak('Opening Youtube')
#                     webbrowser.open('https://www.youtube.com')

#                 elif 'open facebook' in instruction:
#                     speak('Opening Facebook')
#                     webbrowser.open('https://www.facebook.com')

#                 elif 'open python geeks' in instruction:
#                     speak('Opening PythonGeeks')
#                     webbrowser.open('https://pythongeeks.org')

#                 elif 'open linkedin' in instruction:
#                     speak('Opening Linkedin')
#                     webbrowser.open('https://linkedin.com')

#                 elif 'open gmail' in instruction:
#                     speak('Opening Gmail')
#                     webbrowser.open('https://mail.google.com')

#                 elif 'open stack overflow' in instruction:
#                     speak('Opening Stack Overflow')
#                     webbrowser.open('https://stackoverflow.com')
                    
#                 elif 'open amazon' in instruction:
#                     speak('Opening Amazon')
#                     webbrowser.open('https://www.amazon.com')
                    
#                 elif 'open wikipedia' in instruction:
#                     speak('Opening Wikipedia')
#                     webbrowser.open('https://www.wikipedia.org')

#                 elif 'shutdown' in instruction or 'exit' in instruction or 'quit' in instruction:
#                     speak('I am shutting down')
#                     return False
                    
#                 else:
#                     speak('I did not understand, can you repeat again')
                    
#             except Exception as e:
#                 print(f"Error: {e}")
#                 speak('Sorry, I encountered an error')
                
#             return True

#         # ====Default Start calling
#         start()

#         # ====To run assistance continuously
#         while True:
#             if not run_command():
#                 break
#             time.sleep(1)  # Small delay between commands

#     # ==== Close window
#     def close_window(self):
#         self.root.destroy()

# # ==== create tkinter window
# root = Tk()

# # === creating object for class
# obj = assistance_gui(root)

# # ==== start the gui
# root.mainloop()



# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# from PIL import ImageTk

# class AssistanceGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')

#         # Background and frame images
#         self.bg = ImageTk.PhotoImage(file="background.png")
#         Label(self.root, image=self.bg).place(x=0, y=0)

#         self.centre = ImageTk.PhotoImage(file="frame_image.jpg")
#         Label(self.root, image=self.centre).place(x=100, y=100, width=400, height=400)

#         Button(self.root, text='START', font=("times new roman", 14), command=self.start_option).place(x=150, y=520)
#         Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window).place(x=350, y=520)

#     def start_option(self):
#         listener = sr.Recognizer()
#         engine = pyttsx3.init()

#         def speak(text):
#             engine.say(text)
#             engine.runAndWait()

#         def wish():
#             hour = datetime.datetime.now().hour
#             if hour < 12:
#                 speak("Good Morning!")
#             elif hour < 18:
#                 speak("Good Afternoon!")
#             else:
#                 speak("Good Evening!")

#         def take_command():
#             try:
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                     audio = listener.listen(source)
#                     instruction = listener.recognize_google(audio).lower()
#                     return instruction
#             except Exception as e:
#                 print(f"Error: {e}")
#                 return ""

#         def run_command():
#             instruction = take_command()
#             print("You said:", instruction)

#             if 'who are you' in instruction:
#                 speak('I am your personal voice assistant.')
#             elif 'what can you do' in instruction:
#                 speak('I can open websites, tell time, and more.')
#             elif 'current time' in instruction:
#                 time_str = datetime.datetime.now().strftime('%I:%M %p')
#                 speak(f'Current time is {time_str}')
#             elif 'open google' in instruction:
#                 speak('Opening Google')
#                 webbrowser.open('https://www.google.com', new=2)
#             elif 'open youtube' in instruction:
#                 speak('Opening YouTube')
#                 webbrowser.open('https://www.youtube.com', new=2)
#             elif 'open facebook' in instruction:
#                 speak('Opening Facebook')
#                 webbrowser.open('https://www.facebook.com', new=2)
#             elif 'open gmail' in instruction:
#                 speak('Opening Gmail')
#                 webbrowser.open('https://mail.google.com', new=2)
#             elif 'shutdown' in instruction or 'close' in instruction:
#                 speak('Shutting down. Goodbye!')
#                 self.close_window()
#                 return False
#             else:
#                 speak('I did not understand that. Please repeat.')
#             return True

#         speak('Hello Sir,')
#         wish()
#         speak('I am your voice assistant. How may I help you?')

#         while True:
#             if not run_command():
#                 break

#     def close_window(self):
#         self.root.destroy()

# if __name__ == '__main__':
#     root = Tk()
#     app = AssistanceGUI(root)
#     root.mainloop()


# # ==== Importing all the necessary libraries
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# from PIL import ImageTk, Image
# import time
# import threading

# # ==== Class Assistant
# class assistance_gui:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')

#         # Status label to show what's happening
#         self.status_label = Label(self.root, text="Ready", font=("Arial", 12), fg="blue")
#         self.status_label.place(x=300, y=480, anchor=CENTER)

#         # Use simple background
#         bg_label = Label(self.root, bg="lightblue")
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
#         center_label = Label(self.root, bg="white", text="Voice Assistant\n\nClick START to begin", 
#                            font=("Arial", 16), justify=CENTER)
#         center_label.place(x=100, y=100, width=400, height=400)

#         # ====start button
#         start = Button(self.root, text='START', font=("Arial", 14), 
#                       command=self.start_option, bg="green", fg="white")
#         start.place(x=150, y=520)

#         # ====close button
#         close = Button(self.root, text='CLOSE', font=("Arial", 14), 
#                       command=self.close_window, bg="red", fg="white")
#         close.place(x=350, y=520)
        
#     def update_status(self, message):
#         self.status_label.config(text=message)
#         self.root.update()

#     # ==== start assistant
#     def start_option(self):
#         # Run the assistant in a separate thread to prevent GUI freezing
#         thread = threading.Thread(target=self.run_assistant)
#         thread.daemon = True
#         thread.start()

#     def run_assistant(self):
#         self.update_status("Initializing...")
#         listener = sr.Recognizer()
#         engine = pyttsx3.init()
        
#         # Set voice properties for better sound
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[0].id)
#         engine.setProperty('rate', 150)

#         # ==== Voice Control
#         def speak(text):
#             self.update_status("Speaking: " + text)
#             engine.say(text)
#             engine.runAndWait()
#             self.update_status("Listening...")

#         # ====Default Start
#         def start():
#             # ==== Wish Start
#             hour = int(datetime.datetime.now().hour)
#             if hour >= 0 and hour < 12:
#                 wish = "Good Morning!"
#             elif hour >= 12 and hour < 18:
#                 wish = "Good Afternoon!"
#             else:
#                 wish = "Good Evening!"
#             speak('Hello Sir, ' + wish + ' I am your voice assistant. Please tell me how may I help you')

#         # ==== Take Command
#         def take_command():
#             try:
#                 self.update_status("Listening... Speak now")
#                 with sr.Microphone() as source:
#                     # Adjust for ambient noise and set timeout
#                     listener.adjust_for_ambient_noise(source, duration=1)
#                     print("Listening... (speak now)")
#                     audio = listener.listen(source, timeout=5, phrase_time_limit=5)
                    
#                 self.update_status("Processing...")
#                 instruction = listener.recognize_google(audio)
#                 instruction = instruction.lower()
#                 print("You said:", instruction)
#                 return instruction
                
#             except sr.UnknownValueError:
#                 self.update_status("Could not understand audio")
#                 return ""
#             except sr.RequestError as e:
#                 self.update_status("Error with speech service")
#                 print(f"Could not request results; {e}")
#                 return ""
#             except sr.WaitTimeoutError:
#                 self.update_status("No speech detected")
#                 return ""
#             except Exception as e:
#                 self.update_status("Error occurred")
#                 print(f"Error: {e}")
#                 return ""

#         # ==== Run command
#         def run_command():
#             instruction = take_command()
#             if not instruction:
#                 return True
                
#             try:
#                 if 'who are you' in instruction:
#                     speak('I am your personal voice Assistant')

#                 elif 'what can you do' in instruction:
#                     speak('I can open websites like Google, YouTube, Facebook, and more')

#                 elif 'time' in instruction:
#                     current_time = datetime.datetime.now().strftime('%I:%M %p')
#                     speak(f'Current time is {current_time}')

#                 elif 'open google' in instruction:
#                     speak('Opening Google right now')
#                     webbrowser.open('https://www.google.com')
#                     return True

#                 elif 'open youtube' in instruction:
#                     speak('Opening YouTube')
#                     webbrowser.open('https://www.youtube.com')
#                     return True

#                 elif 'open facebook' in instruction:
#                     speak('Opening Facebook')
#                     webbrowser.open('https://www.facebook.com')
#                     return True

#                 elif 'open gmail' in instruction:
#                     speak('Opening Gmail')
#                     webbrowser.open('https://mail.google.com')
#                     return True

#                 elif 'open amazon' in instruction:
#                     speak('Opening Amazon')
#                     webbrowser.open('https://www.amazon.com')
#                     return True

#                 elif 'open wikipedia' in instruction:
#                     speak('Opening Wikipedia')
#                     webbrowser.open('https://www.wikipedia.org')
#                     return True

#                 elif 'shutdown' in instruction or 'exit' in instruction or 'quit' in instruction:
#                     speak('Goodbye! Shutting down')
#                     return False
                    
#                 else:
#                     speak('I did not understand that command. Please try again.')
                    
#             except Exception as e:
#                 print(f"Error: {e}")
#                 speak('Sorry, I encountered an error')
                
#             return True

#         # ====Default Start calling
#         start()

#         # ====To run assistance continuously
#         self.update_status("Ready for commands")
#         while True:
#             if not run_command():
#                 break
#             time.sleep(1)  # Small delay between commands

#     # ==== Close window
#     def close_window(self):
#         self.root.destroy()

# # ==== create tkinter window
# if __name__ == "__main__":
#     root = Tk()
#     obj = assistance_gui(root)
#     root.mainloop()


# # ==== Importing all the necessary libraries
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# import time
# import threading

# # ==== Class Assistant
# class assistance_gui:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')

#         # Status label to show what's happening
#         self.status_label = Label(self.root, text="Ready", font=("Arial", 12), fg="blue")
#         self.status_label.place(x=300, y=450, anchor=CENTER)
        
#         # Command label to show what was heard
#         self.command_label = Label(self.root, text="Heard: ", font=("Arial", 10), fg="green")
#         self.command_label.place(x=300, y=480, anchor=CENTER)

#         # Use simple background
#         bg_label = Label(self.root, bg="lightblue")
#         bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
#         center_label = Label(self.root, bg="white", text="Voice Assistant\n\nClick START to begin\n\nSay 'open google' to test", 
#                            font=("Arial", 16), justify=CENTER)
#         center_label.place(x=100, y=100, width=400, height=300)

#         # ====start button
#         self.start_button = Button(self.root, text='START', font=("Arial", 14), 
#                       command=self.start_option, bg="green", fg="white")
#         self.start_button.place(x=150, y=520)

#         # ====close button
#         close = Button(self.root, text='CLOSE', font=("Arial", 14), 
#                       command=self.close_window, bg="red", fg="white")
#         close.place(x=350, y=520)
        
#     def update_status(self, message):
#         self.status_label.config(text=message)
#         self.root.update()
        
#     def update_command(self, message):
#         self.command_label.config(text="Heard: " + message)
#         self.root.update()

#     # ==== start assistant
#     def start_option(self):
#         # Disable start button during operation
#         self.start_button.config(state=DISABLED)
#         # Run the assistant in a separate thread to prevent GUI freezing
#         thread = threading.Thread(target=self.run_assistant)
#         thread.daemon = True
#         thread.start()

#     def run_assistant(self):
#         self.update_status("Initializing microphone...")
        
#         # Test if microphone works
#         try:
#             listener = sr.Recognizer()
#             with sr.Microphone() as source:
#                 listener.adjust_for_ambient_noise(source, duration=1)
#             self.update_status("Microphone ready")
#         except Exception as e:
#             self.update_status(f"Microphone error: {str(e)}")
#             self.start_button.config(state=NORMAL)
#             return
            
#         engine = pyttsx3.init()
        
#         # Set voice properties for better sound
#         try:
#             voices = engine.getProperty('voices')
#             engine.setProperty('voice', voices[0].id)
#             engine.setProperty('rate', 150)
#         except:
#             pass

#         # ==== Voice Control
#         def speak(text):
#             self.update_status("Speaking: " + text)
#             try:
#                 engine.say(text)
#                 engine.runAndWait()
#                 self.update_status("Ready for command")
#             except:
#                 print("Text-to-speech error")

#         # ====Default Start
#         def start_assistant():
#             # ==== Wish Start
#             hour = int(datetime.datetime.now().hour)
#             if hour >= 0 and hour < 12:
#                 wish = "Good Morning!"
#             elif hour >= 12 and hour < 18:
#                 wish = "Good Afternoon!"
#             else:
#                 wish = "Good Evening!"
#             speak('Hello, ' + wish + ' I am your voice assistant. Please tell me how may I help you')

#         # ==== Take Command
#         def take_command():
#             try:
#                 self.update_status("Listening... Speak now")
#                 with sr.Microphone() as source:
#                     # Adjust for ambient noise and set timeout
#                     listener.adjust_for_ambient_noise(source, duration=1)
#                     print("Listening... (speak now)")
#                     audio = listener.listen(source, timeout=5, phrase_time_limit=5)
                    
#                 self.update_status("Processing...")
#                 instruction = listener.recognize_google(audio)
#                 instruction = instruction.lower()
#                 print("You said:", instruction)
#                 self.update_command(instruction)  # Show what was heard
#                 return instruction
                
#             except sr.UnknownValueError:
#                 self.update_status("Could not understand audio")
#                 self.update_command("Could not understand")
#                 return ""
#             except sr.RequestError as e:
#                 self.update_status("Error with speech service")
#                 self.update_command("Service error")
#                 print(f"Could not request results; {e}")
#                 return ""
#             except sr.WaitTimeoutError:
#                 self.update_status("No speech detected")
#                 self.update_command("No speech detected")
#                 return ""
#             except Exception as e:
#                 self.update_status("Error occurred")
#                 self.update_command(f"Error: {str(e)}")
#                 print(f"Error: {e}")
#                 return ""

#         # ==== Run command
#         def run_command():
#             instruction = take_command()
#             if not instruction:
#                 return True
                
#             try:
#                 # SIMPLIFIED COMMAND RECOGNITION - JUST FOR TESTING
#                 if 'google' in instruction:
#                     speak('Opening Google right now')
#                     webbrowser.open('https://www.google.com')
#                     return True
                    
#                 elif 'youtube' in instruction:
#                     speak('Opening YouTube')
#                     webbrowser.open('https://www.youtube.com')
#                     return True
                    
#                 elif 'time' in instruction:
#                     current_time = datetime.datetime.now().strftime('%I:%M %p')
#                     speak(f'Current time is {current_time}')
#                     return True
                    
#                 elif 'shutdown' in instruction or 'exit' in instruction or 'quit' in instruction:
#                     speak('Goodbye! Shutting down')
#                     return False
                    
#                 else:
#                     speak('I did not understand that command. Please try saying google, youtube, or time.')
#                     return True
                    
#             except Exception as e:
#                 print(f"Error: {e}")
#                 speak('Sorry, I encountered an error')
#                 return True

#         # ====Default Start calling
#         start_assistant()

#         # ====To run assistance continuously
#         self.update_status("Ready for commands - Say 'google'")
#         for i in range(10):  # Only try 10 times to prevent infinite loop
#             if not run_command():
#                 break
#             time.sleep(1)  # Small delay between commands
        
#         # Re-enable start button when done
#         self.start_button.config(state=NORMAL)
#         self.update_status("Ready - Click START to try again")

#     # ==== Close window
#     def close_window(self):
#         self.root.destroy()

# # ==== Test if webbrowser works independently
# def test_webbrowser():
#     print("Testing webbrowser...")
#     try:
#         webbrowser.open('https://www.google.com')
#         print("Webbrowser test successful!")
#         return True
#     except Exception as e:
#         print(f"Webbrowser test failed: {e}")
#         return False

# # ==== create tkinter window
# if __name__ == "__main__":
#     print("Starting voice assistant...")
    
#     # First test if webbrowser works
#     if test_webbrowser():
#         root = Tk()
#         obj = assistance_gui(root)
#         root.mainloop()
#     else:
#         print("Webbrowser is not working. Please check your default browser settings.")
#         input("Press Enter to exit...")


# # ==== Importing all the necessary libraries
# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# from PIL import ImageTk, Image
# import os

# # ==== Class Assistant
# class assistance_gui:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')
        
#         # Initialize the speech engine
#         self.engine = pyttsx3.init()
        
#         # Set up background images (using placeholder paths)
#         try:
#             self.bg = ImageTk.PhotoImage(Image.open("background.png").resize((600, 600), Image.LANCZOS))
#             bg_label = Label(self.root, image=self.bg)
#             bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#         except:
#             # Fallback if image not found
#             self.root.configure(bg='lightblue')
        
#         try:
#             self.centre = ImageTk.PhotoImage(Image.open("frame_image.jpg").resize((400, 400), Image.LANCZOS))
#             centre_label = Label(self.root, image=self.centre)
#             centre_label.place(x=100, y=100)
#         except:
#             # Fallback if image not found
#             pass

#         # ====start button
#         start = Button(self.root, text='START', font=("times new roman", 14), 
#                       command=self.start_option, bg='green', fg='white')
#         start.place(x=150, y=520)

#         # ====close button
#         close = Button(self.root, text='CLOSE', font=("times new roman", 14), 
#                       command=self.close_window, bg='red', fg='white')
#         close.place(x=350, y=520)

#     # ==== Voice Control
#     def speak(self, text):
#         self.engine.say(text)
#         self.engine.runAndWait()  # This ensures speech completes before continuing

#     # ==== start assistant
#     def start_option(self):
#         listener = sr.Recognizer()

#         # ====Default Start
#         def start_assistant():
#             # ==== Wish Start
#             hour = datetime.datetime.now().hour
#             if 0 <= hour < 12:
#                 wish = "Good Morning!"
#             elif 12 <= hour < 18:
#                 wish = "Good Afternoon!"
#             else:
#                 wish = "Good Evening!"
#             self.speak('Hello Sir, ' + wish + ' I am your voice assistant. Please tell me how may I help you')
#             # ==== Wish End

#         # ==== Take Command
#         def take_command():
#             try:
#                 with sr.Microphone() as data_taker:
#                     print("Listening...")
#                     self.speak("I'm listening")
#                     voice = listener.listen(data_taker, timeout=5)
#                     instruction = listener.recognize_google(voice)
#                     instruction = instruction.lower()
#                     print("You said:", instruction)
#                     return instruction
#             except sr.WaitTimeoutError:
#                 self.speak("I didn't hear anything, please try again")
#                 return ""
#             except sr.UnknownValueError:
#                 self.speak("Sorry, I didn't understand that")
#                 return ""
#             except Exception as e:
#                 print("Error:", e)
#                 self.speak("There was an error with the microphone")
#                 return ""

#         # ==== Run command
#         def run_command():
#             instruction = take_command()
#             if not instruction:
#                 return True
                
#             print("Command:", instruction)
#             try:
#                 if 'who are you' in instruction:
#                     self.speak('I am your personal voice Assistant')

#                 elif 'what can you do for me' in instruction:
#                     self.speak('I can play songs, tell time, and help you go with wikipedia')

#                 elif 'current time' in instruction or 'time now' in instruction or 'what time is it' in instruction:
#                     now = datetime.datetime.now()
#                     time_str = now.strftime('%I:%M %p')
#                     self.speak(f'The current time is {time_str}')

#                 elif 'open google' in instruction:
#                     self.speak('Opening Google')
#                     webbrowser.open('https://www.google.com')

#                 elif 'open youtube' in instruction:
#                     self.speak('Opening Youtube')
#                     webbrowser.open('https://www.youtube.com')

#                 elif 'open facebook' in instruction:
#                     self.speak('Opening Facebook')
#                     webbrowser.open('https://www.facebook.com')

#                 elif 'open python geeks' in instruction:
#                     self.speak('Opening PythonGeeks')
#                     webbrowser.open('https://pythongeeks.org')

#                 elif 'open linkedin' in instruction:
#                     self.speak('Opening Linkedin')
#                     webbrowser.open('https://linkedin.com')

#                 elif 'open gmail' in instruction:
#                     self.speak('Opening Gmail')
#                     webbrowser.open('https://gmail.com')

#                 elif 'open stack overflow' in instruction:
#                     self.speak('Opening Stack Overflow')
#                     webbrowser.open('https://stackoverflow.com')

#                 elif 'shutdown' in instruction or 'exit' in instruction or 'stop' in instruction:
#                     self.speak('I am shutting down')
#                     self.close_window()
#                     return False
#                 else:
#                     self.speak('I did not understand, can you repeat again')
#             except Exception as e:
#                 print("Error executing command:", e)
#                 self.speak('There was an error executing your command')
#             return True

#         # ====Default Start calling
#         start_assistant()

#         # ====To run assistance continuously
#         while True:
#             if not run_command():
#                 break

#     # ==== Close window
#     def close_window(self):
#         self.root.destroy()

# # ==== create tkinter window
# if __name__ == "__main__":
#     root = Tk()
#     # === creating object for class
#     obj = assistance_gui(root)
#     # ==== start the gui
#     root.mainloop()



# import speech_recognition as sr
# import pyttsx3
# import webbrowser
# import datetime
# from tkinter import *
# from PIL import ImageTk, Image

# # Initialize the text to speech engine
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# class assistance_gui:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Voice Assistant")
#         self.root.geometry('600x600')

#         self.bg = ImageTk.PhotoImage(Image.open("background.png"))
#         bg = Label(self.root, image=self.bg)
#         bg.place(x=0, y=0, relwidth=1, relheight=1)

#         self.centre = ImageTk.PhotoImage(Image.open("frame_image.jpg"))
#         left = Label(self.root, image=self.centre)
#         left.place(x=150, y=150, width=300, height=250)

#         # === start button
#         start = Button(self.root, text="START", command=self.start_option)
#         start.place(x=150, y=450, width=100, height=40)

#         # === close button
#         close = Button(self.root, text="CLOSE", command=root.destroy)
#         close.place(x=350, y=450, width=100, height=40)

#     def start_option(self):
#         listener = sr.Recognizer()
#         try:
#             with sr.Microphone() as source:
#                 speak("Listening...")
#                 listener.pause_threshold = 1
#                 audio = listener.listen(source)

#                 query = listener.recognize_google(audio, language='en-in')
#                 query = query.lower()
#                 print(f"User said: {query}")

#                 if "open gmail" in query:
#                     webbrowser.open("https://mail.google.com")
#                     speak("Opening Gmail")

#                 elif "time" in query:
#                     str_time = datetime.datetime.now().strftime("%H:%M:%S")
#                     speak(f"The current time is {str_time}")

#                 else:
#                     speak("Sorry, I didn't get that")
#         except Exception as e:
#             print("Error: ", e)
#             speak("Sorry, I could not understand. Please try again.")

# if __name__ == "__main__":
#     root = Tk()
#     obj = assistance_gui(root)
#     root.mainloop()





