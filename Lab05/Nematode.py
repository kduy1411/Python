class Nematode:
    def __init__(self,bodyLength: float, gender: str,age: int) -> None:
        self.bodyLength = bodyLength
        self.gender = gender
        self.age = age
    
    def __str__(self):
        return "Nematode details:\nbody length : {}\ngender : {}\nage :{}".format(self.bodyLength,self.gender,self.age)
    
    def __repr__(self):
        return "{0}({1},{2},{3})".format(self.__class__.__name__,self.bodyLength,self.gender,self.age)
