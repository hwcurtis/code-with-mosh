def greet(name):
    print(f"hi {name}")

    # functions that preform a task * in python greet and print are type 1 function
    # funtions that return a value  # round calculates the value and returns it to the caller

    def get_greeting(name):
        return f"hi {name}"

    message = get_greeting("John")   # best function to use
    print(message)                   #
    file = open("context.txt,"w")
    file.write(message)