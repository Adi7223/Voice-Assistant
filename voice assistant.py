import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import json

engine=pyttsx3.init()
engine.setProperty('rate', 190)

def load_data(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data

data = load_data('C:\\Users\\Aditya\\Desktop\\Study\\prog\\Voice assistant\\data.json')

def takecommand():
 print("Listening....")
 r=sr.Recognizer()
 with sr.Microphone() as source:
  r.pause_threshold = 1
  audio=r.listen(source)
  try:
   query=r.recognize_google(audio, language = "en-in")
   print(f"User said : {query}")
   return query
  except Exception as e:
   return "Some Error Occured"

if __name__=='__main__':
 engine.say('hello, I am Victas')
 engine.runAndWait()
#  print("Listening....")
 while True:
  query=takecommand()
#   sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"]
#         ,["google","https://www.google.com"]]
#   for site in sites:
#    if f"Open {site[0]}".lower() in query.lower():
#     webbrowser.open(site[1])
#     engine.say(f"Opening {site[0]} sir...")
#     engine.runAndWait()
    # engine.say(query)
#    if f"Open Photos".lower() in query.lower():
#     os.system('start ms-photos:')
#    if f"Open whatsapp".lower() in query.lower():
#     os.system('start whatsapp:')
#    if f"Open spotify".lower() in query.lower():
#     os.system('start spotify:')

  for site in data["websites"]:
            if f"Open {site['name']}".lower() in query.lower():
                webbrowser.open(site['command'])
                engine.say(f"Opening {site['name']} sir...")
                engine.runAndWait()
                break

#   apps=[["whatsapp","whatsapp:"],["spotify","spotify:"]
#         ,["photos","ms-photos:"]]
#   for app in apps:
#    if f"Open {app[0]}".lower() in query.lower():
#     os.system( f'start {app[1]}')
#     engine.say(f"Opening {app[0]} sir...")
#     engine.runAndWait()

  for app in data["apps"]:
            if f"Open {app['name']}".lower() in query.lower():
                os.system(f'start {app["command"]}')
                engine.say(f"Opening {app['name']} sir...")
                engine.runAndWait()
                break
  

   
