import os
import pandas
from geopy.geocoders import ArcGIS

# Exmplanation for this fix
# https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-the-currently-running-scrip
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


# Open, read and print csv and json with pandas

dataFrameCSV = pandas.read_csv(
    os.path.join(__location__, "supermarkets/supermarkets.csv")
)
# print("thhis is csv\n", dataFrameCSV, "\n\n\n")

dataFrameJSON = pandas.read_json(
    os.path.join(__location__, "supermarkets/supermarkets.json")
)
# print("this is json\n", dataFrameJSON, "\n\n\n")

dataFrameEXC = pandas.read_excel(
    os.path.join(__location__, "supermarkets/supermarkets.xlsx"), sheet_name=0
)
# print("this is excel\n",dataFrameEXC, "\n\n\n")

# Loading a file using a separator
dataFrameSEP = pandas.read_csv(
    os.path.join(__location__, "supermarkets/supermarkets-semi-colons.txt"), sep=";"
)
# print("this is txt using separators\n", dataFrameSEP)

# Loading a txt file with comma separated values, and changing the header row
dataFrameComma = pandas.read_csv(
    os.path.join(__location__, "supermarkets/supermarkets-commas.txt"),
    sep=",",
    header=None,
)

# Setting a custom header row with name of each cell
dataFrameComma.columns = [
    "ID",
    "Address",
    "City",
    "ZIP",
    "Country",
    "Name",
    "Employees",
]

# Setting a custom index
# dataFrameComma.set_index("ID", drop=False, inplace=True)

# Locate specific data from DataFrame
# print(dataFrameComma.loc["2":"4", "Name"] , "\n\n")

# Add another column to the table
# dataFrameComma["Continent"] = dataFrameComma.shape[0]*["North Amerrica"]

# new column Continent is made from Column Country adn 2 more strings
dataFrameComma["Continent"] = dataFrameComma["Country"] + "," + "North America"

# Add another Row - first make new variable, then transpose original table , then add , then transpose again

dataFrameComma_t = dataFrameComma.T
dataFrameComma_t["6"] = [
    "7",
    "My Adress",
    "My City",
    "My ZIP",
    "My Country",
    "My Name",
    "0",
    "My Continent",
]
dataFrameComma = dataFrameComma_t.T

# Combining addresses and ZIP codes
dataFrameComma["Address"] = dataFrameComma["Address"] + "," + dataFrameComma["City"] + "," + dataFrameComma["ZIP"] 

print(dataFrameComma , "\n\n")

# Working with geocodig
nom = ArcGIS()

# Create new column, add all coordinates from every address using geocoder
dataFrameComma["Coordinates"] = dataFrameComma["Address"].apply(nom.geocode)

# Extract latitude and longitude and add to separaate columns
dataFrameComma["Latitude"] = dataFrameComma["Coordinates"].apply(lambda x: x.latitude if x != None else None)
dataFrameComma["Longitude"] = dataFrameComma["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(dataFrameComma)