from django.test import TestCase, Client
from django.urls import reverse
from .models import Booking
import json

class BookingAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_bookings_post(self):
        # Prepare data for POST request
        data = {
            'first_name': 'John',
            'reservation_date': '2024-01-01',
            'reservation_slot': 1
        }

        # Send POST request to the endpoint
        response = self.client.post('/api/bookings/', json.dumps(data), content_type='application/json')

        # Check if the response status code is 200 (successful POST)
        self.assertEqual(response.status_code, 200)

        # Check if the booking was created in the database
        created_booking = Booking.objects.filter(first_name='John').first()
        self.assertIsNotNone(created_booking)

        # Check if the created booking data matches the data sent
        self.assertEqual(created_booking.reservation_date, '2024-01-01')
        self.assertEqual(created_booking.reservation_slot, 1)

    def test_bookings_get(self):
        # Send GET request to the endpoint
        response = self.client.get('/api/bookings/')

        # Check if the response status code is 200 (successful GET)
        self.assertEqual(response.status_code, 200)

        # Ensure the response content type is JSON
        self.assertEqual(response['content-type'], 'application/json')

        # Check the content of the response JSON data
        json_response = response.json()
        self.assertGreater(len(json_response), 0)  # Ensure there are bookings returned


