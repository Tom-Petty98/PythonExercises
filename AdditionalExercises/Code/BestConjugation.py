# Find out how many different words you can make, from smaller valid sub-words.
# Example
# Awesomeness = 3 – Awe, Some, Ness
# Something = 3 – So, Me, Thing
# Disproportionate = 5 – Dis, Pro, Port, Ion, Ate

# is it quicker to start searching from the starting letter???
import urllib.request

def find_sub_words(word):
    numOfSubWords = 0

    for i in range(len(word)):

        for subWordLen in range(i, len(word) - i):
            subWordLen = 3
        c = listOfWords.count(word[i:i + subWordLen])
        
        if c > 0:
            numOfSubWords += 1
            i += 3


url = "http://www-personal.umich.edu/~jlawler/wordlist"
file = urllib.request.urlopen(url)

#for line in file:
#    if len(line) <= 3:
#        print(line)         # example out b'a\r\n'     So it looks as if it includes the all three letters in length

listOfWords = []

for line in file:
    if len(line) <= 3:
        line.strip('\r\n')
        print(line)


    