from flask import Flask, render_template, jsonify
from flask import request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gsr066567@localhost:3306/testcase?charset=utf8mb4'
db = SQLAlchemy(app)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


class TestCase(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    description = db.Column(db.String(80), unique=False, nullable=True)
    steps = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.description


class HelloWorld(Resource):
    def get(self, tmp):
        print(tmp)
        # db.create_all()
        # db.session.add(TestCase(name="tmp"))
        # db.session.commit()
        testcase = TestCase.query.filter_by(id=tmp)

        # testcase = db.session.query_property(query_cls=TestCase)

        print(testcase)
        print(type(testcase))
        # return "ok"
        return testcase

    def post(self, tmp):
        print(request.data)
        print(request.json)
        print(tmp)
        return "hello, world!"


api.add_resource(HelloWorld, '/<int:tmp>')
# api.add_resource(HelloWorld, '/abc/<int:tmp>')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
