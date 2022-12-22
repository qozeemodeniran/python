x = 7

def Myfunction():
    # global x
    x = 5
    print("local variable: ", x)

Myfunction()

print("Global variable: ", x)