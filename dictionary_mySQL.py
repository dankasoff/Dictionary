import mysql.connector
import json
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))

connection =  mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

word = input('enter a word: ')

cursor = connection.cursor()
query = cursor.execute("SELECT * FROM Dictionary")
results = cursor.fetchall()
resultsDict = dict(results)

def dictionary(word):
    if word in resultsDict:
        return resultsDict[word]
    elif word.lower() in resultsDict:
        return resultsDict[word.lower()]
    elif word.upper() in resultsDict:
        return resultsDict[word.upper()]
    elif word.title() in resultsDict:
        return resultsDict[word.title()]
    elif len(get_close_matches(word,resultsDict.keys())) > 0 and word not in resultsDict:
        #return "did you mean %s?" % get_close_matches(word,data.keys())[0]
        tryagain = input("did you mean %s? Y or N?" % get_close_matches(word,resultsDict.keys())[0])
        if tryagain.upper() == 'Y':
            return resultsDict[get_close_matches(word,resultsDict.keys())[0]]
        elif tryagain.upper() == 'N':
            return 'Word not in dictionary. please try again.'
    else:
        return 'Word is not in dictionary. please try again.'

output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)