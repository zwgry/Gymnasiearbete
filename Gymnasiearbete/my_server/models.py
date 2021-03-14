from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from my_server import db, app

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    popularity = db.Column(db.Integer, nullable=False, default=0)
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

    def as_dict(self):
        return {p.name: getattr(self, p.name) for p in self.__table__.columns}

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
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False) 
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)

    def get_verification_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_verification_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Newsletter_Recipients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'Newsletter_Recipients({self.email})'

