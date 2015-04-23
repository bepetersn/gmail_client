from contextlib import contextmanager
import os
import unittest
from mock import Mock
from gmail_client.message import Message

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


def message_getter_factory(file_object):
    """

    :param file_object: Open file object to be read from
                        to create the message getter.

    :return: A function that returns the raw email text
             as the imaplib.IMAP4_SSL.uid returns it.
    """

    def message_getter(*args, **kwargs):

        return ('unneeded status',
                [
                    ('unneeded headers',
                        file_object.read()
                     )
                ]
        )

    return message_getter


def create_message(file_object):

    """

    Takes an opened file object and from that generates
    a gmail_client.message.Message object. This should
    be used to create messages without having a
    connection to gmail.

    :param file_object: Opened file object to read from to create an email
    :return: An email created from `file_object`.
    """

    # create a mock gmail connection
    mock_gmail = Mock()
    mock_gmail.imap.uid = message_getter_factory(file_object)

    # create a mock mailbox
    mock_mailbox = Mock()
    mock_mailbox.gmail = mock_gmail

    fake_uid = ''

    # create a real message
    return Message(mock_mailbox, fake_uid)


class DataTestCase(unittest.TestCase):

    """
    Defines a helpful `open_message` context manager
    that handles opening and closing of a file containing
    an email, then loading it as a message for use.
    """

    @contextmanager
    def open_message(self, raw_email_filename):
        self.message_path = os.path.join(DATA_DIR, raw_email_filename)
        fo = open(self.message_path)
        yield create_message(fo)
        fo.close()

