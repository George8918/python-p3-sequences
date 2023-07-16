def print_fibonacci(length):
    fib_sequence = [0, 1]  # Starting with the initial Fibonacci numbers

    if length < 0:
        print("Invalid length. Please provide a non-negative integer.")
        return

    if length == 0:
        print([])  # Print an empty list
        return
    
    if length == 1:
        print([fib_sequence[0]])  # Print a single element list
        return

    if length == 2:
        print(fib_sequence)  # Print the initial Fibonacci numbers as a list
        return

    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    print(fib_sequence) 