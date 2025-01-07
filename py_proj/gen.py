def number_generator():
    num = 0
    while True:
        yield num
        num += 1

# Using the generator
gen = number_generator()
for _ in range(5):
    print(next(gen))  # Prints 0, 1, 2, 3, 4

