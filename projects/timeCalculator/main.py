# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

print(add_time("11:59 PM", "24:05"))

# Run unit tests automatically
main(module='time_calculator', exit=False)

# total hours - 47
# total mins - 64

# new hour - 24
# new min - 4