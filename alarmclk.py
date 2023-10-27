from playsound import playsound
from datetime import datetime

txt=input("Set the Time of the alarm: HH:MM:SS:AM/PM\n ")
hour=txt[0:2]
min=txt[3:5]
sec=txt[6:8]
period=txt[9:11].upper()
print("Setting up alarm.. will be turn on at {}:{}:{}:{}".format(hour,min,sec,period))
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")
    if(period==current_period):
        if(hour==current_hour):
            if(min==current_min):
                if(sec==current_sec):
                    print("Get Up!")
                    playsound('audio.mp3')
                    break