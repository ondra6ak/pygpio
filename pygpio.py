class Gpio:
    def __init__(self, gpio, direction="out"):
        self.gpio = gpio
        self.path = "/sys/class/gpio/gpio{}/".format(self.gpio)

        open("/sys/class/gpio/export", "w").write(str(self.gpio))
        open(self.path + "direction", "w").write(direction)

    def set(self, value):
        open(self.path + "value", "w").write(str(value))

    def get(self):
        return int(open(self.path + "value", "r").read().replace("\n", ""))

    def toggle(self):
        if self.get() == 0:
            open(self.path + "value", "w").write("1")
        else:
            open(self.path + "value", "w").write("0")
    
    def get_direction(self):
        return open(self.path + "direction", "r").read().replace("\n", "")
    
    def __del__(self):
        open("/sys/class/gpio/unexport", "w").write(str(self.gpio))
