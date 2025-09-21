import sys 
if len(sys.argv)< 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

path_to_book = sys.argv[1]

from stats import number_of_characters,number_of_words
print("============ BOOKBOT ============")
with open(path_to_book) as f:
    file_contents = f.read().lower()
    word_count = number_of_words(file_contents)
    print("----------- Word Count ----------")
    count_dict = number_of_characters(file_contents)
    print(f"Found {word_count} total words")
    print(" --------- Character Count -------")
    for key ,value in count_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")


# 
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# Found 75767 total words
# --------- Character Count -------
# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
# n: 23643
# s: 20360
# r: 20079
# h: 19176
# d: 16318
# l: 12306
# m: 10206
# u: 10111
# c: 9011
# f: 8451
# y: 7756
# w: 7450
# p: 5952
# g: 5795
# b: 4868
# v: 3737
# k: 1661
# x: 691
# j: 497
# q: 325
# z: 235
# æ: 28
# â: 8
# ê: 7
# ë: 2
# ô: 1
# ============= END ===============