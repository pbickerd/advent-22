import string

lines = []
total = 0

alphabet = list(string.ascii_letters)

def getValue(commonCharacter):
    character = list(commonCharacter)[0] # Item comes in a list, need to get it into a string
    score = alphabet.index(character) + 1 # Get the index value of the character passed in and add 1 as our index starts at 0
    return score

with open("input.txt") as file:
    for line in file:
        firsthalf = set(line[:len(line)//2]) # take first half of the string and put in a set
        secondhalf = set(line[len(line)//2:]) # take second half of the string and put in a set
        common = firsthalf & secondhalf # Set intersection gives us the common characters
        total = total + getValue(common) # User our function that returns a score

print("The total is ", total)