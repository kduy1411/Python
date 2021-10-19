#cau a:
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
#cau b:
    def is_larger(self, other):
        if isinstance(other,Country):
            return self.area > other.area
        else:
            print("Both objects need to be from class Country")
            return -1
#cau c:   
    def population_density(self):
        return (self.population / self.area)
#cau d:
    def __str__(self):
        return ("{0} has a population of {1} and its area is {2} square kilometers.".format(self.name,self.population,self.area))
#cau e:    
    def __repr__(self):
        return "Country('{0}', {1}, {2})".format(self.name, self.population, self.area)
