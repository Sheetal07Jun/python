import pyautogui as pt
import time
time.sleep(3)
count=0
while count<=50:
    pt.typewrite("hello ")
    pt.press("enter")
    count=count+1

   
