import argparse
import random

# Generate random numbers
numbers = []
for _ in range(1000):
    number = random.randint(1, 1000)
    numbers.append(number)

# Write the numbers to a file
with open("numbers.txt", "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, required=True, help="an integer for the value N, which will be output length")
parser.add_argument("--input-file", type=str, required=True, help="A string representing a path to an input file")
parser.add_argument("--output-file", type=str, required=True, help="A string representing a path to an output file")
args = parser.parse_args()
n = args.n
input_file = args.input_file
output_file = args.output_file

# Read the input file
with open(input_file, "r") as f:
    lines = f.readlines()

# Get the N largest numbers
numbers = []
for line in lines:
    number = int(line.strip())
    numbers.append(number)
numbers = sorted(numbers, reverse=True)[:n]

# Write the result to the output file
with open(output_file, "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")
