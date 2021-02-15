from my_server import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pictures = db.relationship('Picture', backref='product', lazy=True)

    def __repr__(self):
        return f"Product('{self.name}','{self.id}')"

    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    filepath = db.Column(db.String(20), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Picture('{self.id}','{self.product_id}')"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    super_category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False, default=0)

    def __repr__(self):
        return f"Category('{self.id}','{self.name}')"

    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.user_id}')"

class List_Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.list_id}')"
