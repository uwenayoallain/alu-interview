# Minimum Operations

This project implements `minOperations(n)`, a function that returns the fewest
number of operations required to obtain exactly `n` characters `H` in a file,
starting from a single `H`, when the only allowed operations are:

- Copy All
- Paste

If `n` is impossible to achieve, the function returns `0`.

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 14.04 LTS with `python3` (3.4.3)
- All files end with a new line
- The first line of all Python files is exactly `#!/usr/bin/python3`
- Code is documented and follows PEP 8 (1.7.x)
- All Python files are executable

## Usage
Example test file:

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
```

Expected output:

```
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```
