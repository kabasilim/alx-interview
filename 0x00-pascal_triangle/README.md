# Pascal's Triangle Generator
This Python script 0-pascal_triangle.py contains a function pascal_triangle(n) that generates Pascal's triangle up to the specified level n and returns it as a list of lists of integers.

## Functionality
- The function pascal_triangle(n) generates Pascal's triangle up to level n.
- It returns an empty list if n is less than or equal to 0.
- It assumes that n will always be an integer.
### Usage
To use this script, follow these steps:

1. Ensure you have Python installed on your system.
2. Save the script 0-pascal_triangle.py in your working directory.
3. Import the function pascal_triangle in your Python code.
4. Call the function with the desired level of Pascal's triangle as an argument.
5. The function will return the Pascal's triangle up to the specified level.
```
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```
<b>This will output:</b>

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]

```
`
