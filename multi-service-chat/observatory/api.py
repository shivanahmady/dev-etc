from flask import Flask
from flask_restful import Resource, Api
# Instantiate 
app = Flask(__name__)
api = Api(app)

class Hub(Resource):
    def get(self):
        return {
            'dataset_1': ['entity_1', 'entity_2', 'entity_2']
        }

#route
api.add_resource(Hub, '/')

#start it up!
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
