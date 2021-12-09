from django import forms
from service_objects.services import Service


class ChangeOfItemTypeName(Service):
    """Сервис для изменения наименования типа предмета"""

    name_kind_lesson = forms.CharField()

    def process(self):

        name = self.cleaned_data["name_kind_lesson"]

        if name == "л.":
            return "Лекция"
        elif name == "лаб.":
            return "Лабораторная"
        elif name == "пр.":
            return "Практика"
        elif name == "фв":
            return "Практика"
        else:
            return " "
