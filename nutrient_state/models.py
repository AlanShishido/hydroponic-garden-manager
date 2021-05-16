from django.db import models
from django.utils import timezone

from nutrient_state.modelmanager import LettuceNutrientsManager, HistoryNutrientsDataManager


class DBNutrientsBase(models.Model):
    id = models.AutoField(
        db_column='id',
        null=False,
        primary_key=True
    )
    active = models.BooleanField(
        db_column='active',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        db_column="dt_create",
        null=False,
        auto_now_add=True
    )
    modifield_at = models.DateTimeField(
        db_column="dt_modify",
        null=False,
        auto_now=True
    )

    @property
    def created_at_with_tz(self):
        return timezone.localtime(self.created_at)

    @property
    def modifield_at_with_tz(self):
        return timezone.localtime(self.modifield_at)

    class Meta:
        abstract = True


class LettuceNutrients(DBNutrientsBase):
    status_code = models.CharField(
        db_column='status_code',
        null=False,
        default='0',
        max_length=4
    )
    ph_value = models.FloatField(
        db_column='ph_value',
        null=False,
        default='-1'
    )
    tds_value = models.FloatField(
        db_column='tds_value',
        null=False,
        default='-1',
    )
    tank_level = models.FloatField(
        db_column='tank_level',
        null=False,
        default='-1',
    )

    objects = LettuceNutrientsManager()

    class Meta:
        db_table = 'nutrientes_alface'
        verbose_name = 'Nutriente da Alface'
        verbose_name_plural = 'Nutrientes das Alfaces'
        managed = True


class HistoryNutrientsData(DBNutrientsBase):
    greens = models.CharField(
        db_column="greens",
        max_length=32
    )
    objects = HistoryNutrientsDataManager()
        
    class Meta:
        db_table = 'historico_nutrientes'
        verbose_name = 'Historico de Nutriente'
        verbose_name_plural = 'Historico de Nutrientes'
        managed = True
