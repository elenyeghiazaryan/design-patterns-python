''' Facade pattern example: Smart Home System
Instead of controlling lights, music, and security one by one, the SmartHomeFacade provides 
one simple method (arrive_home) that triggers all systems together'''
class Lights:
    def turn_on(self):
        print("Lights turned ON")

class SecuritySystem:
    def disarm(self):
        print("Security system disarmed")

class MusicSystem:
    def play_favorite_song(self):
        print("Playing your favorite music")

class SmartHomeFacade: # Facade
    def __init__(self):
        self.lights = Lights()
        self.security = SecuritySystem()
        self.music = MusicSystem()

    def arrive_home(self):
        print("I'm home!")
        self.security.disarm()
        self.lights.turn_on()
        self.music.play_favorite_song()


home = SmartHomeFacade()
home.arrive_home()
