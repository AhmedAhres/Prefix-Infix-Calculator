import sys

def build_stack_prefix(inp):
    '''
    Function to solve the prefix calculator with no parenthesis(part one)
    In order to solve the problem, we will be using a stack data structure
    This function creates a stack out of the current input
    We keep building the stack until having only 1 element which is the result
    '''
    # If input contains zero or one number, we simply return the input
    if len(inp) == 0 or len(inp) == 1:
        return inp
    stack = []
    # We remove the space
    # Variable to keep track of the current result
    current_result = 0
    operators = ['+', '-', '*', '/']
    # We loop through the characters
    for char in inp:
        if char in operators:
            stack.append(char)
        # If the current number is a digit and the one before is a digit
        # We run the operation
        elif char.isdigit():
            if stack[-1].isdigit():
                # We take the last digit before the current one
                last_digit = stack.pop()
                # We run the operation depending on the operator
                # There must be a way to optimize this, using a dictionary
                # to match the char to the cporresponding operator
                # Due to time constraints, I will solve this trivially
                if stack[-1] == '+':
                    current_result = int(int(last_digit) + int(char))
                elif stack[-1] == '-':
                    current_result = int(int(last_digit) - int(char))
                elif stack[-1] == '/':
                    current_result = int(int(last_digit) / int(char))
                elif stack[-1] == '*':
                    current_result = int(int(last_digit) * int(char))
                # We remove the operator
                stack.pop()
                # We append the current number to keep track of it
                # in the next operation
                stack.append(str(current_result))
            else:
                # If we have an operator before the current digit, we add
                # it to the stack
                stack.append(char)
    # Return the stack
    return stack
    
def prefix_calculator(inp):
    '''
    Function to solve the prefix calculator with no parenthesis(part one)
    In order to solve the problem, we will be using a stack data structure
    '''
    # We pre-process the input by removing the spaces
    inp = inp.split(" ")
    # We build the stack
    stack = build_stack_prefix(inp)
    # We keep building the stack until there is only one element
    # The last element is the result
    while len(stack) > 1:
        stack = build_stack_prefix(stack)
    return stack[0]
    
    
def infix_calculator(inp):
    '''
    Function to solve the prefix calculator with no parenthesis(part one)
    In order to solve the problem, we will be using a stack data structure
    '''
    # We pre-process the input by removing the spaces
    inp = inp.split(" ")
    # We build the stack
    stack = build_stack(inp)
    # We keep building the stack until there is only one element
    # The last element is the result
    while len(stack) > 1:
        stack = build_stack(stack)
    return stack[0]
    
# Execute main function
if __name__ == '__main__':
    print("Tests for Prefix calculator...")
    print(prefix_calculator("3"))
    print(prefix_calculator("+ 1 2"))
    print(prefix_calculator("+ 1 * 2 3"))
    print(prefix_calculator("+ * 1 2 3"))
    print(prefix_calculator("- / 10 + 1 1 * 1 2"))
    print(prefix_calculator("- 0 3"))
    print(prefix_calculator("+ 0 3"))
    print(prefix_calculator("/ 3 2"))
