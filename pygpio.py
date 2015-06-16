class Gpio:
    def __init__(self, gpio, direction="out"):
        self.gpio = gpio
        self.direction = direction
        self.path = "/sys/class/gpio{}/".format(self.gpio)
        
        open("/sys/class/gpio/export", "w").write(str(self.gpio))
        open(self.path + "direction", "w").write(self.direction)

    def set(self, value):
        self.value = value
        open(self.path + "value", "w").write(str(value))

    def get(self):
        return open(self.path + "value", "r").read()

    def toggle(self):
        if self.value == 0:
            open(self.path + "value", "w").write("1")
            self.value = 1
        else:
            open(self.path + "value", "w").write("0")
            self.value = 0
    
    def __del__(self):
        open("/sys/class/unexport", "w").write(str(self.gpio))
