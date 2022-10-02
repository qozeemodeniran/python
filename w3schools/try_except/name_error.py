try:
    print(y)
except NameError:
    print("Variable y is not defined")
except:
    print("Something else went wrong")