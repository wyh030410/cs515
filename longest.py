def longest_lines(filename):
    lines = open(filename).readlines()
    lines = [line.rstrip('\n') for line in lines]
    max_length = max(len(line) for line in lines)
    return [line for line in lines if len(line) == max_length]
with open('foo.txt', 'w') as f:
    f.write('a\nb\ncd\nef\ng\n')

print(longest('foo.txt'))