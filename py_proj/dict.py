def greet_user(names):
    print("Your message will be sent to each user in the list") #"""Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
greet_user(["tom", "sally", "jane","Sandeep"])
print("Ending code")
