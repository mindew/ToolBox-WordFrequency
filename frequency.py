
import pickle
import requests
import string
from operator import itemgetter

adventure_of_sherlock_holmes = requests.get('http://www.gutenberg.org/ebooks/1661.txt.utf-8').text
# Analyzing "Adventure of Sherlock Holmes"

# Save data to a file
f = open('adventure_of_sherlock_holmes.pickle', 'wb')
pickle.dump(adventure_of_sherlock_holmes, f)
f.close()

# Load data from a file
input_file = open('adventure_of_sherlock_holmes.pickle', 'rb')
reloaded_copy_of_texts = pickle.load(input_file)


def process(s):
    # creates a dictionary called hist by stripping of the text
    hist = dict()
    new_s = s.replace('-', ' ')
    # replace the space with dash and strips it off later
    for word in new_s.split():
        word = word.strip(string.punctuation + string.whitespace)
        # strips off all of punctuations and whitespaces
        word = word.lower()
        # converts the string into all lowercase
        hist[word] = hist.get(word, 0) + 1
        # update the dictionary w/e it finds new word / updates its value
    return hist


hist = process(reloaded_copy_of_texts)


def most_common(text):
    # creates the dictionary called t to find out most commonly used words
    t = []
    for key, value in text.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t


t = most_common(hist)
print('The most common words are:')
for freq, word in t[:99]:
    print(word, freq)
    # sort the dictionary by its values and returns
    # top 10 highest keys



if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
