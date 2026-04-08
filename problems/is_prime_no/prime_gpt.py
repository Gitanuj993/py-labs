import timeit # this is optional
# actual funcitons
def prime() :
    # Taking user input from the user
    n = int(input("Enter range upto n : "))

    # initially assume all numbers are prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    count_prime = 0
    count_composite = 0

    for i in range(2, n + 1):
        if is_prime[i]:
            count_prime += 1
        else:
            count_composite += 1

    print(f"Total number of prime numbers is: {count_prime}")
    print(f"Total number of composite numbers is: {count_composite}")


# To measure execution time of code , code copied from chatGpt
execution_time = timeit.timeit(stmt="prime()", globals=globals(), number=1)
print(f"Execution time: {execution_time:.6f} seconds")
