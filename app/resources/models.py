from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
# from sqlalchemy.orm import relationship, backref
import json

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(50), nullable=False, unique=True)
    product_cost = db.Column(db.Numeric(12, 2), nullable=False)
    security_id = db.Column(db.Integer, db.ForeignKey('security.security_id'))
    vendor_code = db.Column(db.String(15),db.ForeignKey('vendor.vendor_code'))
    vendor = db.relationship('Vendor')
    security = db.relationship('Security')

    def __init__(self, product_name, product_cost, vendor_code,security_id):
        self.vendor_code = vendor_code
        self.product_name = product_name
        self.product_cost = product_cost
        self.security_id = security_id

    def get_dict(self):
        return {'Vendor Code':self.vendor_code,
        'Product ID': self.product_id,
        'Product Name':self.product_name,
        'Product Cost':str(self.product_cost),
        'Security ID':self.security_id}

    def save_product(self):
        db.session.add(self)
        db.session.commit()

    def delete_product(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def create_porduct(cls, dict_product):
        new_product = Product(**dict_product)
        new_product.save_product()
        # return new_product.get_dict()

    @classmethod
    def get_products(cls):
        result = []
        for r in cls.query.all():
            result.append(r.get_dict()) 
        return result 


class Security(db.Model):
    __tablename__= 'security'
    security_id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    security_level = db.Column(db.Integer, nullable=False)
    category_code = db.Column(db.String(15),db.ForeignKey('category.category_code'))
    # category_id = db.Column(db.Integer)
    category = db.relationship('Category')
    
    def __init__(self, category_code, security_level):
        self.security_level = security_level
        self.category_code = category_code
    
    def save_security(self):
        db.session.add(self)
        db.session.commit()

    def delete_security(self):
        db.session.delete(self)
        db.session.commit()

    def get_dict(self):
        return {'Security ID': self.security_id, 
        'Category Code': self.category_code, 
        'Security Level': str(self.security_level)
        }
    
    @classmethod
    def create_security(cls, dict_security):
        new_security = Security(**dict_security)
        new_security.save_security()

    @classmethod
    def get_securities(cls):
        result = []
        for r in cls.query.all():
            result.append(r.get_dict())
        return result


class Category(db.Model):
    __tablename__='category'
    category_code = db.Column(db.String(15),primary_key=True)
    category_name = db.Column(db.String(50),nullable=False, unique=True)
    # end point ect 

    def __init__(self, category_name, category_code):
        self.category_name = category_name
        self.category_code = category_code

    def save_category(self):
        db.session.add(self)
        db.session.commit()

    def delete_category(self):
        db.session.delete(self)
        db.session.commit()

    def get_dict(self):
        return {'Category Code': self.category_code ,'Category Name': self.category_name}

    @classmethod
    def create_category(cls, dict_category):
        new_category = Category(**dict_category)
        new_category.save_category()

    @classmethod
    def get_categories(cls):
        result = []
        for r in cls.query.all():
            result.append(r.get_dict()) 
        return result 

class Vendor(db.Model):
    __tablename__='vendor'
    vendor_code = db.Column(db.String(15), primary_key=True)
    vendor_name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, vendor_name, vendor_code):
        self.vendor_name = vendor_name
        self.vendor_code = vendor_code

    def save_vendor(self):
        db.session.add(self)
        db.session.commit()

    def delete_vendor(self):
        db.session.delete(self)
        db.session.commit()

    def get_dict(self):
        return {'Vendor Name': self.vendor_name, 'Vendor Code':self.vendor_code}
    
    @classmethod
    def create_vendor(cls, dict_vendor):
        new_vendor = Vendor(**dict_vendor)
        new_vendor.save_vendor()
    
    @classmethod
    def get_vendors(cls):
        result = []
        for r in cls.query.all():
            result.append(r.get_dict()) 
        return result 

                           
