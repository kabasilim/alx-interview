#!/usr/bin/python3
"""
This file contains the pascal_triangle function
"""

def pascal_triangle(n):
  """
  This function generates Pascal's triangle up to the nth row.

  Args:
      n: An integer representing the number of rows in the Pascal's triangle.

  Returns:
      A list of lists containing the integers of Pascal's triangle.
      Returns an empty list if n <= 0.

  Raises:
      ValueError: If n is not an integer.
  """

  if not isinstance(n, int):
      raise ValueError("n must be an integer")

  if n <= 0:
      return []

  triangle = [[1]]  # Initialize with the first row (always [1])

  # Iterate for each row from the second row (index 1) up to n-1
  for i in range(1, n):
      previous_row = triangle[i-1]  # Access the previous row
      current_row = [1]  # Start the current row with 1

      # Generate the middle elements by adding adjacent elements from the previous row
      for j in range(1, i):
          current_row.append(previous_row[j-1] + previous_row[j])

      # Add the final 1 to the current row
      current_row.append(1)

      # Append the completed current row to the triangle
      triangle.append(current_row)

  return triangle

# Example usage (assuming the function is saved in a separate file named 0-pascal_triangle.py)
def print_triangle(triangle):
  """
  Print the triangle in a user-friendly format.
  """
  for row in triangle:
    print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
  try:
    triangle = pascal_triangle(5)
    print_triangle(triangle)
  except ValueError as e:
    print(e)

