from chalice import Chalice
from chalicelib.VuePy import VuePy
import json

app = Chalice(app_name='backend')

@app.route('/state/{storage_id}')
def state(storage_id):
    try:
        stored = next(VuePy.query(storage_id))
    except:
        return {}

    return json.loads(stored.countries)

@app.route('/save', methods=['POST'])
def save():
    data = app.current_request.json_body

    vuepy = VuePy(data['id'], countries=json.dumps(data['countries']))
    vuepy.save()

    return {'success': 'true'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
