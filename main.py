#  Your program should open sample.txt and read in the entirety of its text.
from string import punctuation

with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read()

# normalize the text so that words in different cases are still the same word and so it's scrubbed of punctuation

contents = better_contents
bad_n = ["\n"]
for x in punctuation:
    contents = contents.replace(x, "")

for n in bad_n:
    contents = contents.replace(n, " ")

contents = contents.split()
my_dict = {}

for word in contents:
    print(word)
    if word in my_dict.keys():
        my_dict[word] += 1
    else:
        my_dict[word] = 1
print(sorted(my_dict.items(), key=lambda x: x[1]))



#  go through the text and find the number of times each word is used.
#  a collection of text (a book) into another form (a frequency dictionary).
#  find the top 20 words used and output them to the console in reverse order, along with their frequency,
#  print(help(list))
#  sorted accepts the value of a key
