from flask import Flask

app = Flask(__name__)

@app.route("/couriers", methods=['POST'])
def add_couriers():
    """Добавляет курьеров в БД"""
    return  {"message" : 'add_couriers'}


@app.route("/couriers/<int:courier_id>", methods=['GET', 'PATCH'])
def get_or_edit_courier(courier_id):
    """Показывает полную информацию курьера или обновляет его данные"""
    if request.method == 'GET':
        return {"message" : 'get_courier'}
    else:
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

