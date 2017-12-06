import re


def contains(xs, val):
    return True if xs.count(val) > 0 else False


def count_occurance(dict, key):
    count = dict[key] + 1 if contains(list(dict.keys()), key) else 1
    dict[key] = count


def word_count(file_name):
    f = open(file_name, 'r')
    word_counts = {}
    for line in f:
        data = line.strip().split(" ")
        words = [re.sub(r'[^a-z]', '', x.lower()) for x in data]
        [count_occurance(word_counts, w) for w in words]
    return word_counts


if __name__ == "__main__":
    print(word_count("./alice_in_wonderland.txt"))
