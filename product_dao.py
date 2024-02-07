from sql_connection_dao import get_all_connection

def get_all_products():

    cursor = connection.cursor()

    query = ("SELECT product_table.product_id,product_table.product_name,product_table.unit_id,"
             "product_table.price_per_unit,unit_table.unit_name FROM product_table INNER JOIN unit_table ON product_table.unit_id=unit_table.unit_id")

    cursor.execute(query)

    response = []

    for (product_id,product_name,unit_id,price_per_unit,unit_name) in cursor:
      response.append(
         {
           "product_id" : product_id,
           "product_name": product_name,
           "unit_id": unit_id,
           "price_per_unit": price_per_unit,
           "unit_name": unit_name
         }
      )


    return response
def insert_product(connection,product):

    cursor =connection.cursor()

    query = ("insert into product_table"
             "(product_name,unit_id,price_per_unit)"
             "value(%s,%s,%s)")

    data = (product['product_name'],product['unit_id'],product['price_per_unit'])

    cursor.execute(query, data)

    connection.commit()

    return cursor.lastrowid

def delete_product(connection,product_id):
    cursor= connection.cursor()
    query = ("delete from product_table where product_id= "+ str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ =='__main__':
    connection = get_all_connection()
    print(delete_product(connection,12))

   # print (insert_product (connection,{
           # 'product_name': 'chips',
           # 'unit_id' : '1',
           # 'price_per_unit' : '30'
   # }
   # ))##














