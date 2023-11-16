'''

np.insert() is used to insert elements at a specific position in an existing array, while np.concatenate() and np.append() are used to concatenate multiple arrays together.

np.concatenate() can concatenate more than two arrays together and also specify the axis along which to concatenate.

np.append() is a convenience function that is equivalent to calling np.concatenate((a, [b])) with a and b being the input arrays. It can only concatenate two arrays and it concatenate along the last axis.

In summary, use np.insert() when you want to insert elements into an existing array at a specific position.
            Use np.concatenate() when you want to concatenate multiple arrays together along a specific axis.
             Use np.append() when you want to concatenate two arrays together along the last axis.
'''


from string import punctuation

my_list = ['hello', 'world', 'andndksl']

word = max(my_list, key=len) #longest string


class Analyzer:
    def __init__(self, s):
        for c in punctuation:
            s = s.replace(c, '') # replaces a specified phrase with another specified phrase
            s = s.lower()  # converts all uppercase characters into lowercase characters
            self.words = s.split()  # Split a string into a list where each word is a list item
    #how many words are in the string
    def num_words(self):
        return len(self.words)
    #how many start with a given string
    def stars_with(self, s):
        return len([w for w in self.words if w[:len(s)] == s])
    # how many are of given length
    def num_with_len(self, n):
        return len([w for w in self.words if len(w) == n])

s = 'This is a test of the class'
analyze = Analyzer(s)
print(analyze.words)
print('Number of words:', analyze.num_words())
c, n = 't', 2
print(f'Number of words start with "{c}":',analyze.stars_with(c))
print(f'Number of {n}-letter words:',analyze.num_with_len(n))