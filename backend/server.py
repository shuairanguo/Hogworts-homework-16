from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config["testcase"]=[]

@app.route('/')
def hello():
    return "Hello world!"

#
# @app.route('/app', methods=['get', 'post'])
# def hello2():
#     return "Hello app!"


@app.route('/abc/<int:tmp>', methods=['get', 'post'])
def hello3(tmp):
    print(request.data)
    print(request.json)
    print(tmp)
    return 'hello'


class HelloWorld(Resource):
    def get(self):
        # print(app.config["testcase"].append(request.json))
        if 'id' in request.args:
            for i in app.config["testcase"]:
                print(i)
                # 返回用例
                if i['id'] == int(request.args["id"]):
                    print(i)
                    return i
        else:
            return app.config["testcase"]


    def post(self):
        """
        每条testcase要有id
        :return:
        """
        if "id" not in request.json:
            return {"result":"error","errorcode":400,"msg":"need id"}
        print(request.json)
        app.config["testcase"].append(request.json)
        return 'this is a post'


api.add_resource(HelloWorld, '/testcase')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
