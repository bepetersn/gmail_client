
from tests.load_data import DataTestCase

EMAIL_BODY_TEXT = 'Message with a body.'


class ParsedEmailTestCase(DataTestCase):

    def test_find_text_in_email_body(self):
        with self.open_message('email-with-body.txt') as m:
            m.fetch()
            self.assertIn(EMAIL_BODY_TEXT, m.body)

