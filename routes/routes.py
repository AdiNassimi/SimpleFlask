from flask import Blueprint, jsonify, request


# Create a Blueprint instance
routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get('name')
    data = request.get_json()  # Get body param
    return jsonify({"message": f"Hello {name} from Blueprint!"}), 200