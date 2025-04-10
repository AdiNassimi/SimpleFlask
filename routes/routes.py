from flask import Blueprint
from controllers.ActivitiesController import get_activity, create_activity
from controllers.MonitorController import get_monitor

routes_bp = Blueprint('routes', __name__)

routes_bp.route('/activity', methods=['GET'])(get_activity)
routes_bp.route('/activity', methods=['POST'])(create_activity)
routes_bp.route('/monitor', methods=['GET'])(get_monitor)
