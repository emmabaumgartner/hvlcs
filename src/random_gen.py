import random
from hvlcs import hvlcs, backtracking

def generate_string_and_values():
    string_A = ""
    string_B = ""
    for _ in range(25, 50):
        string_A += random.choice('abcdefghijklmnopqrstuvwxyz') * random.randint(5, 25)
    for _ in range(25, 50):
        string_B += random.choice('abcdefghijklmnopqrstuvwxyz') * random.randint(5, 25)
    values_A = []
    values_B = []
    for _ in range(len(string_A)):
        values_A += [random.randint(1, 25)]
    for _ in range(len(string_B)):
        values_B += [random.randint(1, 25)]
    return string_A, string_B, values_A, values_B

def run_gen():
    num_tests = 3
    for i in range(num_tests):
        string_A, string_B, values_A, values_B = generate_string_and_values()

        with open(f"data/file{i+1}.in", "w") as f:
            f.write(f"{string_A} {string_B}\n")
            f.write(" ".join(map(str, values_A)) + "\n")
            f.write(" ".join(map(str, values_B)))
run_gen()