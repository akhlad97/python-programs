import sys

# Check if the correct number of arguments is provided
if len(sys.argv) < 3:
    print("Usage: python script_name.py <integer1> <integer2>")
    sys.exit(1)

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except ValueError:
    print("Error: Both arguments must be integers.")
    sys.exit(1)

z = x + y
print(z)

