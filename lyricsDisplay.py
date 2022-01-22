from pyfirmata import Arduino, util, STRING_DATA
import scraper
import time

def main():

    board = Arduino('COM3')
    lyrics = scraper.getLyrics()
    # lyrics = ['[Verse]', 'How', 'did', 'I', 'try', 'to', 'get', 'you', 'off', 'my', 'mind?How', 'did', 'I', 'try', 'to', 'get', 'you', 'off', 'my', 'mind?', 'Could', 'this', 'be', 'the', 'end', 'Of', 'you', 'and', 'I', 'for', 'now?', 'Hope', 'that', 'I', 'see', 'you', 'soon', "Don't", 'know', 'what', 'I', 'would', 'do', 'My', 'heart', 'is', 'under', 'the', 'weather', 'I', 'know', 'that', 'I’m', 'the', 'only', 'one', 'who', 'can', 'heal', 'it', "I'm", 'on', 'my', 'own,', "I'm", 'on', 'my', 'own', "I'm", 'on', 'my', 'own,', "I'm", 'on', 'my', 'own', 'I', 'try', 'to', 'be', 'the', 'strong', 'one', 'for', 'you', 'But', "that's", 'just', 'too', 'hard', 'for', 'anyone', 'to', 'do', '[Outro]', 'Ooh', 'Mmm']
    # lyrics = ['[Verse]', 'How did I try to get you off my mind?How did I try to get you off my mind?', 'Could this be the end', 'Of you and I for now?', 'Hope that I see you soon', "Don't know what I would do", 'My heart is under the weather', 'I know that I’m the only one who can heal it', "I'm on my own, I'm on my own", "I'm on my own, I'm on my own", 'I try to be the strong one for you', "But that's just too hard for anyone to do", '[Outro]', 'Ooh', 'Mmm']
    sorted = []
    count = 0
    lengthCount = 0
    clear = '\n'
    exit = '^'
    # spaces = "                        " # 24 spaces for off-screen space filling

        
   #lyrics[i] = word  
    for i in range(0, len(lyrics)):
        lengthCount += (len(lyrics[i]) + 1) # word length plus a space

        if count == 1:
            printLyrics(board, clear) # clears lcd after screen is full
            count = 0
            
        if lengthCount < 16:
            try:
                if lyrics[i + 1]:
                    # if lC plus the next word is less than 16
                    if (lengthCount + (len(lyrics[i + 1]) + 1) <= 16): 
                        sorted.append(lyrics[i] + " ") # add word to list + space
                    
                    # if lC plus the next word is greater than 16
                    elif (lengthCount + (len(lyrics[i + 1]) + 1) > 16):
                        sorted.append(lyrics[i] + " ")
                        
                        # while lengthCount < 16: # fills space before printing (only used when both rows of the screen are used)
                        # sorted.append(" " + clear)
                            # lengthCount += 1  
                    
                        for word in sorted:
                            printLyrics(board,word)
                            time.sleep(0.8) # speed of text
                         
                        # printLyrics(board,spaces) # fills in space off-screen
                        lengthCount = 0 # reset count
                        sorted.clear() # clear list after printing
                        count += 1 # line count
                        
                # if no following word, fill space in current list and print words       
                else:
                    sorted.append(lyrics[i] + " ")
                    
                    # while lengthCount < 16: # fills space before printing (only used when both rows of the screen are used)
                    # sorted.append(" " + clear)
                        # lengthCount += 1  
                    
                    for word in sorted:
                        printLyrics(board,word)
                        time.sleep(0.8) # speed of lcd printing
                    
                    # printLyrics(board,spaces)
                    lengthCount = 0 # reset count
                    sorted.clear() # clear list after printing
                    count += 1
            except:
                printLyrics(board,lyrics[i])
                time.sleep(5)
                printLyrics(board, exit)
                
        elif (lengthCount == 16):
            sorted.append(lyrics[i] + " ")
            
            for word in sorted:
                    printLyrics(board,word)
                    time.sleep(0.8) # speed of lcd printing
                    
            # printLyrics(board,spaces)
            lengthCount = 0 # reset count
            sorted.clear() # clear list after printing
            count += 1  
            
        else:
            print("Error: Cannot parse strings greater than 16 characters")
            return 1
    
        
def printLyrics(board,line):
    board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(line))


if __name__ == "__main__":
    main()