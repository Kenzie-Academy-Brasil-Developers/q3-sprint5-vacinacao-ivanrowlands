from app.models.vaccine_model import Vaccine
from sqlalchemy.exc import IntegrityError
from app.configs.database import db
from flask import request, jsonify

request_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]

def create_vaccine_card():
	data = request.get_json()
	data_keys = data.keys()
	right_keys = []

	for key in request_keys:
		if key in data_keys:
			right_keys.append(key)
		else:
			return {"error": f"missing key '{key}'"}
	

	if len(right_keys) == 4:
		delete_keys = list(data_keys - request_keys)
		
		for key in delete_keys:
			del data[key]
		

	for values in data.values():
		if type(values) is not  str:
			return {"error": "request must be in string"}, 400
		
	try:
		if len(data["cpf"]) == 11:
			data["name"] = data["name"].title()
			data["health_unit_name"] = data["health_unit_name"].title()
			vaccine_card = Vaccine(**data)
			db.session.add(vaccine_card)
			db.session.commit()

			return jsonify(vaccine_card), 201
		else :
			return {"error": "cpf must contain 11 characters"}, 400

	except IntegrityError as e:
		return jsonify({"error": "cpf already registered"}), 409
	
	except (KeyError, TypeError):
		wrong_keys = list(data_keys - request_keys)
		return jsonify({"error": {"expected_keys": request_keys,"incoming_keys": wrong_keys}}), 400

def get_vaccine_card():
	vaccines = (
		Vaccine
		.query
		.all()
	)
	return jsonify({"vaccines_card": vaccines}), 200