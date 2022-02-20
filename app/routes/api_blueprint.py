from flask import Blueprint
from app.routes.vaccine_blueprint import bp_vaccine

bp_api = Blueprint("bp_api", __name__, url_prefix="/")

bp_api.register_blueprint(bp_vaccine)