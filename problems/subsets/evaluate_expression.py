"""
Given an expression containing digits and operations (+, -, *), 
find all possible ways in which the expression can be evaluated 
by grouping the numbers and operators using parentheses.

Soln: If we know all of the ways to evaluate the left-hand 
side (LHS) of an expression and all of the ways to evaluate 
the right-hand side (RHS), we can determine all of the ways 
to evaluate the entire expression.

Time complexity: O(N * 2^N)

Space complexity: O(2^N)
"""

def diff_ways_to_evaluate_expression(input):
  # base case
  if input.isdigit():
    return [int(input)]
  
  result = []
  for i in range(len(input)):
    char = input[i]
    
    if char.isdigit():
      continue

    LHS = diff_ways_to_evaluate_expression(input[:i])
    RHS = diff_ways_to_evaluate_expression(input[i+1:])

    for left_part in LHS:
      for right_part in RHS:
        if char == '+':
          result.append(left_part + right_part)
        elif char == '-':
          result.append(left_part - right_part)
        else:
          result.append(left_part * right_part)
   
  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
