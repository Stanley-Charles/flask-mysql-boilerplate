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

@SystemAdmin.route('/allposts', methods=['GET'])
def get_sitewide_posts():
    cursor = db.get_db().cursor()
    query = '''
        SELECT PostID, Content
        FROM Post
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@SystemAdmin.route('/allusers', methods=['GET'])
def get_all_users():
    cursor = db.get_db().cursor()
    query = '''
        SELECT FirstName, LastName, UserId
        FROM VerifiedUser
        WHERE UserId
        UNION
        SELECT FirstName, LastName, UserId
        FROM NormalUser
        WHERE UserId
        UNION
        SELECT FirstName, LastName, AdminId
        FROM SystemAdmin
        WHERE AdminId
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)


@SystemAdmin.route('/get_comments/<PostID>', methods=['GET'])
def get_comments(PostID):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT c.UserID, c.CommentText FROM Comment c JOIN Reaction r ON c.UserID = r.UserID AND c.ReactionID = r.ReactionID WHERE r.PostID = {0}'.format(PostID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#update password for system admin
@SystemAdmin.route('/change/<AdminID>', methods=['PUT'])
def update_admin_password(AdminID):
    the_data = request.json
    AdminPassword = the_data['AdminPassword']

    the_query = 'UPDATE SystemAdmin SET AdminPassword = %s WHERE AdminID = %s;'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (AdminPassword, AdminID))
    db.get_db().commit()
    return jsonify ({"message": "Password uploaded successfully"}), 200

#update address for system admin
@SystemAdmin.route('/address/<AdminID>', methods=['PUT'])
def update_admin_address(AdminID):
    the_data = request.json
    HouseNumber = the_data['HouseNumber']
    Street = the_data['Street']
    City = the_data['City']

    the_query = 'UPDATE SystemAdmin SET HouseNumber = %s, Street = %s, City = %s WHERE AdminID = %s;'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (HouseNumber, Street, City, AdminID))
    db.get_db().commit()
    return jsonify({"message": "Address updated successfully"}), 200

#Add another admin(post request)
@SystemAdmin.route('/post', methods=['POST'])
def add_new_admin():
    the_data = request.json
    AdminID = the_data['AdminID']
    FirstName = the_data['FirstName']
    LastName = the_data['LastName']
    Email = the_data['Email']
    AdminPassword = the_data['AdminPassword']
    HouseNumber = the_data['HouseNumber']
    Street = the_data['Street']
    City = the_data['City']
    Salary = the_data['Salary']

    the_query = 'INSERT INTO SystemAdmin(AdminId,FirstName,LastName,Email,AdminPassword,HouseNumber,Street,City,Salary) VALUES (%s , %s, %s, %s, %s, %s, %s, %s, %s);'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (AdminID, FirstName, LastName, Email, AdminPassword, HouseNumber, Street, City, Salary))
    db.get_db().commit()
    return jsonify({"message": "Added User successfully"}), 200

#Delete an Admin from the table (Delete request)
@SystemAdmin.route('/delete', methods=['DELETE'])
def delete_admin():
    the_data = request.json
    AdminID = the_data['AdminID']
    the_query = 'DELETE FROM SystemAdmin WHERE AdminId = %s'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (AdminID))
    db.get_db().commit()
    return jsonify({"message": "Deleted User successfully"}), 200


#Delete a post from the table (Delete request)
@SystemAdmin.route('/delete/comment', methods=['DELETE'])
def delete_comment():
    the_data = request.json
    PostID = the_data['PostID']
    ReactionID = the_data['ReactionID']
    the_query = 'DELETE FROM Comment WHERE (UserID, ReactionID) IN (SELECT r.UserID, r.ReactionID FROM Reaction r WHERE r.PostID = %s AND r.ReactionID = %s);'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (PostID, ReactionID))
    db.get_db().commit()
    return jsonify({"message": "Deleted comment successfully"}), 200