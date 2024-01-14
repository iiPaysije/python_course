import os

# Exmplanation for this fix 
# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

f = open(os.path.join(__location__, "fruits.txt"))
print(f.read())
