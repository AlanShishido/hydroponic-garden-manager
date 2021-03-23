from django.db import models
from django.db.models import Case, When, F


class ManageModelBase(models.Model):
    def queryset(self):
        return super(ManageModelBase, self)


class HistoryNutrientsDataManager(ManageModelBase):
    def get_all(self, **params):
        params['active'] = params.get('active', True)

        return self.queryset().filter(**params).order_by('created_at')


class LettuceNutrientsManager(ManageModelBase):
    def get_model_attibutes(self, **filters):
        return self.queryset().filter(**filters).all()
