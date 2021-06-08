data_set = open('/Users/taraghazanfari/Desktop/dataset.txt', 'r')
f = data_set.read().splitlines()
text = f[0]
pattern = f[1]


def patterncount(text, pattern):
    count = 0
    text_size = len(text)
    pattern_size = len(pattern)
    sizing = text_size + pattern_size + 1

    for i in range(0, sizing):
        if text[i : pattern_size + i] == pattern:
            count += 1
    return count
print(patterncount(text, pattern))