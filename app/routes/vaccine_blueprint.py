from flask import Blueprint

from app.controllers.vaccine_controller import create_vaccine_card, get_vaccine_card

bp_vaccine = Blueprint("bp_vaccine", __name__, url_prefix="/vaccinations")
bp_vaccine.post("")(create_vaccine_card)
bp_vaccine.get("")(get_vaccine_card)