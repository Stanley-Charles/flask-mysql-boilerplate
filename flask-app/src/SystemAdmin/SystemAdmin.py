from flask import Blueprint, request, jsonify, make_response
import json
from src import db


SystemAdmin = Blueprint('SystemAdmin', __name__)

# Get all the admins
@SystemAdmin.route('/SystemAdmin', methods=['GET'])
def get_systemadmin_posts():
    cursor = db.get_db().cursor()
    query = '''
        SELECT FirstName
        FROM SystemAdmin
        LIMIT 5
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)
