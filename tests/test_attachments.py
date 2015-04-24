
import unittest
from gmail_client.message import Attachment, PointerAttachment


class TestPointerAttachments(unittest.TestCase):

    def test_regular_attachment_is_not_pointer(self):
        a = Attachment('my-doc.txt', 'text/html', 'This is the document contents.')
        self.assertFalse(a.is_pointer)

    def test_pointer_attachment_init(self):

        class CoolVendorAttachment(PointerAttachment):

            def fetch(self):
                pass

        a = CoolVendorAttachment()
        self.assertTrue(a.is_pointer)

        # We didn't set the name in `fetch`,
        # and by default it is None.
        self.assertIsNone(a.name)


