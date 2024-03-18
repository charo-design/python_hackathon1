def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    if n ==0:
      return[]
    else:
      return[0]
    # Complete here
  else:
    a, b = 0,1
    fibonacci_sequence=[]
    for _ in range(2, n + 1):
      c = a + b
      fibonacci_sequence.append(c)
      a, b = b, c  # Update a and b for next iteration
    return fibonacci_sequence
    # complete here
    

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence=fibonacci(num_terms)

# Print the Fibonacci sequence
print(fibonacci_sequence)


# Your program should:

# Ask the user to input the value of n.
# Create a function that takes n as a parameter and returns a list containing the first n terms of the Fibonacci sequence.
# Print the generated Fibonacci sequence.