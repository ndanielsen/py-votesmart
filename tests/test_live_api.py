import os
import unittest

from votesmart import VoteSmartAPI


@unittest.skipIf(not os.environ.get('VOTE_SMART_API_KEY'), 'no api key')
class LiveTestAPITestCase(unittest.TestCase):

    def setUp(self):
        self.vsmart = VoteSmartAPI(api_key=os.environ.get('VOTE_SMART_API_KEY'))


class CandidatesTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(CandidatesTestCase, self).setUp()

    def test_getByOfficeState(self):
        results = self.vsmart.Candidates.getByOfficeState(3, 'NJ', electionYear=2009)
        self.assertEqual(len(results), 20)
