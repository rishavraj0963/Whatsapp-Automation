# pip install pyautogui <-- python library which we can use to automate our mouse and keyboard actions
import webbrowser  #Built-In library that I will use to open link in browser(here - whatsapp web)
import pyautogui
import time #we can apply some delay using this library
from datetime import datetime # we will use this module to fetch current time
import numpy as np

def seconds_cal(end_hh, end_mm): #calculating seconds from current time --to--> time of delever the message
    minutes = 0
    current = datetime.now()
    start_hh = current.hour
    start_mm = current.minute
    if end_hh > start_hh:
        minutes += ((end_hh-start_hh-1)*60) + (60-start_mm) + end_mm
    elif end_hh == start_hh and end_mm > start_mm:
        minutes += end_mm - start_mm
    else:
        minutes += ((23-start_hh)*60) + (60-start_mm) + (end_hh*60) + end_mm
    return minutes*60-current.second

person_name = input('Enter person name to Message : ')
message = input('Enter what you want to send : ')
cnt = int(input('How many times you want to send message : '))
hh, mm = input('Enter time when to send message (HH:MM) : ').split(':')
hh = int(hh)
mm = int(mm)
delay_time = seconds_cal(hh, mm)
print('Your message will be delever at ',hh,':',mm,',after',delay_time,'seconds.')
time.sleep(delay_time)

webbrowser.open('https://web.whatsapp.com/')
time.sleep(15) #Waiting 15sec. to open whatsapp in browser

#For finding position of any coordinate we use ----> print(pyautogui.position())
#search for person
#pyautogui.click(177, 211) #(333, 253) is position of search bar in whatsapp
for i in range(4):
    pyautogui.press('tab')

pyautogui.typewrite(person_name) #We will put the name of person in the search bar
time.sleep(1) #After writing person name in search bar we have to wait a little to get search result
pyautogui.press('down') #we will go to first suggested person
#pyautogui.click(969, 961) #(812, 980) is position of Chatting bar, where we want to type the message
time.sleep(1)
for i in range(6):
    pyautogui.press('tab')

#pyautogui.hotkey('ctrl', 'v', interval = 0.15)
#time.sleep(2)
#pyautogui.press('enter')
time.sleep(1)
for x in range(cnt):
    pyautogui.write(message, interval=0.001)  # We will put the message in the chatting bar with the time interval of 0.02sec
    pyautogui.press('enter')  # sending message by pressing enter