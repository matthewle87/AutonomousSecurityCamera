from flask import Flask
from flask_restful import Api, reqparse, abort, fields
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    year = db.Column(db.Integer, nullable = False)
    month = db.Column(db.Integer, nullable = False)
    day = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String(100), nullable = False, primary_key = True)

    def __repr__(self):
        return f"Video(Year = {year}, month = {month}, day = {day}, name = {name})"

resource_fields = {
    'year': fields.Integer,
    'month': fields.Integer,
    'day': fields.Integer,
    'name': fields.String
}

#creates database if one is not present
if not os.path.exists("database.db"):
    db.create_all()

#makes sure that the request has all the information necessary
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("year", type = str, help = "Name of the video is required.", required = True)
video_put_args.add_argument("month", type = str, help = "Name of the video is required.", required = True)
video_put_args.add_argument("day", type = str, help = "Name of the video is required.", required = True)
video_put_args.add_argument("name", help = "Request sent without the video.", required = True)

@app.route('/profile')
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body

#When the website initially opens, grabs all the videos in the database
@app.route('/getall')
def getall():
    result = [vid.name for vid in VideoModel.query.all()]
    if not result:
        abort(404, "No videos are in the database")
    return {"videos": [vid.name for vid in VideoModel.query.all()]}

#Gets all videos of a specific year
@app.route('/getyear/<int:yearNum>')
def getyear(yearNum):
    result = [vid.name for vid in VideoModel.query.filter_by(year = yearNum).all()]
    if not result:
        abort(405, message = "Could not find video with that date.")
    return {"videos": [result]}

#Puts a new video into the database
@app.route('/put', methods = ['PUT'])
def put():
    args = video_put_args.parse_args()
    result = VideoModel.query.filter_by(name = args['name']).first()
    if result:
        abort(409, message = 'Video name is already taken...')
    video = VideoModel(year = args['year'], month = args['month'], day = args['day'], name = args['name'])
    db.session.add(video)
    db.session.commit()
    return "Successful"

if __name__ == "__main__":
    app.run(debug = True)
    print()