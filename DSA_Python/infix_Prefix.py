# Dictionary for operator precedence
op = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

# Function to reverse infix expression and adjust parentheses
def reverse_infix(exp):
    rev = ""
    for x in exp[::-1]:
        if x == "(":
            rev += ")"
        elif x == ")":
            rev += "("
        else:
            rev += x
    return rev

# Function to convert infix to postfix
def infix_to_postfix(exp):
    output = []
    stack = []

    for x in exp:
        if x.isalnum():  # If operand, add to output
            output.append(x)
        elif x in op:  # Operator handling
            while (stack and stack[-1] != '(' and
                   op.get(x, 0) <= op.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(x)
        elif x == '(':  # Opening parenthesis
            stack.append(x)
        elif x == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # Pop the '('

    # Pop remaining operators from the stack
    while stack:
        output.append(stack.pop())

    return output

# Main function to convert infix to prefix
def infix_to_prefix(infix_exp):
    # Step 1: Reverse the infix expression
    rev_infix = reverse_infix(infix_exp)

    # Step 2: Get postfix of the reversed infix expression
    postfix = infix_to_postfix(rev_infix)

    # Step 3: Reverse the postfix to get prefix
    prefix = reverse_infix("".join(postfix))

    return prefix

# Input infix expression from user
infix_exp = input("Enter expression (infix): ")

# Convert infix to prefix
prefix_expr = infix_to_prefix(infix_exp)

# Output the prefix expression
print(f"Prefix Expression: {prefix_expr}")
