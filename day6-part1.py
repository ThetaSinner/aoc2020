def split(word):
    return [char for char in word]

f = open('day6-input')
input = f.read().split('\n\n')

clean_newlines = [x.replace('\n', '') for x in input]

sum_of_counts = sum([len(set(split(x))) for x in clean_newlines])
print(sum_of_counts)
