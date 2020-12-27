from selenium import webdriver
from os import system, name

from time import time, strftime, gmtime, sleep
import pyfiglet, os, threading

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title TIKTOD V3')

print(pyfiglet.figlet_format("TIKTOD V3", font="slant"))
print("1. Viewbot.\n2. Heartbot.\n3. Followerbot.\n4. Credits.\n")

auto = int(input("Mode: "))

if auto == 1 or auto == 2 or auto == 3:
    vidUrl = input("TikTok video URL: ")

    start = time()
    time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
    driver.set_window_size(1024, 650)

    Views = 0
    Hearts = 0
    Followers = 0

def beautify(arg):
    return format(arg, ',d').replace(',', '.')

def title1(): # Update the title IF option 1 was picked.
    global Views
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title TIKTOD V3 ^| Views Sent: {beautify(Views)} ^| Elapsed Time: {time_elapsed}')

def title2(): # Update the title IF option 2 was picked.
    global Hearts
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title TIKTOD V3 ^| Hearts Sent: {beautify(Hearts)} ^| Elapsed Time: {time_elapsed}')

def title3(): # Update the title IF option 3 was picked.
    global Followers
    
    while True:
        time_elapsed = strftime('%H:%M:%S', gmtime(time() - start))
        system(f'title TIKTOD V3 ^| Followers Sent: {beautify(Followers)} ^| Elapsed Time: {time_elapsed}')
    
def loop1():
    global Views
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop1(100)
        
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/input").send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/div/div/form/div/div/button").click()
        
        sleep(5)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        
        driver.refresh()
        Views += 500 # When testing, the test-video gained +500 views instead of +1000
        print("[+] Views sended!")
        
        sleep(150)
        loop1(100)
        
    except:
        print("[-] An error occured. Retrying..") # "Now will try again" is trashy grammar. I replaced it with "Retrying.."
        driver.refresh()
        loop1(100)

def loop2():
    global Hearts
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop2()
        
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/div/div/form/div/input').send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath('//*[@id="sid2"]/div/div/div/form/div/div/button').click()
        
        sleep(5)
        driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button').click()
        
        sleep(6)
        hearts = driver.find_element_by_xpath('//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Hearts += int(hearts[0])
        print("[+] Hearts sended!")
        
        sleep(5)
        driver.refresh()
        
        sleep(640)
        loop2()
        
    except:
        print("[-] An error occured. Retrying..") # "Now will try again" is trashy grammar. I replaced it with "Retrying.."
        driver.refresh()
        loop2()

def loop3():
    global Followers
    sleep(10)
    
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div/div[1]/div/button").click()
        
    except:
        print("[-] The captcha is unsolved!")
        driver.refresh()
        loop3()
        
    try:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/input').send_keys(vidUrl)
        
        sleep(1)
        driver.find_element_by_xpath('//*[@id="sid"]/div/div/div/form/div/div/button').click()
        
        sleep(5)
        driver.find_element_by_xpath().click('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button')
        
        sleep(6)
        folls = driver.find_element_by_xpath('//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9r"]/span').text.split()
        
        Followers += int(folls[0])
        print("[+] Followers sended!")
        
        driver.refresh()
        sleep(310)
        loop3()
        
    except:
        print("[-] An error occured. Retrying..") # "Now will try again" is trashy grammar. I replaced it with "Retrying.."
        driver.refresh()
        loop3()

clear()

print(pyfiglet.figlet_format("TIKTOD V3", font="slant"))
print("Log:")

if auto == 1:
    driver.get("https://ketuy.com/")
    
    a = threading.Thread(target=title1)
    b = threading.Thread(target=loop1)
    
    a.start()
    b.start()
    
elif auto == 2:
    driver.get("https://ketuy.com/")
    
    a = threading.Thread(target=title2)
    b = threading.Thread(target=loop2)
    
    a.start()
    b.start()
    
elif auto == 3:
    driver.get("https://ketuy.com/")
    
    a = threading.Thread(target=title3)
    b = threading.Thread(target=loop3)
    
    a.start()
    b.start()
    
elif auto == 4:
    print("[+] This program was created by @kongoka. [github.com/kangoka]")
    print("[+] This program was origionally uploaded to github.com/kangoka/tiktodv3.")
    print("[+] This program was majorly improved by @XxBiancaXx. [github.com/XxBiancaXx]")
    print("[+] Views xPath problem solved by @NoNameoN-A. [github.com/NoNameoN-A]")
    
else:
    print(f"{auto} is not a valid option. Please pick 1, 2, 3, or 4")
