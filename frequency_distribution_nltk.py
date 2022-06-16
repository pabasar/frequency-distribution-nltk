# Frequency Distribution of Words and Letters 

first_gen = """There were a few technologies that evolved and influenced the beginning of 1st generation in wireless communications. Before the 1940s there were wired communications. After that moving from wired to wireless was a revolution in communications. The technologies used in this era called Pre-1G or 0G technologies. First of wireless communications were used for military purposes in world war 2, and government agencies, not for civilians or commercial use. At that time there were pre-cellular mobile radiotelephones (AM radio phones) that could only be used in a limited geographical area. Motorola and Bell Systems were giants in mobile communications in that era. Mobile devices were too large and mounted in cars or trucks. Also, there were briefcase models of telephones. All those systems were not suitable for mass-scale development to facilitate communication for regular people."""

first_gen

from nltk.tokenize import word_tokenize as wt

first_gen = wt(first_gen)

' '.join(first_gen)

import string
string.punctuation

for i in first_gen:
    for j in list(string.punctuation):
        i = i.replace(j,'')
    print(i)

first_gen_no_punct = []

for i in first_gen:
    for j in list(string.punctuation):
        i = i.replace(j,'').lower()
    first_gen_no_punct.append(i)

first_gen_no_punct

' '.join(first_gen_no_punct)

for i in first_gen_no_punct:
    if i.isalpha():
        print(i)

first_gen_words = []

for i in first_gen_no_punct:
    if i.isalpha():
        first_gen_words.append(i)

' '.join(first_gen_words)

from nltk.probability import FreqDist as fd

fd(first_gen_words).most_common(10)

word_dict = dict(fd(first_gen_words).most_common(10))

word_dict

import pandas as pd

most_common_words = pd.DataFrame(
    {"Frequency Distribution of Words": list(word_dict.values())}, 
    index=list(word_dict.keys()))

most_common_words.plot(kind="bar")
       
letters = []

for i in str(first_gen_words):
    if i.isalpha():
        letters.append(i)
        
letters

fd(letters).most_common(10)

letter_dict = dict(fd(letters).most_common(10))

letter_dict

import pandas as pd

most_common_letters = pd.DataFrame(
    {"Frequency Distribution of Letters": list(letter_dict.values())}, 
    index=list(letter_dict.keys()))

most_common_letters.plot(kind="bar")

