#this program will shift messages left

#gets user input
word = input("input a few words")

#this will be modified later on
codedWord = ""

#program to be run
for ch in word:
	    offset = ord(ch) - ord('a') - 1     #how many letters past 'a' (i.e. how far away the character/letter is from 'a')
	    wrap = offset % 26                  #if difference between ASCII 'a' and the letter ASCII is larger than 26, wrap back to 0
	    newChar = chr(ord('a') + wrap)      #compute the new letter
	    codedWord = codedWord + newChar     #add the newChar to the coded word

#prints new, coded/shifted, word	    
print(codedWord)
