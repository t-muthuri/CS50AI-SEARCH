str = "This is Python\n"

print(str.splitlines()) # => ['This is Python']
print(str.split()) # => ['This', 'is', 'Python']
print(str.splitlines(keepends=True)) # => ['This is Python\n']