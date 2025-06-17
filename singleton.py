''' 1) This class ensures there is only one language setting used across the entire app.
No matter where you access it, the selected language stays the same everywhere. '''
class LanguageManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.language = "English"
        return cls._instance

    def set_language(self, language):
        self.language = language
        print(f"Language set to: {language}")

    def get_language(self):
        print(f"Current language: {self.language}")
        return self.language

language1 = LanguageManager() # Only one language setting 
language2 = LanguageManager()

language1.set_language("French")
language2.get_language()

print(language1 is language2)  


'''2) This class manages the temperature setting as a single shared instance. 
Changing the temperature from anywhere updates the same thermostat.'''
class Thermostat:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._temperature = 20  # Default 
        return cls._instance

    def set_temperature(self, temp):
        self._temperature = temp
        print(f"Temperature set to {temp}°C")

    def get_temperature(self):
        print(f"Current temperature: {self._temperature}°C")
        return self._temperature

thermo1 = Thermostat()
thermo2 = Thermostat()

thermo1.set_temperature(25)
thermo2.get_temperature()
thermo2.set_temperature(18)
thermo1.get_temperature()

print(thermo1 is thermo2)  
