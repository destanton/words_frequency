#  Your program should open sample.txt and read in the entirety of its text.
from string import punctuation

with open("sample.txt") as better_open_file:
    better_contents = better_open_file.read()

content = better_contents.lower()
# spaces = [" ", "  ", "   "]
bad_n = ["\n"]
for x in punctuation:
    content = content.replace(x, "")
for n in bad_n:
    content = content.replace(n, " ")
# for space in spaces:
#     content = content.replace(space, " ")

content = content.split()
print('\n'.join(content))
bad_words = [
            'a',
            'an',
            'the',
            'if',
            'from',
            'with',
            'be',
            'for',
            'as',
            'it',
            'he',
            'she',
            'they',
            'his',
            'her',
            'to',
            'too',
            'i',
            'am'
            'the',
            'of',
]
new_content = []
while True:
    if bad_words in content:
        continue
    else:
        new_content.append(content)
    break
print('\n'.join(new_content))

# an empty list

# and in your list of every single one of your words, you looped through and and you were like “is this word in my list of excluded words?"

# and if it isn’t, you add that word to your new list

# and if it is, you don’t do anything

# and at the end, you have that new list that has all of your words, minus anything in the exclude list
# # normalize the text so that words in different cases are still the same word and so it's scrubbed of punctuation
# bad_n = ["\n"]
# contents = better_contents
# for x in punctuation:
#     contents = contents.replace(x, "")
#
# for n in bad_n:
#     contents = contents.replace(n, " ")
# contents = contents.split()
# print(contents)
# while True:
#     ignored_words = "a, an, and, the, he, she, it, we, they, them, be, is, do, of"
#     if ignored_words in contents:
#         contents = contents.replace(ignored_words, "")
#     else:
#         break
# print(contents)

my_dict = {}

# for word in content:
#     # print(word)
#     if word in my_dict.keys():
#         my_dict[word] += 1
#     else:
#         my_dict[word] = 1
# words_sort = sorted(my_dict.items(), key=lambda x: x[1])
# words_sort = words_sort[:-21:-1]
#
#
# for word, count in words_sort:
#     print("{} {}".format(word, count))




# for word in contents:
#     # print(word)
#     if word in my_dict.keys():
#         my_dict[word] += 1
#     else:
#         my_dict[word] = 1
# words_sort = sorted(my_dict.items(), key=lambda x: x[1])
# words_sort = words_sort[:-21:-1]
#
# for word, count in words_sort:
#     print("{} {}".format(word, count))
# print(contents)
#  my notes
#  print(help(list))
#  sorted accepts the value of a key
