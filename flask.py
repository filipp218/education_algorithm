from flask import Flask,request, abort
from jsonschema import validate, exceptions

app = Flask(__name__)

@app.errorhandler(400)
def answer_400(error):
    return 'bad request!', 400

courier_shema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "courier_id": {"type": "integer"},
            "courier_type":{
                "type": "string",
                "enum":["foot", "bike" , "car"]},
            "regions": {
                "type": "array",
                "items": {"type": "integer"}},
            "working_hours":{
                "type": "array",
                "items": {"type": "string"}}
            },
        "required": ["courier_id", "courier_type", "regions", "working_hours"],
}

@app.route("/couriers", methods=['POST'])
def add_couriers():
    """Добавляет курьеров в БД"""
    answer_error = {"validation_error":{
                "couriers": []
                }}
    id_error = answer_error["validation_error"]
    valid_couriers = {"couriers":[]}

    json_couriers = request.get_json()
    for raw in json_couriers['data']:
        try:
            validate(instance=raw, schema=courier_shema)
            valid_couriers["couriers"].append(raw["courier_id"])
        except exceptions.ValidationError:
            id_error.append(raw["courier_id"])

    if len(id_error["couriers"])>0:
        abort(400)

    return  {"message" : 'add_couriers'}


@app.route("/couriers/<int:courier_id>", methods=['GET'])
def get_courier(courier_id):
    """Показывает полную информацию курьера"""
    return {"message" : 'get_courier'}


@app.route("/couriers/<int:courier_id>", methods=['PATCH'])
def edit_courier(courier_id):
    """Обновляет данные курьера"""
    return {"message" : 'edit_courier'}

@app.route("/orders", methods=['POST'])
def add_orders():
    """Добавляет новые заказы в БД"""
    return {"message" : 'add_orders'}


@app.route("/orders/assign", methods=['POST'])
def assign_orders():
    """Распределяет заказы по курьерам"""
    return {"message" : 'assign_orders'}


@app.route("/orders/complete", methods=['POST'])
def orders_complete():
    """Добавляет выполненные заказы"""
    return {"message" : 'orders_complete'}


if __name__ == '__main__':
    app.run()
