from collections import deque

# BFS-like approach
# Generates each "node" one by one

def generate_valid_parentheses(num):
  result = deque([''])
  # count[0] is the number of open paren
  # count[1] is the number of close paren
  counts = deque([[0, 0]]) 

  for i in range(1, 2*num + 1):
    level_size = len(result)
    for _ in range(level_size):
      parens = result.popleft()
      count = counts.popleft()

      # add open paren
      if count[0] < num:
        result.append(parens + '(')
        counts.append([count[0] + 1, count[1]])
      # add close paren
      if count[0] > count[1]:
        result.append(parens + ')')
        counts.append([count[0], count[1] + 1])
     
  return list(result)


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
