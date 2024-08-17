
sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. Interestingly, The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

words = sample_story.replace(',','').replace('.','').split()
print(words)

def get_longest_word(sentence):
    remove_comma = sentence.split(", ")
    new_txt = ' '.join(remove_comma)
    list_wo_commas = new_txt.split()
    counter = 0
    largest_word = ""
    for word in list_wo_commas:
        if "." in word:
            word_length = len(word) - word.count(".")
            if word_length > counter:
                counter = word_length
                largest_word = word
        else:
            if len(word) > counter:
                counter = len(word)
                largest_word = word
    print(largest_word)

#get_longest_word(sample_story)


def get_longest_word(input_string):
    words = input_string.replace('.', ' ').replace(',', ' ').split()
    temp_max_word = ''

    for word in words:
        if len(word) > len(temp_max_word):
            temp_max_word = word

    return temp_max_word

# example = "Once I'm awaken, I'll sacrifice, your soul, to the ruler of darkness."
#
# list1 = example.split(",")
# print(list1)

# list2 = sample_story.split()
# print(list2)

# to not count spaces
# res = sum(not chr.isspace() for chr in test_str)

##Goal: Given an input which will be a sentence, dispaly the word that has the longest length.

txt = "Hello, my name is Peter, I am 26 years old..."

# ##TODO split the string into a list by removing any commas
# remove_comma = sample_story.split(", ")
# #print(remove_comma)
#
# ##TODO join the list to a string
# new_txt = ' '.join(remove_comma)
# #print(new_txt)
#
# ##TODO split the string into a list again now that commas have been removed
# list_wo_commas = new_txt.split()
# #print(list_wo_commas)
#
# ##Count the length of each word but do not include the "."
# counter = 0
# largest_word = ""
# for word in list_wo_commas:
#     print(f"{word}: {len(word)}")
#     if "." in word:
#         word_length = len(word) - word.count(".")
#         if word_length > counter:
#             counter = word_length
#             largest_word = word
#     else:
#         if len(word) > counter:
#             counter = len(word)
#             largest_word = word
# print(counter, largest_word)

#x = ' '.join()
#print(x)
#x = x.split()
#x = 
#print(x)
# for i in x:
#   if "." in i:
#     y = i.count(".")
#     z = len(i) - y
#     print(i)
#     print(y)
#     print(z)

