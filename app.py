from flask import Flask
from flask_restful import Api
from resources import HotelResource, RoomResource, BookingResource
from models import HotelSystem

app = Flask(__name__)
api = Api(app)

# Register API resources
api.add_resource(HotelResource, '/hotels', '/hotels/<int:hotel_id>')
api.add_resource(RoomResource, '/rooms/<int:hotel_id>')
api.add_resource(BookingResource, '/bookings')

if __name__ == '__main__':
    app.run(debug=True)
