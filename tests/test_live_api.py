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


class StateTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(StateTestCase, self).setUp()

    def test_getStateIDs(self):
        results = self.vsmart.State.getStateIDs()
        self.assertEqual(len(results), 56)
        self.assertEqual(results[0].__dict__, {'stateId': 'NA', 'name': 'National'})
        self.assertEqual(results[1].stateId, "AS")
        self.assertEqual(results[1].name, "American Samoa")

    def test_getState(self):
        results = self.vsmart.State.getState('TX')
        self.assertEqual(results.stateId, "TX")
        self.assertEqual(results.name, "Texas")
        self.assertEqual(results.bird, "Mockingbird")

class ElectionTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(ElectionTestCase, self).setUp()

    def test_getElectionByYearState(self):
        results = self.vsmart.Election.getElectionByYearState(2010, 'TX')
        self.assertEqual(len(results), 5)
        self.assertEqual(len(results[0].stages), 3)

    def test_getElectionByZip(self):
        results = self.vsmart.Election.getElectionByZip('92821', year=2010)
        self.assertEqual(len(results), 24)

    # def test_getStageCandidates(self):
    #     results = self.vsmart.Election.getStageCandidates('839', '3296')
    #     self.assertEqual(len(results), 5)
    #
    # def test_getElection(self):
    #     results = self.vsmart.Election.getElection(839)
    #     self.assertEqual(len(results), 5)
