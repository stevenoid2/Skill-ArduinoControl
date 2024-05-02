from mycroft import MycroftSkill, intent_handler
import serial

class ArduinoControlSkill(MycroftSkill):
    def __init__(self):
        super(ArduinoControlSkill, self).__init__(name="ArduinoControlSkill")
        self.leg = serial.Serial('/dev/ttyACM1', 115200)  # Adjust as necessary
        self.eye = serial.Serial('/dev/ttyACM0', 115200)  

    @intent_handler('perlin.intent')
    def handle_perlin(self, message):
        self.eye.write('G'.encode('ascii'))
        self.leg.write('G'.encode('ascii'))
        self.speak("I'm confused")

    @intent_handler('party.intent')
    def handle_party(self, message):
        self.eye.write('F'.encode('ascii'))
        self.leg.write('F'.encode('ascii'))
        self.speak("Party is on")

    @intent_handler('bright.intent')
    def handl_bright(self, message):
        self.eye.write('J'.encode('ascii'))
        self.leg.write('J'.encode('ascii'))
        self.speak("Light is up")

    @intent_handler('dim.intent')
    def handle_dim(self, message):
        self.eye.write('K'.encode('ascii'))
        self.leg.write('K'.encode('ascii'))
        self.speak("Light is down")

    @intent_handler('relax.intent')
    def handle_relax(self, message):
        self.eye.write('C'.encode('ascii'))
        self.leg.write('C'.encode('ascii'))
        self.speak("I'm chilling")

    @intent_handler('angery.intent')
    def handle_angery(self, message):
        self.eye.write('D'.encode('ascii'))
        self.leg.write('D'.encode('ascii'))
        self.speak("I'm angery")

    @intent_handler('stand.intent')
    def handle_stand(self, message):
        self.leg.write('U'.encode('ascii'))
        self.eye.write('U'.encode('ascii'))
        self.speak("Standing up")

    @intent_handler('walk.intent')
    def handle_walk(self, message):
        self.leg.write('W'.encode('ascii'))
        self.eye.write('W'.encode('ascii'))
        self.speak("Walking")

    @intent_handler('stop.intent')
    def handle_stop(self, message):
        self.leg.write('S'.encode('ascii'))
        self.eye.write('S'.encode('ascii'))
        self.speak("all motor function stopped")

    def shutdown(self):
        if self.leg.is_open:
            self.leg.close()
        if self.eye.is_open:
            self.eye.close()

def create_skill():
    return ArduinoControlSkill()
