import json
import difflib


def input_function():       #Called when the word entered has some relavent keys
    choose=raw_input()      #Yes or No
    if choose=="Y" or choose=="y":  #if yes return the first element of the resultant list
        return dictionary[difflib.get_close_matches(word,dictionary.keys())[0]]     #retrives hte first element
    elif choose=="N" or choose=="n":
        return "The specified key is not found"
    else:
        return "You have entered a wrong input"

def search_dict(word):      #Helps in searching the word
    if word in dictionary:      #if the key is present print the value
        return dictionary[word]
    elif word.title() in dictionary:        #if the first letter is caps (Atlanta,Texas)
        return dictionary[word.title()]
    elif word.upper() in dictionary:        #if the word has all letters in uppercase(USA,UFO,UNICEF)
        return dictionary[word.upper()]
    elif len(difflib.get_close_matches(word,dictionary.keys()))>0:  #if the word entered by user is not in dict and has some relavent keys
        print("Did u mean %s .[Y/N]?" % difflib.get_close_matches(word,dictionary.keys())[0])       #Asks the user to confirm
        return input_function()     #calls input_function()
    else:
        return "The specified key is not found"



dictionary=json.load(open("data.json"))         #Opening Json files and stores the result as a dictionary
word=raw_input("Enter the word to be searched:").lower()        #Get user input and covert to lower case
resultObject=search_dict(word)      #Calls the serch_dict() and stores the result in result resultObject
if type(resultObject) == list:      #Checks the value in result object --->list or string
    for result in resultObject:     #iterates through the list to display the value
        print(result)
else:
    print(resultObject)
