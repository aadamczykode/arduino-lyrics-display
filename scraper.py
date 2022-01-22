from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def getLyrics():
    name = input("enter artist name: ")
    artist = ""
    j = 0
    
    for letter in name:
        if letter == " ":
            if name[j + 1].isalpha():
                letter = "-"
            else:
                print("invalid artist name")
                return(1)
        j += 1
        artist += letter
        
    song = input("enter song title: ")

    artist = artist + "-"
    song = song.replace(" ", "-")
    songArtist = artist + song
    route = ""
    i = 0

    for space in songArtist:
        if space == songArtist[0] and i == 0:
            space = space.upper()
            i += 1
        if space == "":
            space = "-"
        route += space      
            
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))      
    driver.get(f"https://genius.com/{route}-lyrics")

    content = driver.page_source # gets page source form genius URL
    soup = BeautifulSoup(content, "html5lib")
    
    # searching for divs with lyrics and saving text
    results = []
    for a in soup.findAll("div", {"class": "Lyrics__Container-sc-1ynbvzw-6 lgZgEN"}):
        for b in a:
            results.append(b.text)

    # removing empty values in list
    lyrics = ""
    for line in results:
        if line != '':
            lyrics += line + " "
                   
    
    lyrics = lyrics.split()

    print(lyrics)
    return lyrics