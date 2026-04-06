import random
import time
import matplotlib.pyplot as plt
from hvlcs import hvlcs
import os

def generate_input_file():
    os.makedirs("data", exist_ok=True)
    for i in range(10):
        alphabet = random.sample('abcdefghijklmnopqrstuvwxyz', random.randint(2, 26))
        values = {char: random.randint(1, 25) for char in alphabet}

        k = random.randint(25, 100)
        A = ''.join(random.choices(alphabet, k=k))
        B = ''.join(random.choices(alphabet, k=k))

        with open(f"data/file{i+1}.in", "w") as f:
            f.write(f"{len(alphabet)}\n")
            for char, val in values.items():
                f.write(f"{char} {val}\n")
            f.write(f"{A}\n")
            f.write(f"{B}\n")

def read_input_file(filepath):
    with open(filepath, "r") as f:
        k = int(f.readline().strip())
        vA = {}
        for _ in range(k):
            l = f.readline().split()
            vA[l[0]] = int(l[1])

        A = f.readline().strip()
        B = f.readline().strip()
    return vA, A, B


def run():
    runtimes = []
    for i in range(10):
        vA, A, B = read_input_file(f"data/file{i+1}.in")

        start = time.time()
        hvlcs(A, B, vA)
        end = time.time()

        elapsed = end - start
        runtimes.append((len(A), len(B), elapsed))

    return runtimes

def plot_runtimes(runtimes):
    labels = [f"file{i+1}\n({r[0]} by {r[1]})" for i, r in enumerate(runtimes)]
    times = [r[2] for r in runtimes]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, times)
    plt.xlabel("Input file size")
    plt.ylabel("runtimes")
    plt.title("HVLCS runtimes")
    plt.savefig("data/runtime_graph")

generate_input_file()
runtimes = run()
plot_runtimes(runtimes)