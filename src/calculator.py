def calculator(operation, num1, num2):
    """
    Performs basic arithmetic operations on two numbers.
    
    Args:
        operation (str): The operation to perform. Supported operations:
                'add', 'subtract', 'multiply', or 'divide'.
        num1 (float): The first number.
        num2 (float): The second number.
    
    Returns:
        float: The result of the operation.
    
    Raises:
        ValueError: If the operation is unsupported.
        ZeroDivisionError: If division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: '{operation}'. Supported operations are 'add', 'subtract', 'multiply', and 'divide'.")
