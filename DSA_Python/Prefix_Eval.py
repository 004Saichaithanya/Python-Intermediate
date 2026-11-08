# Function to evaluate a prefix expression
def evaluate_prefix(prefix_exp):
    stack = []
    
    # Traverse the prefix expression from right to left
    for symbol in prefix_exp[::-1]:
        # If the symbol is an operand, push it to the stack
        if symbol.isdigit():
            stack.append(int(symbol))
        # If the symbol is an operator, pop two operands, evaluate and push the result back
        elif symbol in ['+', '-', '*', '/', '^']:
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            if symbol == '+':
                result = operand1 + operand2
            elif symbol == '-':
                result = operand1 - operand2
            elif symbol == '*':
                result = operand1 * operand2
            elif symbol == '/':
                result = operand1 / operand2
            elif symbol == '^':
                result = operand1 ** operand2
            
            # Push the result back onto the stack
            stack.append(result)
    
    # The last item in the stack will be the final result
    return stack.pop()

# Input prefix expression from user
prefix_exp = input("Enter prefix expression: ")

# Evaluate the prefix expression
result = evaluate_prefix(prefix_exp)

# Output the result
print(f"Result of prefix evaluation: {result}")
