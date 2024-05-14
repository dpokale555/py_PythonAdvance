import random

# Create an empty set to store generated combinations
generated_combinations = set()

# Generate and print unique combinations
while len(generated_combinations) < 6:
    otp = random.randint(1, 6)
    if otp not in generated_combinations:
        print(otp, end="")
        generated_combinations.add(otp)