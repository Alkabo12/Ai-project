from scrapetube import *
import pandas as pd
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
from bs4 import BeautifulSoup
import requests
from pytube import YouTube
import os
import shutil
from os import path
#import bidi.algorithm
import os


def scrape_info(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")
    title = s.getText("span").split("-")
    return title[0]
      
channelid =input("Please Enter the youtube channel Link :")
list=[]
titles=[]
paths=[]
url ="https://www.youtube.com/watch?v="
vedeos=scrapetube.get_channel(None,channelid)
for vedeo in vedeos:
    url1=url+str(vedeo['videoId'])
    print(url1)
    yt = YouTube(url1)
    video = yt.streams.get_highest_resolution()
    video.download()
    paths.append(video.get_file_path())
    list.append(url1)
    titles.append(scrape_info(url1))
print("Paths Of All Videos \n")
for i in range (len(paths)):
    print(str(paths[i]))
print("Get All Videos Compelete!")


url = 'https://www.facebook.com/login.php'
class FacebookLogin():
    def __init__(self, email, password, browser):

        self.email = email
        self.password = password

        if browser == 'Chrome':
            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        self.driver.get(url)
        time.sleep(1)

    def login(self):
        email_element = self.driver.find_element(By.ID,'email')
        email_element.send_keys(self.email)

        password_element = self.driver.find_element(By.ID,'pass')
        password_element.send_keys(self.password)

        login_button = self.driver.find_element(By.ID,'loginbutton')
        login_button.click()
        time.sleep(5)

    def Msg(self):
        for i in range (len(list)):
            pyautogui.hotkey('Ctrl','f')
            pyautogui.typewrite("what's on your mind")
            pyautogui.press('enter')
            pyautogui.press('Escape')
            pyautogui.press('enter')
            pyautogui.typewrite(titles[i])
            time.sleep(5)
            pyautogui.hotkey('Ctrl','f')
            pyautogui.typewrite("Add to your post")
            pyautogui.press('enter')
            pyautogui.press('Escape')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('Ctrl','f')
            pyautogui.typewrite("photo/video")
            pyautogui.press('enter')
            pyautogui.press('Escape')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('Ctrl','f')
            pyautogui.typewrite("Add photos/videos")
            pyautogui.press('enter')
            pyautogui.press('Escape')
            pyautogui.press('enter')
            time.sleep(4)
            pyautogui.typewrite(paths[i])
            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('Ctrl','f')
            pyautogui.typewrite("post")
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(5)
            pyautogui.hotkey('Ctrl','enter')
            time.sleep(7)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.hotkey('Ctrl','enter')
            time.sleep(15)
answer=str(input("Are You Ready To Post to Facebook enter y:"))
if answer=="y":
    em = str(input("Enter Your FaceBook Account:"))
    pa=str(input("Enter Your Facebook Password:"))
    fb_login = FacebookLogin(email="", password="", browser='Chrome')
    fb_login.login()
    time.sleep(60)
    fb_login.Msg()
    print("We Post All Videos!")


