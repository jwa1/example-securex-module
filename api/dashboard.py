from flask import Blueprint, json

from api.schemas import DashboardTileDataSchema, DashboardTileSchema
from api.utils import get_json, get_jwt, jsonify_data

dashboard_api = Blueprint("dashboard", __name__)


@dashboard_api.route("/tiles", methods=["POST"])
def tiles():
    # _ = get_jwt()
    return jsonify_data(
        [
            {
                "id": "test-summary",
                "type": "metric_group",
                "title": "Test Tile",
                "periods": ["last_24_hours"],
                "short_description": "A short description",
                "description": "A longer description",
                "tags": ["test"],
            },
            {
                "id": "test-graph",
                "type": "line_chart",
                "title": "Test Graph",
                "periods": ["last_24_hours"],
                "short_description": "A short description",
                "description": "A longer description",
                "tags": ["test"],
            },
        ]
    )


@dashboard_api.route("/tiles/tile", methods=["POST"])
def tile():
    # _ = get_jwt()
    _ = get_json(DashboardTileSchema())
    return jsonify_data({})


@dashboard_api.route("/tiles/tile-data", methods=["POST"])
def tile_data():
    # _ = get_jwt()
    _ = get_json(DashboardTileDataSchema())
    if _["tile_id"] == "test-summary":
        return jsonify_data(
            {
                "observed_time": {
                    "start_time": "2020-12-19T00:07:00.000Z",
                    "end_time": "2021-01-18T00:07:00.000Z",
                },
                "valid_time": {
                    "start_time": "2021-01-18T00:07:00.000Z",
                    "end_time": "2021-01-18T00:12:00.000Z",
                },
                "data": [
                    {
                        "icon": "brain",
                        "label": "IQ Required to Hack",
                        "value": 197,
                        "value-unit": "integer",
                    },
                    {
                        "icon": "percent",
                        "label": "% of password required",
                        "value": 15,
                        "value-unit": "integer",
                    },
                ],
                "cache_scope": "org",
            }
        )
    else:
        return jsonify_data(
            {
                "observed_time": {
                    "start_time": "2020-12-28T04:33:00.000Z",
                    "end_time": "2021-01-27T04:33:00.000Z",
                },
                "valid_time": {
                    "start_time": "2021-01-27T04:33:00.000Z",
                    "end_time": "2021-01-27T04:38:00.000Z",
                },
                "key_type": "timestamp",
                "data": [
                    {"key": 1611731572, "value": 13},
                    {"key": 1611645172, "value": 20},
                    {"key": 1611558772, "value": 5},
                    {"key": 1611431572, "value": 13},
                    {"key": 1611345172, "value": 20},
                    {"key": 1611258772, "value": 5},
                    {"key": 1611131572, "value": 13},
                    {"key": 1611045172, "value": 20},
                    {"key": 1610958772, "value": 5},
                    {"key": 1610831572, "value": 13},
                    {"key": 1610745172, "value": 20},
                    {"key": 1610658772, "value": 5},
                    {"key": 1610531572, "value": 13},
                    {"key": 1610445172, "value": 20},
                    {"key": 1610358772, "value": 5},
                ],
                "cache_scope": "org",
            }
        )
