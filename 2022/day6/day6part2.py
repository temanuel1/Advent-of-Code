f = open('input.txt', 'r')
content = f.read()
char_needed = 14

def check_unique(str):
  for i in range(len(str)):
    for j in range(i + 1,len(str)):
      if(str[i] == str[j]):
        return False
  return True

while not (check_unique(content[:14])):
    char_needed += 1
    content = content[1:]

print(char_needed)