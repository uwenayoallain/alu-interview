# Minimum Operations

## Description
This project involves calculating the minimum number of operations required to achieve exactly `n` characters in a file, starting with a single character 'H'. The operations allowed are "Copy All" and "Paste". 

The goal is to determine the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should be documented
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Usage
To use the `minOperations` function, you need to import it and call it with a positive integer `n`.

### Example
```python
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
