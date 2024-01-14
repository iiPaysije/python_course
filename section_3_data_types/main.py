possible_dates = list(range(1, 32))

# Average in a list
avg_date = sum(possible_dates) / len(possible_dates)
print(avg_date, "is average date")

# Max in a list
max_date = max(possible_dates)
print(max_date, "is max date")

# Count occurence of given value
numof_10 = list.count(possible_dates, 10)
print(numof_10, "number of tens")

# a simple dictionary
ocene = {"pera": 10,
         "mika": 7,
         "zika": 8}

print(sum(ocene.values()) / len(ocene), 'is average grade of following students:', ocene.keys())