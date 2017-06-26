#chaper 10 - Tuples (like immutable lists)

(x, y) = (4, 'fred')
print y

#double assignment
a, b = (99, 98)
print a
print type(a)

print (0, 1, 2) < (5, 1, 2)
print (0, 1, 2000) < (0, 3, 4)
print ('Jones', 'Solly') < ('Jones', 'Sally')

d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t
t.sort(reverse=True)
print t

q = sorted(d.items())
print q

for k, v in sorted(d.items()):
    print k, v

#Short version of sorting above
#List comprehension: creates a dynamic list.
#In this case a list of reveresed tuples and then sort it.
print sorted( [ (v,k) for k,v in d.items() ] )

fhand = open('inverseSquareRoot.c')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append( (val, key) )

lst.sort(reverse=True)

print 'Top ten words in file'
for val, key in lst[:10]:
    print key, val
