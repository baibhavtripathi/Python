# plain subtitution of values
print('This is %s'%'Python')

# Multiple substitution of values needs to be in tuple
print('This is %s %s language'%('Python', 'programming'))

# Convertion of values
print('This is %d'%3.14)
print('This is %f'%3)
print('This is 0x%x'%49)

# Padding and aligning strings
print('This is %10s'%('Python'))

# Truncating long strings
print('This is %.5s'%('Python'))

# Combining padding and truncating
print('This is %10.5s'%('Python'))

# Using the old style with dictionaries
print('This is %(language)s'%{"language":"Python"})

# Using the old style with lists
print('This is %s %s language'%["Python", "programming"])