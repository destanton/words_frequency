# ignored_words = ("a, able, about, across, after, all, almost, also, am, among, an, and, any, are, as, at, be, because,    been, but, by, can, cannot, could, dear, did, do, does, either, else, ever, every, for, from, get, got, had, has, have, he, her, hers, him, his, how, however, i, if, in, into, is, it, its, just, least, let, like, likely, may, me, might, most, must, my, neither, no, nor, not, of, off, often, on, only, or, other, our, own, rather, said, say, says, she, should, since, so, some, than, that, the, their, them, then, there, these, they, this, tis, to, too, twas, us, wants, was, we, were, what, when, where, which, while, who, whom, why, will, with , would, yet, you, your")
# for bad in ignored_words:
#     contents = contents.replace(bad, " ")
# print(contents)
# secret_word = ['them', 'we', 'they']
# my_list = ['me', 'you', 'she', 'they']
# my_new_list = []
# while True:
#     if my_list in secret_word:
#         continue
#     else:
#         my_new_list.append(secret_word)
#         break
# print(my_new_list)

my_string = "peanut is awesome"
my_string = my_string.split()
# convert large string into list of occurances. .split will make inv. words inside a list.
print ('\n'.join(my_string))
