from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


def test_sqlalchemy():
    app = Flask(__name__)
    api = Api(app)
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gsr066567@localhost:3306/testcase?charset=utf8mb4'
    db = SQLAlchemy(app)

    class TestCase(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), unique=False, nullable=True)
        description = db.Column(db.String(80), unique=False, nullable=True)
        steps = db.Column(db.String(120), unique=False, nullable=True)

        def __repr__(self):
            return '<User %r>' % self.description

    db.session.add(TestCase(name="测试", description="descriptiondescription", steps="stepssteps"))
    db.session.commit()
