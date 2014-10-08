from django.test import TestCase

from ..utils import q


class QueueTestCase(TestCase):
    """
    Tests that queue works
    No need for further tests as RQ is already tested and time-consuming
    """
    def test_empty_queue(self):
        self.assertEqual(len(q.jobs), 0)
