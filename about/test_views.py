from django.test import TestCase
from django.urls import reverse

class TestAboutView(TestCase):
    """Test for collaboration request submission on the about page."""

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""

        # Prepare the post data for collaboration request
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }

        # Send a POST request to the 'about' page with the collaboration data
        response = self.client.post(reverse('about'), post_data)

        # Assert that the response status code is 200 (successful)
        self.assertEqual(response.status_code, 200)

        # Assert that the response content contains the success message
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.', response.content
        )
