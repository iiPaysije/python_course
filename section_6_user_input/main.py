def make_greet():
    """function receives firstname from user
        if its a digit, it handles the error
        else it prints out a greet in uppercase 
    """
    user_name = input("enter your firstname: ")
    if user_name.isdigit():
        user_name = input(
            "Please do not use digits in your name, enter your name again: "
        )

    greet = f"Hello {user_name.upper()}"
    return greet


print(make_greet())
