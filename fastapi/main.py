import atexit
class TemperatureConverter:
    count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.count += 1
        return (celsius * 1.8) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_count():
        return TemperatureConverter.count

print(TemperatureConverter.celsius_to_fahrenheit(int(input("Введи температуру в Цельсиях"))))  # градусы Цельсия в Фаренгейты
print(TemperatureConverter.fahrenheit_to_celsius(int(input("Введи температуру в Фарингейтах"))))  #Фаренгейт в Цельсии
print(TemperatureConverter.get_count())
    # def at_exit(self):
    #     spi.close()
    #     GPIO.cleanup