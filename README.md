# Lyrics Display Project
#### Video Demo:  <https://www.youtube.com/watch?v=f8fSq2kHuKU&ab_channel=aadamczykode>
#### Description:
The user is promted to input the name of an artist and the name of a song. The lyrics to the selected song are then displayed on an arduino display.
The LCD1602 module being used is very limiting. The size of the display is 16x2 and it only has 80 bytes of RAM.
Because of this, characters are corrupted and the display starts acting up if a string longer than ~40 characters is sent to it all at once.
I have chosen to use only one row in the display to gain more control. When using both rows, I would need to fill in the empty space left at the end of
a string to completely fill the 16 space screen, then add a 24 character buffer to fill in off-screen space before beginning to print on the 2nd row.
This caused awkward pauses to occur, because it takes a while for the empty space to be filled.


#### Hardware:
- Arduino Uno
- LCD Screen with pin header (compatible with Hitachi HD44780 driver)
- 10k ohm potentiometer
- 220 ohm resistor
- hook-up wires
- breadboard


#### Circuit:
- LCD RS pin to digital pin 12
- LCD Enable pin to digital pin 11
- LCD D4 pin to digital pin 5
- LCD D5 pin to digital pin 4
- LCD D6 pin to digital pin 3
- LCD D7 pin to digital pin 2
- LCD R/W pin to GND
- LCD VSS pin to GND
- LCD VCC pin to 5V
- LCD LED+ to 5V through a 220 ohm resistor
- LCD LED- to GND


#### Scripts:

#### scraper.py
##### getLyrics Function
Asks user to input artist name and song title.
Concatenates both and then formats them with dashes
instead of spaces. Using the Selenium library, the instance of chrome webdriver is made with the help of chrome driver manager.
The formatted artist name + song title are then inserted into the genius.com URL where the "driver.get" method loads the contents of the webpage.
Once fully loaded, the page source is set to a variable, "content".
Next, the BeautifulSoup library is used to scrape the page source, using html5lib as a parser.
BeautifulSoup's ".findAll" method is used to search for divs in the HTML that contain song lyrics.
The lyrics are formatted and then set to a variable, lyrics. The function returns lyrics.


#### lyricsDisplay.py
##### main Function
Initalizes "board" variable to the arduino and the port being used.
Next, gets lyrics by calling the "getLyrics" function in the "scraper.py" script.
The "sorted" variable is made to hold a list of words whose characters' total sum is less than or equal to 16.
Once ~16 characters are loaded into the list, the printLyrics function is called to send the arduino one word at a time.
After all of the words are sent to the arduino, the screen is cleared.
The time library's "sleep" method is what determines who fast or slow a song's lyrics are printed to the display.
After 1 line of lyrics is sent to the Arduino, the screen is cleared.
After the final lyric is printed, the screen turns off.

##### printLyrics Function
Sends string data to string callback function in Arduino code.

#### lyricsDisplay.ino
LCD pins connected to the arduino board are specified to be used with LiquidCrystal library. Variables "c" and "e" are initialized
to specify when the LCD should be cleared or turned off based on what is sent to the "stringDataCallback" function.
Number of columns and rows on screen are specified for use.
Firmata library and methods are used to receive
string data sent to the Arduino from "lyricsDisplay.py" in both setup and loop functions.
This function has to be called every time a word is passed to it, because the firmata library only allows the
Arduino to receive a string via callback function. It cannot store the string for future use.


#### Issues:
- Songs with words greater than 16 characters long will not work with the code.
- If a song is long and has many lyrics, it may take a while for the webdriver to load
the contents of the page into the "content" variable.
- Sometimes lyrics are formatted improperly with two words combined to make one.
- Sometimes strange characters show up to replace others, but rarely.