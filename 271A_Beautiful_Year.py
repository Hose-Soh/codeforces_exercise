year = input()
next_distinct = str(int(year)+1)

while len(set(next_distinct))!=4:
    next_distinct = str(int(next_distinct) + 1)

print(next_distinct)