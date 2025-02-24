# Create a Stack
def get_stack():
    return []

# Check empty
def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if(check_empty(stack)):
        return "Stack underflow"
    return stack.pop()

stack = get_stack()
push(stack, '1')
push(stack, '2')
push(stack, '3')
push(stack, '4')
push(stack, '5')

print(pop(stack))
print(stack)