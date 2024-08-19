## TODO Operational Projects: Find duplicate files
## TODO Operational Projects: Find commond keywords in files like IP address
## TODO Operational Projects: Use tkinter to create a GUI for above

input = 'There, are, commas and periods.'
words = input.replace(',', '').replace('.', '').split()
largest_word = ''

for word in words:
    if len(word) > len(largest_word):
        largest_word = word
print(largest_word)
