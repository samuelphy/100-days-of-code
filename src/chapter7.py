# Chapter 7
# Files

fname = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opended:',fname
    exit()

for line in fhand:
    line = line.strip() #Remove \n
    # Skip uninteresting lines
    if not line.startswidth('From:'):
        continue # exit this iteration and look at the next line
    # Process interesting line
    print line
