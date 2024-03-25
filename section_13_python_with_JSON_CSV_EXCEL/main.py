import os
import pandas

# Exmplanation for this fix
# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# Open, read and print csv and json with pandas

dataFrameCSV = pandas.read_csv(
    os.path.join(__location__, "supermarkets/supermarkets.csv")
)
print("thhis is csv\n", dataFrameCSV, "\n\n\n")

dataFrameJSON = pandas.read_json(
    os.path.join(__location__, "supermarkets/supermarkets.json")
)
print("this is json\n", dataFrameJSON, "\n\n\n")

dataFrameEXC = pandas.read_excel(
    os.path.join(__location__, "supermarkets/supermarkets.xlsx"), sheet_name=0
)
print("this is excel\n",dataFrameEXC, "\n\n\n")

# Loading a file using a separator
dataFrameSEP = pandas.read_csv(
    os.path.join(__location__, 'supermarkets/supermarkets-semi-colons.txt'), sep=";"
)
print("this is txt using separators\n", dataFrameSEP)