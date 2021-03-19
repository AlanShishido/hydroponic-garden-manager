from nutrient_state.models import LettuceNutrients


def save_ph_value(ph_value: float):
    maintenance_item = LettuceNutrients(
        status_code='1000',
        ph_value=ph_value
    )
    maintenance_item.save()
