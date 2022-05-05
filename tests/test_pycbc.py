import unittest

from asimov.event import Event
from asimov.analysis import SimpleAnalysis

class TestPyCBCIntegration(unittest.TestCase):

    def test_make_config(self):
        """Check that asimov can make a config file for pycbc."""

        subject = Event(name="GW150914")
        analysis = SimpleAnalysis(subject=subject,
                                  name="Test 1",
                                  pipeline="pycbc",
                                  interferometers=["L1", "H1"]
        )
        analysis.make_config("test.ini")
        
        pass
