import re 

s = input().lower()

pattern = r"h.*?e.*?l.*?l.*?o"

match = re.search(pattern, s)

if match:
    print("YES")
else:
    print("NO")

    