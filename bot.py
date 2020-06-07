from selenium import webdriver 
from pyautogui import press
from time import sleep
from faker import Faker
import json
import random

#programmed by essam al deen


link = input("Enter link: ") #take link

fname = json.loads(open('fnames.json').read())#first names
lname = json.loads(open('lnames.json').read())#last names
web = webdriver.Chrome()#using chrome
fake = Faker()#faker

def sendForm(runs):
        randfname = random.randrange(1000)#random
        randlname = random.randrange(1000)#random
        randemail = fake.email()#fake email
        firstname = web.find_element_by_name("firstName")
        lastname = web.find_element_by_name("lastName")
        emailbox = web.find_element_by_name("email")
        signbutton = web.find_element_by_xpath("""//*[@id="page"]/div[1]/div[3]/div[2]/div/div/div/div[2]/div[2]/form/button""")
        publick = web.find_element_by_name("public")
        print("Using name", fname[randfname], lname[randlname], "and email", randemail, "This is run number", runs)
        firstname.send_keys(fname[randfname])
        lastname.send_keys(lname[randlname])
        emailbox.send_keys(randemail)
        sleep(0.5)#take 0.5 sleep
        publick.click()
        sleep(0.5)
        signbutton.click()
        sleep(1)
        web.delete_all_cookies()
        web.get(link)

def main():#main func
    web.get(link)
    rm = 0
    for _ in range(1, 1000):#range
        try:
            sendForm(rm)
            rm =rm+ 1
        except: #except
            web.delete_all_cookies()
            web.get(link)
            print("Error,  Refreshing")
main()#call main func
