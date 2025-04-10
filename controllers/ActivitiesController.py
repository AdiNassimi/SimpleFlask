from flask import request, jsonify


def get_activity():
    """
    Get all activities of a specific server.
    """
    server_id = request.args.get('server_id', None)

    # Here you would typically fetch the activities from a database
    # For now, we'll just return a mock response
    return jsonify({
        "message": "Activities fetched successfully!",
        "data": {
            "server_id": server_id,
            "activities": [
                {"id": 1, "type": "login", "timestamp": "2023-10-01T12:00:00Z"},
                {"id": 2, "type": "logout", "timestamp": "2023-10-01T12:30:00Z"}
            ]
        }
    }), 200


def create_activity():
    """
    Create a new activity for a specific server.
    """
    data = request.get_json()
    server_id = data.get('server_id')
    activity_type = data.get('activity_type')
    description = data.get('description')

    # Here you would typically save the activity to a database
    # For now, we'll just return the received data as a response
    return jsonify({
        "message": "Activity created successfully!",
        "data": {
            "server_id": server_id,
            "activity_type": activity_type,
            "description": description
        }
    }), 201
