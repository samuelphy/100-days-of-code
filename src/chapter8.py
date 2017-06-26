#chapter 8 - Lists

x = range(4) #create a list length 4
print x
x[2] = 7
print x

print x[2:]

x.append(-3)
x.append(99)

print x

print len(x)
print max(x)
print min(x)
print sum(x)
print sum(x)/len(x) #avg

if 99 in x:
    print 'Yes 99 is in x'

friends = ['Ann', 'Carola', 'Birger']
print len(friends)

print range(len(friends))

for friend in friends:
    print 'Happy new year', friend

friends.sort()
print friends

#Strings and list
abc = 'With    three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]

cs = 'hej,hopp,gott'
stuff = cs.split(',')
print stuff
