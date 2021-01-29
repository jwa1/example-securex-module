from functools import partial

from flask import Blueprint
from webexteamssdk import WebexTeamsAPI

from api.schemas import ActionFormParamsSchema, ObservableSchema
from api.utils import get_json, get_jwt, jsonify_data

respond_api = Blueprint('respond', __name__)

get_observables = partial(get_json, schema=ObservableSchema(many=True))
get_action_form_params = partial(get_json, schema=ActionFormParamsSchema())

@respond_api.route('/respond/observables', methods=['POST'])
def respond_observables():
    # _ = get_jwt()
    _ = get_observables()
    return jsonify_data([
        {
            "id": "helpme",
            "title": "Ask for Help",
            "description": "Ask for help with this observable",
            "categories": ["help", "stuff"],
            "query-params": {
                "observable_value": _[0]["value"],
                "observable_type": _[0]["type"],
                "action_id": "help"
            }
        }]
    )


@respond_api.route('/respond/trigger', methods=['POST'])
def respond_trigger():
    # _ = get_jwt()
    _ = get_action_form_params()
    # _['observable_type'], _['observable_value']
    
    return jsonify_data({'status': 'success'})
