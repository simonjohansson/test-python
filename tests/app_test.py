from flask_testing import TestCase
from app import make_app

class AppTest(TestCase):
    def create_app(self):
        return make_app()

    def test_it_divides(self):
        rsp = self.client.get('/div?divisor=100&dividend=10')
        assert rsp.status == '200 OK'
        assert rsp.data == b'10.0'

    def test_it_complains_if_no_divisor_or_divident(self):
        rsp = self.client.get('/div')
        assert rsp.status == '200 OK'
        assert rsp.data == b'Please call with divisor and dividend'

    def test_it_does_not_accept_zero_divident(self):
        rsp = self.client.get('/div?divisor=100&dividend=0')
        assert rsp.status == '200 OK'
        assert rsp.data == "Please dont use 0 as divident"