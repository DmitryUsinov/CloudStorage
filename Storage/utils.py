from .models import *

menud = [{'title': "Главная", 'url_name': 'about'},
        {'title': "Дисциплины", 'url_name': 'discipline'},
        {'title': "Добавить дисциплину", 'url_name': 'add_discipline'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Discipline.objects.all()
        user_menu = menud.copy()
        if self.request.user.is_authenticated:
            if not self.request.user.groups.all()[0].name == 'Преподаватель':
                user_menu.pop(2)
        else:
            user_menu.pop(2)

        context['menu'] = user_menu

        return context