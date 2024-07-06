class LengthConverter:
    Koef_length = 3.28084
    Koef_kl_mili = 1.609344
    Koef_jrd_metr = 1.093613

    @staticmethod
    def meters_to_feet(meters):
        return meters * LengthConverter.Koef_length

    @staticmethod
    def feet_to_meters(feet):
        return feet / LengthConverter.Koef_length

    @staticmethod
    def kl_to_mili(kl):
        return kl / LengthConverter.Koef_kl_mili

    @staticmethod
    def mili_to_km(mili):
        return mili * LengthConverter.Koef_kl_mili

    @staticmethod
    def jrd_metr(metr):
        return metr / LengthConverter.Koef_jrd_metr

    @staticmethod
    def metr_jrd(jrd):
        return jrd * LengthConverter.Koef_jrd_metr


print(LengthConverter.meters_to_feet(int(input("Введи величину в метрах : "))))
print(LengthConverter.feet_to_meters(int(input("Введи величину в футах : "))))
print(LengthConverter.kl_to_mili(int(input("Введи величину в километрах : "))))
print(LengthConverter.mili_to_km(int(input("Введи величину в милях : "))))
print(LengthConverter.jrd_metr(int(input("Введи величину в ярдах : "))))
print(LengthConverter.metr_jrd(int(input("Введи величину в метрах : "))))