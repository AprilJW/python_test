# 4.温度转化
class ConvertTemperature:
    def __init__(self, value, unit='C'):
        if unit == 'F':
            self.value = 5 * (value - 32) / 9
        elif unit == 'k':
            self.value = value - 273.15
        else:
            self.value = value

    @classmethod
    def convert_F2C(cls, F):
        return 5 * (F - 32) / 9

    @classmethod
    def convert_C2F(cls, C):
        return 9 * C / 5 + 32

    @classmethod
    def convert_C2k(cls, C):
        return C + 273.15


print(ConvertTemperature.convert_C2F(37))
print(ConvertTemperature.convert_F2C(98.6))
print(ConvertTemperature.convert_C2k(37))


# 4. 温度转化方法2
class ConvertTemperature:
    def __init__(self, value, unit='C'):
        self._F = None
        self._C = None
        self._k = None
        if unit == 'F':
            self._value = self._convert_F2C(value)

        elif unit == 'k':
            self._value = self._convert_k2C(value)

        else:
            self._value = value

    @property
    def F(self):
        return self._convert_C2F(self._value)

    @property
    def k(self):
        return self._convert_C2k(self._value)

    @property
    def C(self):
        return self._value

    def _convert_C2F(self, C):
        return C * 9 / 5 + 32

    def _convert_C2k(self, C):
        return C - 273.15

    def _convert_F2C(self, F):
        return 5 * (F - 32) / 9

    def _convert_k2C(self, k):
        return k + 273.15

t = ConvertTemperature(37, 'C')
print(t.C)
print(t.F)
print(t.k)

t = ConvertTemperature(98.6, 'F')
print(t.C)
print(t.F)
print(t.k)

t = ConvertTemperature(-236.14999999, 'k')
print(t.C)
print(t.F)
print(t.k)