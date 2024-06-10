class MarkDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        if value < self.min_value:
            instance._value = 0
            raise ValueError(f"Значение должно быть больше {self.min_value}")
        elif value > self.max_value:
            instance._value = 10
            raise ValueError(f"Значение должно быть меньше {self.max_value}")
        else:
            instance._value = value


class Mark:
    value = MarkDescriptor(0, 10)


NewMark = Mark()
Mark.value = 8 # Значение в пределах допустимого, все хорошо
print(Mark.value)

Mark.value = 14 # Значение больше 10, ошибка
print(Mark.value)


