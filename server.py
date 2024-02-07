from flask import Flask,request,jsonify
import product_dao
from sql_connection_dao import get_all_connection
import unit_dao


app = Flask(__name__)

connection = get_all_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = unit_dao.get_all_unit(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getProducts', methods=['GET'])
def get_products():
    response = product_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print("starting python flask server for grocery store management system ")
    app.run(port=5000)

