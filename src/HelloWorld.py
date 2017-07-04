import math

__author__ = 'Alex Odago'
class HelloWorld:
    def sayHello(self):
        age = int(input("Enter your Age : "))
        years_of_study = math.sqrt(4)
        new_age = age + years_of_study
        if new_age >=40:
            decision = 'You will be too old. Declined.'
        elif new_age < 40 and new_age >=25:
            decision = 'Your application is Approved'
        else:
            decision = 'You are too young to enter this course'
        print("You will be :", new_age, " when you finish your studies.",decision)
    def listOfCities(self):
        cities = ['Manila','Antananarivo','Johannesburg','Cancun','Vladivostok','Minneapolis','Lisbon']
        cities.remove('Cancun')
        del cities[3]
        print(cities)
        cities.append('Maputo')
        print(cities)
# create dictionary, add items, use get and check if variable is None
    def dictionaryOfCountries(self):
        countries = {'Manila':'Phillipines','Johannesburg':'South Africa','Cancun':'Mexico','Minneapolis':'USA','Vladivostok':'Russia','Lisbon':'Portugal'}
        countries['Luanda'] = 'Angola'
        del countries['Cancun']
        selectedCity = input("Please enter your city : ")
        myCountry = countries.get(selectedCity)
        if not myCountry:
            print('The country where ' + selectedCity + ' is located is unknown')
        else:
            print('Your country is ' + myCountry)
HelloWorld().sayHello()
HelloWorld().listOfCities()
HelloWorld().dictionaryOfCountries()
