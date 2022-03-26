from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()
driver.get("https://music.yandex.kz/users/CleRleQ/playlists/3")

cross = driver.find_element_by_css_selector("div.js-close")
cross.click()

i=0
file = open('playlist.txt', 'w', encoding="utf-8")
while i != 13:
    i += 1
    all_songs = driver.find_elements_by_css_selector("div.d-track__overflowable-wrapper ")

    for song in all_songs:
        file.write(song.text + "\n" + "\n")
    file.write(str(len(all_songs)))

    driver.execute_script("window.scrollBy(0, 4488)","")
    time.sleep(2)

file.close()
    
time.sleep(2)
driver.close()






