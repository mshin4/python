### Given the dictionary, output the file names that are identical.

dict = {
    "file1": "e7d29b6fc7afbffd3829f373a3a30876",
    "file2": "bad5a62acd5007c3eab9b08ca3f8941f",
    "file3": "e7d29b6fc7afbffd3829f373a3a30876",
    "file4": "9b36325abb4a6d8fd577e4676ade182f",
    "file5": "c111262de69c0ddfdc421d32feafce6c",
    "file6": "bad5a62acd5007c3eab9b08ca3f8941f",
    "file7": "e7d29b6fc7afbffd3829f373a3a30876",
}

dict_result = {}

for file in dict:
    hash = dict[file]
    if hash in dict_result:
        dict_result[hash].append(file)
    else:
        dict_result[hash] = [file]

print(dict_result)