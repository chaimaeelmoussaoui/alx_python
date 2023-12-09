s = Square(5)
print(s.get_size()) # Output: 5

s.set_size(10)
print(s.get_size()) # Output: 10

s.set_size(-5) # Raises ValueError: Size must be non-negative