

#inheritance
class asianperson(person):
    def __init__(self, name, age, country, hobby):
        super().__init__(name , age)
        self.country = country
    def full_name (self):
        return f"{self.name} {self.age} {self.country} {self.hobby}"
        my_asian_person = asianperson("hehe","20","nepal","singing")
        print(my_asian_person.full_name())
        print(my_asian_person.name)
        print(my_asian_person.age)
        print(my_asian_person.country)
        print(my_asian_person.hobby)