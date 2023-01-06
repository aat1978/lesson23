from flask import Blueprint, request, jsonify

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    validated_data = BatchRequestSchema().load(data)
    result = None
    for query in validated_data:
        result = build_query(
            cmd=validated_data['cmd'],
            value=validated_data['value'],
            file_name='data/apache_logs.txt',
            data=result
        )
    return jsonify(result)
