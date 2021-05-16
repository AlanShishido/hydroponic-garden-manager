from nutrient_state import models


def save_nutrients_value(payload: tuple):
    ph, tds, tank = payload
    maintenance_itens = models.LettuceNutrients(
        status_code='1000',
        ph_value=ph,
        tds_value=tds,
        tank_level=tank
    )
    maintenance_itens.save()


def save_ph_value(ph_value: float):
    maintenance_item = models.LettuceNutrients(
        status_code='1',
        ph_value=ph_value
    )
    maintenance_item.save()


def save_tds_value(tds_value: float):
    maintenance_item = models.LettuceNutrients(
        status_code='2',
        tds_value=tds_value
    )
    maintenance_item.save()
