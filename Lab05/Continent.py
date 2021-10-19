from Country import Country
class Continent:
    def __init__(self,name,countries):
        self.name = name
        self.countries = countries

    def total_population(self):
        sum = 0
        for country in self.countries:
            sum += country.population
        return sum

    def __str__(self):
        string = self.name + '\n'
        for country in self.countries:
            string += '{} has a population of {} and is {} square km.'.format(country.name, country.population, country.area) + '\n'
        return string
