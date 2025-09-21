def number_of_words(text: str):
    return text.split().__len__()

def number_of_characters(text:str):
    count_dict = {}
    characters = [char for char in text]
    for char in characters:
        count_dict[char] = count_dict.get(char, 0) + 1
    print(count_dict)
    return count_dict