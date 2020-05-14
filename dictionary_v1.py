import json
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))

def dictionary(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys())) > 0 and word not in data:
        #return "did you mean %s?" % get_close_matches(word,data.keys())[0]
        tryagain = input("did you mean %s? Y or N?" % get_close_matches(word,data.keys())[0])
        if tryagain.upper() == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif tryagain.upper() == 'N':
            return 'Word not in dictionary. please try again.'
    else:
        return 'Word is not in dictionary. please try again.'

word = input('enter word:')
output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
