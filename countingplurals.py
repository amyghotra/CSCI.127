#counting nouns

#have the use input a list of nouns
words = input("Enter nouns: ")

#counts how many words there are by counting the number of spaces
# "1" is added for the last word, which does not have a space attached
lengthWords = words.count(" ")+1

#prints the number of words present in the list
print("Number of words: ", lengthWords)

#in order to count the plurals, count how many letter "s"s are followed by a space
numberPlurals = words.count("s ")

#set a variable to "s"
SS = "s"

#set the last letter of the last word equal to "last"
last = words[-1]

#if the last letter of the last word in the list is an "s"
if last == SS:
    numberPlurals2 = numberPlurals + 1          #add 1 to the number of plurals if the last letter is indeed an "s"
    fraction2 = numberPlurals2 / lengthWords    #get the fraction of words which are plural
    print("Fraction of your list that is plural is: ", fraction2)   #print the fraction of words which are plural
#this will run if the last letter is not an "s"
else:   
    fraction = numberPlurals / lengthWords
    print("Fraction of your list that is plural is: ", fraction)
