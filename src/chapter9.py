# Chapter 9 - Dictionaries

purse = dict()
purse['money'] = 12
purse['candy'] = 'lollypop'
purse['tissues'] = 5
print purse
purse['tissues'] = purse['tissues'] - 1
print purse
print purse['candy']

print 'tissues' in purse
print 'tuggumi' in purse

print 'Count the occuring names in the list'
counts = dict()
names = ['sven', 'hjalmar', 'sven', 'ingrid', 'sven', 'olle', 'olle']
print names
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts

name = 'sven'
print 'check if the key sven is in the dictionary'
print counts.get(name,0) #prints 0 (default value) if name does not exist

counts2 = dict()
for name in names:
    counts2[name] = counts2.get(name,0) + 1
print counts2

text = 'Det var i inte nagot brott som lag bakom branden i Ostra klockstapeln i Nykoping den 2 juni, rapporterar lokala medier. Den tekniska undersokning som gjorts efter branden visar att brandorsaken inte gar att faststalla. Det fanns inga spar efter brandfarliga vatskor och inte heller nagra tecken pa att nagon brutit sig in i byggnaden. Sormlandspolisen skriver i ett pressmeddelande att en'
words = text.split()
#print 'Words:', words
for word in words:
    counts[word] = counts.get(word,0) + 1

for key in counts:
    print key, counts[key]

# Does the same as above
for nyckel,varde in counts.items():
    print nyckel, varde

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print 'Flest antal av:', bigword,bigcount
