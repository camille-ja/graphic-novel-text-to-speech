import pyautogui
import pyscreeze
pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False


print("start")

res = pyautogui.locateOnScreen("edit.png") #left = x, top = y
print(res)
#edit_but = pyautogui.center(res) #center coordinates
#pyautogui.locateCenterOnScreen("edit.png") #does the same thing^

#pyautogui.moveTo(edit_but) #moves the mouse!

channel_name = pyautogui.prompt(text="", title="Enter channel name") #takes inputs while minimizing vscode
print(channel_name)

pyautogui.hotkey("ctrl","t") #doesn't work if you're alr in a new tab!
pyautogui.sleep(1)
pyautogui.write("https://www.youtube.com/") #just minimize vscode and it should work
pyautogui.hotkey("enter")

pyautogui.sleep(5)
print("awake")
search_loc = pyautogui.locateCenterOnScreen("search.png")
print(search_loc)
pyautogui.moveTo(search_loc)
pyautogui.click()
pyautogui.write(channel_name)
pyautogui.hotkey("enter")
pyautogui.sleep(5)
subscribe = pyautogui.locateCenterOnScreen("subscribe.png")
print(subscribe)


pyautogui.moveTo(subscribe)
#pyautogui.hotkey("enter")
pyautogui.rightClick()

print("done")