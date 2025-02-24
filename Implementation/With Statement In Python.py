import os

with open('C:\Workspace\Python\AsQueue.py', 'r') as f:
    print(f.read())

print(os.getcwd())

# Custome class with __enter__ & __exit__

class AddWithSupport:
    def __enter__(self):
        print("Entering...")
        return 'Hola!'
    
    def __exit__(self, *args, **kwargs):
        print('Exiting...')

with AddWithSupport() as a:
    print(a)


# Add Context Manager Protocol using contextlib decorator - @ContextManager
## Function based contextmanager
from contextlib import contextmanager

@contextmanager
def customeContextManager():
    print('Entering...')
    yield 'Hello!!'
    print('Exiting...')

with customeContextManager() as cm:
    print(cm)