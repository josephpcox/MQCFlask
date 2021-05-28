from flask import Flask
from app.authentication import auth
from flask_restplus import Resource, Api
from app.resources.models import Product, Security, Category, Vendor
from app.authentication.auth import AuthError,requires_auth

api = Api()

@api.route('/product/create/<string:vendor_code>/<string:product_name>/<string:product_cost>/<int:security_id>')
class CreateProduct(Resource):
    response = {
        201: "OK",
        400: "Bad Input. Required fileds are missing or are malformed",
        403: "Database error"
    }

    @api.doc(response)
    @requires_auth
    def post(self, vendor_code,product_name, product_cost, security_id):
        if all([vendor_code,product_name, product_cost, security_id]) is False:
            return {'msg': self.response[400]}, 400
        try:
            dict_product = {'vendor_code':vendor_code,
            'product_name': product_name, 
            'product_cost': float(product_cost), 
            'security_id':security_id}
            Product.create_porduct(dict_product=dict_product)
            # result = True
        except Exception as e:
            return {'msg': str(e)}, 403
        return 201

@api.route('/product/get_all')
class GetProduct(Resource):
    response = {
        201: "OK",
        403: "Database Error"
    }
    api.doc(response)
    @requires_auth
    def get(self):
        try:
            result = Product.get_products()
        except Exception as e:
            return {'msg': str(e)}, 403
        return result, 201

@api.route('/security/create/<string:category_code>/<int:security_level>')
class CreateSecurity(Resource):
    response = {
        201: "OK",
        400: "Bad Input. Required fileds are missing or are malformed",
        403: "Database error"
    }
    @requires_auth
    def post(self, category_code, security_level):
        if all([security_level,category_code]) is False:
            return {'msg':self.response[400]},400
        try:
            dict_security = {'category_code': category_code, 'security_level': security_level}
            Security.create_security(dict_security)
        except Exception as e:
            return {'msg':str(e)},403
        return 201


@api.route('/security/get_all')
class GetSecurities(Resource):
    response = {
        201: "OK",
        400: "Bad Input. Required fileds are missing or are malformed",
        403: "Database error"
    }
    @requires_auth
    def get(self):
        try:
            result = Security.get_securities()
        except Exception as e:
            return {'msg': str(e)}, 403
        return result, 201


@api.route('/category/create/<string:category_name>/<string:category_code>')
class CreateCategory(Resource):
    response = {
        200:"OK",
        400:"Bad Input",
        500:"Database Error"
    }
    api.doc(response)
    @requires_auth
    def post(self, category_name, category_code):
        if category_name is None:
            return {'msg':self.response[400]},400
        try:
            dict_category = {'category_name': category_name, 'category_code': category_code}
            Category.create_category(dict_category)
        except Exception as e:
            return {'msg':str(e)},500
        return 200

@api.route('/category/get_all')
class GetCategories(Resource):
    response = {
        201: "OK",
        403: "Database Error"
    }
    
    api.doc(response)
    @requires_auth
    def get(self):
        try:
            result = Category.get_categories()
        except Exception as e:
            return {'msg': str(e)}, 403
        return result, 201


@api.route('/vendor/create/<string:vendor_name>/<string:vendor_code>')
class CreateVendor(Resource):
    response = {
        200: "OK",
        400: "Bad Input",
        500: "Database Error"
    }
    api.doc(response)
    @requires_auth
    def post(self, vendor_name, vendor_code):
        if all([vendor_name, vendor_code]) is False:
            return {'msg': self.response[400]}, 400
        try:
            dict_vendor = {'vendor_name': vendor_name,
                             'vendor_code': vendor_code
            }
            Vendor.create_vendor(dict_vendor)
        except Exception as e:
            return {'msg': str(e)}, 500
        return 200


@api.route('/vendor/get_all')
class GetVendors(Resource):
    response = {
        201: "OK",
        403: "Database Error"
    }
    api.doc(response)
    @requires_auth
    def get(self):
        try:
            result = Vendor.get_vendors()
        except Exception as e:
            return {'msg': str(e)}, 403
        return result, 201
