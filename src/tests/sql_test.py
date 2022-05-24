import unittest
from services.tables import *
from services.connection import get_connection

class TestTables(unittest.TestCase):
    def setUp(self):
        print("")

    def test_connection_setup(self):
        testcon = get_connection()
        testcur = testcon.cursor()
        self.assertEqual(type(testcur),type(setup()))


