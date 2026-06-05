class animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def sound(self):
    print("bark")

class human:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def sound(self):
        print("speak")

    animal1 = animal("dog","british")
    human1 = human("man", "person")

    for x in (animal1, human1):
        x.sound()
        