digits = ['1','2','3','4','5','6','7','8','9']
en = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
fr = ['un','deux','trois','quatre','cinq','six','sept','huit', 'neuf']

# french = dict.fromkeys(fr, 'french')
# english = dict.fromkeys(en, 'english')
#
# print(french)
# print(english)
output = dict((z[0], { 'french': z[1], 'english': z[2]}) for z in zip(digits,fr,en))
#
print(output)

# d = dict(
#     [
#         (1, 2),
#         (4, 5)
#     ]
# )

#  d = {}
# # for i in range(0,len(digits)):
# #     d[digits[i]] = {'french':fr[i], 'english':en[i]}
# print(d)

#need to read documentation for dictionaries/ how to solve something using a dictionary
# do the train assignment
