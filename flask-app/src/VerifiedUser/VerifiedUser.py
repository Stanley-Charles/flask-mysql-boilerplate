from flask import Blueprint, request, jsonify, make_response
import json, re
from src import db


VerifiedUser = Blueprint('VerifiedUser', __name__)

# Get all the verified users
@VerifiedUser.route('/VerifiedUsers', methods=['GET'])
def get_all_verified_users():
    cursor = db.get_db().cursor()
    query = '''
        SELECT FirstName
        FROM VerifiedUser
        LIMIT 5
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get all the Posts
@VerifiedUser.route('/Post', methods=['GET'])
def get_all_posts():
    cursor = db.get_db().cursor()
    query = '''
        SELECT *
        FROM Post
        LIMIT 5
    '''
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)
    

# Get All Posts details for Verified User with particular userID
@VerifiedUser.route('/Post/<userID>', methods=['GET'])
def get_post(userID):
    cursor = db.get_db().cursor()
    cursor.execute("select * from Post where UserID = '{0}' order by LikeCount".format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get Win Percentage for Verified User with particular userID
@VerifiedUser.route('/Win/<userID>', methods=['GET'])
def get_WinP(userID):
    cursor = db.get_db().cursor()
    cursor.execute("select WinPercntage from VerifiedUser where UserID = '{0}'".format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#Get Team Props after a specific date
@VerifiedUser.route('/TeamProp/<date>', methods=['GET'])
def get_Team_Prop_date(date):
    cursor = db.get_db().cursor()
    query = '''
    SELECT TeamProps, PropName, GameTime, T.TeamID
    FROM TeamProps JOIN Team T on T.TeamID = TeamProps.TeamID JOIN PlaysIn Y on T.TeamID = Y.PlaysInName
    JOIN Game G on Y.GameID = G.GameId
    WHERE GameTime >= '{0}'
    '''
    cursor.execute(query.format(date))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#Get Player Props after a specific date
@VerifiedUser.route('/PlayerProp/<date>', methods=['GET'])
def get_Player_Prop_date(date):
    cursor = db.get_db().cursor()
    query = '''
    SELECT PlayerProps, PropName, GameTime, PlayerName
    FROM PlayerProps JOIN Team T on T.TeamID = PlayerProps.TeamID JOIN PlaysIn Y on T.TeamID = Y.PlaysInName
    JOIN Game G on Y.GameID = G.GameId
    WHERE GameTime >= '{0}'
    '''
    cursor.execute(query.format(date))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#Change the content of a specific Post
@VerifiedUser.route('/change', methods=['PUT'])
def update_post_content():
    the_data = request.json
    PostId = the_data['PostId']
    Content = the_data['Content']

    the_query = 'UPDATE Post SET Content = %s WHERE PostID = %s;'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (Content, PostId))
    db.get_db().commit()
    return jsonify ({"message": "Content changed successfully"}),200

# Get the count of Posts for a Specific User
@VerifiedUser.route('/PostCount/<userID>', methods=['GET'])
def get_post_count(userID):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT count(*) FROM Post WHERE UserID = '{0}'".format(userID))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

#Add another Post (post request)
@VerifiedUser.route('/AddPost', methods=['POST'])
def add_new_post():
    the_data = request.json
    UserID = the_data['UserID']
    PostID = the_data['PostID']
    Content = the_data['Content']
    #LikeCount = the_data['LikeCount']
    #DislikeCount = the_data['DislikeCount']
    GameID = the_data['GameID']

    the_query = 'INSERT INTO Post(UserID,PostID,Content,LikeCount,DislikeCount,GameID) VALUES (%s , %s, %s, 0, 0 , %s);'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (UserID, PostID, Content, GameID))
    db.get_db().commit()
    return jsonify({"message": "Added User successfully"}), 200

#Delete your Verified User Account (Delete request)
@VerifiedUser.route('/delete/user', methods=['DELETE'])
def delete_user():
    the_data = request.json
    UserID = the_data['UserID']
    the_query = 'DELETE FROM VerifiedUser WHERE UserID = %s'
    #current_app.logger.info(the_query)
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (UserID))
    db.get_db().commit()
    return jsonify({"message": "Deleted User successfully"}), 200



#Make a login page for the Verified User
@VerifiedUser.route('/login', methods=['GET'])
def vu_login():
    the_data = request.json
    UserId = the_data['UserId']
    UserPassword = the_data['UserPassword']
    the_query = 'SELECT * FROM VerifiedUser WHERE UserId = %s AND UserPassword = %s'
    cursor = db.get_db().cursor()
    cursor.execute(the_query, (UserId, UserPassword))
    result = cursor.fetchone()
    if result:
        return "Success"
    else:
        raise Exception("Incorrect credentials")