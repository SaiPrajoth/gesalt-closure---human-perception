from itertools import permutations
from wordfreq import zipf_frequency


taken_statement = "Three were two gerat dyas in ym lief"
taken_statement=taken_statement.lower()
x = taken_statement.split()
k=""

def computerWork(i):
    new = []
    inp = x[i]
    letter = [y for y in inp]

    for z in list(permutations(letter)):
        new.append("".join(z))

    max = 0
    for item in new:
        if zipf_frequency(item, 'en') > max:
            k = item
            max=zipf_frequency(item,'en')

    return k

computer_statement=""
for i in range(len(x)):
    ToBeAdded=computerWork(i)
    computer_statement+=" "+ToBeAdded

print(computer_statement)
