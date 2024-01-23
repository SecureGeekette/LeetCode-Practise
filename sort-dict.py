input = {0: 10, 1: 5, 2:2}
new_input = list(input.items())

# sort a dictionary in ascending order by value

for i in range(len(new_input)):
  for j in range(len(new_input)-i-1):
    if new_input[j][1] > new_input[j+1][1]:
      new_input[j], new_input[j+1] = new_input[j+1], new_input[j]


print(dict(new_input))

