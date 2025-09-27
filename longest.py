def longest_lines(filename):
    lines = open(filename).readlines()
    lines = [line.rstrip('\n') for line in lines]
    max_length = max(len(line) for line in lines)
    return [line for line in lines if len(line) == max_length]