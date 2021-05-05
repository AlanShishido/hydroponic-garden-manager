from nutrient_state import models


def save_all_data(payload: tuple):
    ph, tds = payload
    maintenance_item = models.LettuceNutrients(
        ph_value=ph,
        tds_value=tds
    )
    maintenance_item.save()

def save_ph_value(ph_value: float):
    maintenance_item = models.LettuceNutrients(
        status_code='1000',
        ph_value=ph_value
    )
    maintenance_item.save()

def save_tds_value(tds_value: float):
    maintenance_item = models.LettuceNutrients(
        status_code='1001',
        tds_value=tds_value
    )
    maintenance_item.save()


def modify_value(ph_value: float):
    maintenance_item = models.LettuceNutrients.objects.get(status_code='1000')

    if maintenance_item:
        maintenance_item.status_code = '1001'
        maintenance_item.ph_value = ph_value
        maintenance_item.save()
