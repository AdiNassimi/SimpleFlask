from flask import request, jsonify


def get_monitor():
    """
    Get all monitors of a specific server.
    """
    server_id = request.args.get('server_id', None)
    # Here you would typically fetch the monitors from a database
    # For now, we'll just return a mock response
    return jsonify({
        "message": "Monitors fetched successfully!",
        "data": {
            "server_id": server_id,
            "monitors": [
                {"id": 1, "name": "CPU Usage", "value": "75%"},
                {"id": 2, "name": "Memory Usage", "value": "60%"}
            ]
        }
    }), 200
