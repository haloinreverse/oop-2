class TComplex:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                nums = args[0].replace(' ', '').split('+')
                self.__real_part = float(nums[0])
                self.__im_part = float(nums[1][:-1])
            else:
                self.__real_part = 0
                self.__im_part = 0
        else:
            self.__real_part = args[0]
            self.__im_part = args[1]

    def __str__(self):
        if self.__real_part == 0 and self.__im_part == 0:
            return '0'
        elif self.__real_part == 0:
            return f'{self.__im_part}i'
        elif self.__im_part == 0:
            return f'{self.__real_part}'
        elif self.__im_part < 0:
            return f'{self.__real_part} - {- self.__im_part}'
        else:
            return f'{self.__real_part} + {self.__im_part}'

    def __abs__(self):
        return ((self.__real_part) ** 2 + (self.__im_part) ** 2) ** 0.5

    def __eq__(self, other):
        if self.__real_part == other.__real_part and self.__im_part == other.__im_part:
            return True
        else:
            return False

    def __add__(self, other):
        return TComplex(self.__real_part + other.__real_part, self.__im_part + other.__im_part)

    def __mul__(self, other):
        return TComplex(self.__real_part * other.__real_part - self.__im_part * other.__im_part, self.__real_part * other.__real_part + self.__im_part * other.__im_part)

    def __sub__(self, other):
        return TComplex(self.__real_part - other.__real_part, self.__im_part - other.__im_part)

    def __ne__(self, other):
        return not self == other

    def __truediv__(self, other):
        return TComplex((self.__real_part * other.__real_part + self.__im_part * other.__im_part)/(other.__real_part ** 2 + other.__im_part),
                        (self.__im_part * other.__real_part + self.__real_part / other.__im_part)/(other.__real_part ** 2 + other.__im_part))

