from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.properties import BooleanProperty


class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        super().__init__(**kwargs)
        self.done = False
        self.total = total
        self.current = 0
        my_text = "Прошло секунд: " + str(self.current)

    def restart(self, total):
        self.done = False
        self.total = total
        self.current = 0
        #self.text = "Прошло секунд: " + str(self.current)
        self.start()
    def restart1(self, total):
        self.done = False
        self.total = total
        self.current = 0
        #self.text = "Прошло секунд: " + str(self.current)
        self.start1()
    def restart2(self, total):
        self.done = False
        self.total = total
        self.current = 0
        #self.text = "Прошло секунд: " + str(self.current)
        self.start2()

    def start(self):
        Clock.schedule_interval(self.change, 1)
    def start1(self):
        Clock.schedule_interval(self.change1, 1)
    def start2(self):
        Clock.schedule_interval(self.change2, 1)

    def change(self, dt):
        self.current+=1
        self.text = "Прошло секунд: " + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False
    def change1(self, dt):
        self.current+=1
        self.text = "Прошло секунд: " + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

    def change2(self, dt):
        self.current+=1
        self.text = "Прошло секунд: " + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

