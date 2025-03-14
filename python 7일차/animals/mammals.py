class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return f"{self.name}는 {self.breed} 종이며 '멍멍' 짖습니다."