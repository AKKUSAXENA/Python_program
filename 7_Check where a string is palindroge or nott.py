my_str = "Madam"

# convert entire string to either lower  or upper
my_str=my_str.lower()

#reverse string
rev_str = reversed(my_str)

#check if the string is equaal to its reverse
if list(my_str) ==list(rev_str):
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")

print()


# 2nd programme
print() # only for space between two programme
myStr = "python Program to Sort words in Alphabetic Order"

#breakdown the string into list of words
words = myStr.split()

#sort the list
words.sort()

#print Sorted words are
for word in words:
    print(word)