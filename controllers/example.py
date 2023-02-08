from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class ProductController(Resource):
    def get(self, product_id):
        # Return a specific product based on its id
        product = get_product(product_id)
        return jsonify(product)

    def put(self, product_id):
        # Update a specific product based on its id
        data = request.get_json()
        update_product(product_id, data)
        return jsonify({'message': 'Product updated successfully'})


api.add_resource(ProductController, '/products/<int:product_id>')

if __name__ == '__main__':
    app.run(debug=True)