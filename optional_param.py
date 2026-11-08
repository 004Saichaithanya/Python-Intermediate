# def func(word,freq=2,add=5):
#     print(word*(freq+add))

# func('sai',5)


class myclass:
    def __init__(self, model, year, condition="New", kms=0):
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=False):
        if showAll:
            print(
                "This car is %s bought on %s and condition %s and kms %s"
                % (self.model, self.year, self.condition, self.kms)
            )
        else:
            print("This car is %s bought on %s" % (self.model, self.year))


obj = myclass("Ford", 2030)
obj.display()
