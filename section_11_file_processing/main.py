import os

# Exmplanation for this fix
# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "vegetables.txt"), "w") as f:
    content = f.read()

f.close()

print(content)

# Append and read the content of the file

with open('file.txt', '+a') as file:
    content = file.write("Some new randon text")
    file.seek(0)
    content = file.read()
    print(content)
