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

    def test_getStageCandidates(self):
        results = self.vsmart.Election.getStageCandidates('3217', 'G')
        self.assertEqual(len(results), 106)

    def test_getElection(self):
        results = self.vsmart.Election.getElection(3217)
        self.assertEqual(len(results), 7)


class OfficeTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(OfficeTestCase, self).setUp()

    def test_getTypes(self):
        results = self.vsmart.Office.getTypes()
        self.assertEqual(len(results), 10)

    def test_getBranches(self):
        results = self.vsmart.Office.getBranches()
        self.assertEqual(len(results), 3)

    def test_getLevels(self):
        results = self.vsmart.Office.getLevels()
        self.assertEqual(len(results), 3)

    def test_getOfficesByLevel(self):
        results = self.vsmart.Office.getOfficesByLevel('F')
        self.assertEqual(len(results), 30)

    def test_getOfficesByType(self):
        results = self.vsmart.Office.getOfficesByType("L")
        self.assertEqual(len(results), 3)

    def test_getOfficesByTypeLevel(self):
        results = self.vsmart.Office.getOfficesByTypeLevel("C", "F")
        self.assertEqual(len(results), 2)

    def test_getOfficesByBranchLevel(self):
        "Legislative federal"
        results = self.vsmart.Office.getOfficesByBranchLevel("L", "F")
        self.assertEqual(len(results), 2)
