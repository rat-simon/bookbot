def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_letters(file_contents):
    dictionary = {}
    for letter in file_contents:
        letter = letter.lower()
        if letter in dictionary:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    return dictionary
def sort_by(dict):
    return dict["count"]

def sort_letters(dictionary):
    finished_list = []
    for a, b in dictionary.items():
        finished_list.append({"letter": a, "count": b})
    finished_list.sort(reverse=True, key=sort_by)
    return finished_list

