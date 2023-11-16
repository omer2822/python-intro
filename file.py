# read files

# The string method strip removes any whitespace characters from the beginning and end of a string.
# We will use rstrip if we need to preserve whitespace at the begining of the line
lines = [line.strip() for line in open('example.txt')]
print(lines)

s = open('example.txt').read()

# write to files

f = open('writefile.txt', 'w')
print('This is line 1.', file=f)
print('This is line 2.', file=f)
f.close()