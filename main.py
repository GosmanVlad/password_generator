import string
import random
import sys

max_chars = 18
min_chars = 12
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = "!?#@"

if __name__ == "__main__":
   if sys.argv[1] == '-use-dict':
       print("Get data from file")