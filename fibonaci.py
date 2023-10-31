def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

terms = int(input("Enter the number of terms: "))

if terms > 0:
    print("Fibonacci sequence:", end=" ")
    for i in range(terms):
        print(fibo(i), end=" ")
    print()  # Add a newline character to separate the output from the prompt
else:
    print("Please enter a number greater than 0.")
