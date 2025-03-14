class Eagle:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name}는 날개 길이가 {self.wingspan}m로 하늘을 납니다."