class PaintWindow:

    # Constructor -> Executed when we create an Object
    def __init__(self):
        print(">> Paint Window Created and you can Paint")

    # Destructor -> Executed when we delete an Object
    def __del__(self):
        print(">> Paint Window is closed/deleted from memory")


# Object Construction -> PaintWindow() -> Will execute __init__ i.e. Constructor
pRef = PaintWindow()
del pRef            # -> execute __del__ i.e. Destructor