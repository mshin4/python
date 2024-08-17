##TODO use math module to round up the division of string length; then, slice the string in the middle

# string_utils.py
# def halve_string(input_string):
#     halfway_pt = math.ceil(len(input_string)/2)
#     return (input_string[:halfway_pt], input_string[halfway_pt:])
#

# strings_utils.py
# def halve_strings(list):
#     strings_list = []
#     for i in list:
#         strings_list.append(string_utils.halve_string(i))
#     return strings_list

# main.py file
# import strings_utils
#
# quotes = ['Being happy never goes out of style.',
#           'Life is either a great adventure or nothing.',
#           'All you need in this life is ignorance and confidence; then success is sure.',
#           'All your life, you will be faced with a choice. You can choose love or hate... I choose love.',
#           'The time is always right to do what is right.']
#
# print(strings_utils.halve_strings(quotes))