from flask import Flask, request, jsonify, render_template, flash, session, redirect
from flask_restful import Api, Resource,reqparse
from datetime import date, time
import uuid

app=Flask(__name__)
api = Api(app)

DateTimeRange =[{
	'start': 'DateTime',
	'end': 'DateTime'
	}]

TimeOpening= [{
	id: 'UUID',
	'requestDeadline': DateTime,
	'timeSelectionRange': DateTimeRange,
	'timeSelectionIntervalMinutes': 5
	}
	]
	
TripRequests =[{
	id:'UUID',
	'timeOpening': TimeOpening,
	'mode': 'passenger' or 'driver',
	'selectedTimeRange': DateTimeRange
	}]
	

class Trips():

	def get(self):

		"""Get time openings for current week"""
		from datetime import datetime

	def getOpenings(self):
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
	        'start': datetime.datetime(year=t.year, month=t.month, day=t.day, hour=15:30, minute=0, second=0),
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
		

	def post(self, tripRequest):
		"""creates trip request """
		parser-reqparse.RequestParser()
		parser.add_argument("mode")
		parser.add_argument("TimeOpening")
		parser.add_argumnet("DateTimeRange")
		args=parser.parse_args()
		
		id=uuid.uuid4()
		TripRequests={id:tripRequest}
		tripRequest ={
			"id":id,
			"timeOpening": args["TimeOpening"],
			"mode": args["mode"],
			"selectedTimeRange": args["DateTimeRange"]
		}


		for TripRequest in TripRequests:
			if tripRequest[id]==TripRequest[id]:
				return "TripRequest already submitted", 403
			elif tripRequest[TimeOpening]==TripRequest[timeOpening]:
				return "Cannot create a trip request twice for the same time opening", 403
			elif tripRequest[id]==TripRequest[id] and TripRequest[mode]=='passenger' and TripRequest[TimeOpening]==tripRequest[TimeOpening]:
				and trip[mode] == 'driver':
				return "Cannot be passenger in the AM and driver in the PM", 403 
			## not sure how to identify the deadline to make sure TripRequest is being created before the deadline
			else:
				TripRequests.append(tripRequest)

		return trip, 200


	def put(self, tripRequest):
		"""the put method is used to update the details of trip request"""
		"""Cannot modify a trip request after the deadlne and can only modify the time range + mode"""
		parser-reqparse.RequestParser()
		parser.add_argument("mode")
		parser.add_argument("DateTimeRange")
		args=parser.parse_args()

		t=datetime.datetime.now()

		if t.hour > 15 :
	  		return 'The deadline to modify a trip for today has passed', 404
	  	elif t.hour > 21:
	  		return ' The deadline to modiy a trip for tomorrow AM has passed', 404
		else:		
			tripRequest[id] = {
			"mode": args["mode"],
			selectedTimeRange: args["DateTimeRange"]
			}
		return tripRequest, 200


	def delete(self, trip):
		""" the delete method is used to delete a request"""

		global trips
		trips = [trip for trip in TripRequests if trip["id"] != "id"]
		return "{} is deleted.".format(trip), 200



	
api.add_resource(start, "/trips/<string:trip>")
app.run(debug=True)






