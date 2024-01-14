all_strings = []
interrogatives = ('how', 'what', 'when', 'why')

# This program is made to cumulate basic string manipulation, while loops, and use of lists.

# if string starts with interrogatives add '?' at the end of the string
# else add fullstop
def make_string_from(phrase): 
    capitelized_string = phrase.capitalize()
    if phrase.lower().startswith(interrogatives):
        return "{}?".format(capitelized_string)
    else:
        return "{}.".format(capitelized_string)

# if user enter qqq, exit program, and print all senteces that are said 
# else, keep asking for input
while True:
    user_said = input("kazi Miki: ")

    if user_said == "qqq":
        print(" ".join(all_strings))
        break
    
    all_strings.append(make_string_from(user_said))
