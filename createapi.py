from flask import Flask, request, jsonify, render_template, flash, session, redirect
from flask_restful import Api, Resource,reqparse
from datetime import date, time
from datetime import datetime
import uuid

app=Flask(__name__)
api = Api(app)

class Trips():
	def getOpenings(self):
		"""Get time openings for current week"""
		id=uuid.uuid4()
		deadlines = []
		t = datetime.datetime.now()
		weekday=datetime.datetime.today().weekday()
		if t.hour < 15:
		    deadline = datetime.datetime(year=t.year, month=t.month, day=t.day, hour=15, minute=0, second=0)
		    deadlines.append(deadline)
		elif t.hour<21:
		    deadline=datetime.datetime(year=t.year, month=t.month, day=t.day, hour=21, minute=0, second=0)
		    deadlinse.append(deadline)
		else:
		    today + datetime.timedelta(days=1)


		DateTimeRange =[{
		    'start': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=15, minute=30, second=0),
		    'end': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=20, minute=0, second=0)
		    },
		    {'start': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=6, minute=0, second=0),
		    'end': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=11, minute=0, second=0)
		    }]
		   
		for day in range(0,7) >= weekday:
		    for timeRange in DateTimeRange:
		        for deadline in deadlines:
		            timeOpening={
		                'id': id,
		                'requestDeadline' : nextdeadline,
		                'timeSelectionRange': DateTimeRange,
		                timeSelectionIntervalMinutes: 5
		                }
		TimeOpening.append(timeOpening)
		return (TimeOpening, 200)
			

	def postRequest(self,tripRequest):
		"""creates trip request """
		tripRequest ={
			"timeOpening": TimeOpening,
			"mode": mode,
			"selectedTimeRange": DateTimeRange}
			
		id=uuid.uuid4()
		TripRequests={}
		for k in TripRequests:
			if k == id:
				return "TripRequest already submitted", 403
			for {timeOpening, mode, DateTimeRange} in TripRequests[v]:
				if timeOpening == TimeOpening:
					return "Cannot create a trip request twice for the same time opening", 403
				elif  (timeOpening == timeOpening, mode == 'passenger') and (DateTimeRange = {
		    'start': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=15, minute=30, second=0),
		    'end': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=20, minute=0, second=0)
		    }):
					return "Cannot be passenger in the AM and driver in the PM", 403 
				elif ({timeOpening[deadline] == datetime.datetime(year=t.year, month=t.month, day=t.day, hour=15, minute=0, second=0) and (DateTimeRange =={
		    'start': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=15, minute=30, second=0),
		    'end': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=20, minute=0, second=0)
		    }) or ({timeOpening[deadline] == datetime.datetime(year=t.year, month=t.month, day=t.day, hour=21, minute=0, second=0) and (DateTimeRange =={
		    'start': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=6, minute=30, second=0),
		    'end': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=11, minute=0, second=0)
		    }):
		    		console.log ("Deadline has passed", 403)
					## not sure how to identify the deadline to make sure TripRequest is being created before the deadline
				else:
					TripRequests={id:tripRequest}
					TripRequests.append(tripRequest)

		return tripRequest, 200


	def putRequest(self,tripRequest):
		"""the put method is used to update the details of trip request"""
		"""Cannot modify a trip request after the deadlne and can only modify the time range + mode"""
		parser-reqparse.RequestParser()
		parser.add_argument("id")
		args=parser.parse_args()

		if TripRequest[id] in TripRequests:
			return "That trip does not exist", 404

		t=datetime.datetime.now()

		if t.hour > 15 :
		  	return 'The deadline to modify a trip for today has passed', 404
		elif t.hour > 21:
		  	return ' The deadline to modiy a trip for tomorrow AM has passed', 404
		else:		
			tripRequest[id] = {
			mode: args[mode],
			selectedTimeRange: args[DateTimeRange]
			}
		return tripRequest, 200


	def delete(self,tripRequest):
		""" the delete method is used to delete a request"""

		global trips
		trips = [trip for trip in TripRequests if trip["id"] != "id"]
		return "{} is deleted.".format(trip), 200

	
	def getRequests(self):
		# they never mentioned a user in their data structures so all the requests mentioned above are mine
		# return the content of the dictionary with status 200

	

	def getRequest(self):
		# get request ID from URL and look it up in the dictionary
		# error 404 if not found
		# return the TripRequest found with status 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)





