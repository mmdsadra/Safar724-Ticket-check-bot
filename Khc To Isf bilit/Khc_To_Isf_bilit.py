from ast import Delete
from enum import Flag
from winsound import PlaySound
from selenium import webdriver
import re
import time
emptysit = False


options = webdriver.ChromeOptions()
options.page_load_strategy = 'none'

print('Please turn on your VPN and make sure your telegram is connected.')
print('Make sure that you have chrome web driver!')
y = input('enter year:')
m = input('enter month:')
d = input('enter day:') 
global stime
stime = input('enter sleep time (recommand +60):')
global date
date = y + '-' + m + '-' + d

def app():
# Load the webpage
    
    #driver = webdriver.Chrome(options=options)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get('https://safar724.com/bus/khvansar-esfahan?date=%s' %date)

# Wait for the page to load (you might need to adjust the sleep time)
    time.sleep(float(stime))
# Get the page source after it's loaded
    page_source = driver.page_source

# Print or use the page source as needed
    for item in re.findall(r'<p>(\d+)<span>صندلی خالی<\/span><\/p>', page_source):
        print(item)
        if(not(item == "۰>")):
            global emptysit
            emptysit = True
            print("its okey")
    driver.quit()

def call():
    ids = ['']
    for id in ids:
        driver = webdriver.Chrome(options=options)
        driver.get('https://api.telegram.org/BotTOCKEN/sendMessage?chat_id=%s&text=bilit %s' %(id, date))
        time.sleep(8)
        driver.quit()

def playBeep():
    
    import playsound3
    PlaySound('beep.wav',flags=True)

def check ():
    if(emptysit):
        playBeep()
        call()
        call()
        call()
    else:
        app()
        check()


check()