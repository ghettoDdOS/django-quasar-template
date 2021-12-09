import io

import jinja2
import xlsxwriter
from config.settings import TEMPLATES_DIR
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import dateformat
from django.views import View
from docxtpl import DocxTemplate
from num2words import num2words
from rest_framework.response import Response
from rest_framework.serializers import (
    CharField,
    IntegerField,
    Serializer,
    SerializerMethodField,
)
from rest_framework.views import APIView


def num2words_filter(number):
    """
    Функция обертка для создания фильтра jinja2
    которая преобразует числов в его текстовое представление
    на русском языке
    """
    return num2words(number, lang="ru")


class DocxTemplateView(View):
    """
    Базовый класс представления для генерации .docx документа
    на основе jinja2 шаблона.

    Подробнее: [docxtpl](https://docxtpl.readthedocs.io/en/latest/)
    """

    template_name = None
    file_name = "file"
    not_fount_template_url = "/"

    def get(self, request, *args, **kwargs):
        tempate = self.get_template_path(**kwargs)

        if not tempate:
            return redirect(self.not_fount_template_url)

        doc = DocxTemplate(tempate)
        jinja_env = jinja2.Environment()
        jinja_env.filters["date_format"] = dateformat.format
        jinja_env.filters["num2words"] = num2words_filter
        doc.render(self.get_context_data(**kwargs), jinja_env)
        byte_file = io.BytesIO()
        doc.save(byte_file)
        response = HttpResponse(
            byte_file.getvalue(), content_type="application/msword"
        )
        file_name = self.get_file_name(**kwargs)
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{file_name}.docx"'
        return response

    def get_template_path(self, **kwargs):
        template_name = self.get_template_name(**kwargs)

        if not template_name:
            return None

        return f"{TEMPLATES_DIR}/{template_name}"

    def get_template_name(self, **kwargs):
        return self.template_name

    def get_file_name(self, **kwargs):
        return self.file_name

    def get_context_data(self, **kwargs):
        return {}


class XLSXView(View):
    """
    Базовый класс представления для генерации .xlsx документа.

    Подробнее: [xlsxwriter](https://xlsxwriter.readthedocs.io/)
    """

    file_name = "file"

    def get(self, request, *args, **kwargs):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        self.create_file(
            self.get_context_data(**kwargs),
            workbook,
            worksheet,
            **kwargs,
        )

        workbook.close()
        output.seek(0)

        file_name = self.get_file_name(**kwargs)
        response = HttpResponse(
            output,
            content_type=(
                "application/vnd.openxmlformats"
                "-officedocument.spreadsheetml.sheet"
            ),
        )
        response[
            "Content-Disposition"
        ] = f'attachment; filename="{file_name}.xlsx"'

        return response

    def get_file_name(self, **kwargs):
        return self.file_name

    def get_context_data(self, **kwargs):
        return {}

    def create_file(self, context, workbook, worksheet, **kwargs):
        pass


class BaseChoiceView(APIView):
    """
    Базовый класс представления API
    для получения списка choices
    """

    objects = None

    class ChoiceSerializer(Serializer):
        """Сериализатор для ModelChoice"""

        id = IntegerField(read_only=True)
        name = CharField(read_only=True, max_length=100)
        short_name = SerializerMethodField()

        def get_short_name(self, obj):
            return obj["name"][0]

    def choice_to_dict(self, items):
        """Метод преобразовывает ModelChoice в dict"""
        for el in items:
            yield {"id": el[0], "name": el[1]}

    def get(self, request):
        objetcs = list(self.choice_to_dict(self.objects))
        serializer = self.ChoiceSerializer(objetcs, many=True)
        return Response(serializer.data)
