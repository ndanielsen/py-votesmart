import os
import unittest

from votesmart import VoteSmartAPI
from votesmart.exceptions import VotesmartApiError

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

    def test_getByOfficeState_stageId(self):
        results = self.vsmart.Candidates.getByOfficeState(3, 'NJ', electionYear=2009, stageId='P')
        self.assertEqual(len(results), 8)

    def test_getByOfficeTypeState(self):
        results = self.vsmart.Candidates.getByOfficeTypeState('C', stateId='TX', electionYear='2012')
        self.assertEqual(len(results), 313)

    def test_getByLastname(self):
        results = self.vsmart.Candidates.getByLastname("Agris", electionYear="2012")
        self.assertEqual(len(results), 1)

    def test_getByLevenstein(self):
        results = self.vsmart.Candidates.getByLevenstein("Agris", electionYear="2012")
        self.assertEqual(len(results), 1)

    def test_getByElection(self):
        results = self.vsmart.Candidates.getByElection(3517)
        self.assertEqual(len(results), 223)

    def test_getByElection(self):
        results = self.vsmart.Candidates.getByElection(3517, 'G')
        self.assertEqual(len(results), 53)

    def test_getByDistrict(self):
        results = self.vsmart.Candidates.getByDistrict(29538, electionYear=2012)
        self.assertEqual(len(results), 10)

    def test_getByZip(self):
        results = self.vsmart.Candidates.getByZip(92821, electionYear=2012)
        self.assertEqual(len(results), 60)


class DistrictTestCase(LiveTestAPITestCase):

    def test_getByZip(self):
        results = self.vsmart.District.getByZip(90001)
        self.assertEqual(len(results), 11)

    def test_getByOfficeState(self):
        results = self.vsmart.District.getByOfficeState(5, 'CA')
        self.assertEqual(len(results), 53)


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
        self.assertEqual(len(results), 27)

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

class CandidateBioTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(CandidateBioTestCase, self).setUp()

    def test_getBio(self):
        results = self.vsmart.CandidateBio.getBio(176111)
        self.assertEqual(len(results), 23)

    def test_getDetailedBio(self):
        results = self.vsmart.CandidateBio.getDetailedBio(176111)
        self.assertEqual(len(results), 23)

    def test_getAddlBio_winning_candidate(self):
        results = self.vsmart.CandidateBio.getAddlBio(138524)
        self.assertEqual(len(results), 4)

    def test_getAddlBio_no_bio(self):
        with self.assertRaises(VotesmartApiError):
            results = self.vsmart.CandidateBio.getAddlBio(176111)

class RatingTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(RatingTestCase, self).setUp()

    def test_getCategories(self):
        results = self.vsmart.Rating.getCategories(stateId="CA")
        self.assertEqual(len(results), 25)

    def test_getSigList(self):
        results = self.vsmart.Rating.getSigList("2", stateId="CA")
        self.assertEqual(len(results), 6)

    def test_getSig(self):
        results = self.vsmart.Rating.getSig("331")
        self.assertEqual(len(results), 16)

    def test_getSigRatings(self):
        results = self.vsmart.Rating.getSigRatings("331")
        self.assertEqual(len(results), 3)

    def test_getCandidateRating(self):
        results = self.vsmart.Rating.getCandidateRating(138524)
        self.assertEqual(len(results), 148)

    def test_getRating(self):
        results = self.vsmart.Rating.getRating(5613)
        self.assertEqual(len(results), 117)



class OfficialsTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(OfficialsTestCase, self).setUp()

    def test_getTypes(self):
        results = self.vsmart.Officials.getTypes()
        print(results)
        self.assertEqual(len(results), 10)

    def test_getStatewide(self):
        results = self.vsmart.Officials.getStatewide(stateId='CA')
        self.assertEqual(len(results), 1858)

    def test_getByOfficeState(self):
        results = self.vsmart.Officials.getByOfficeState('73', stateId='AL')
        self.assertEqual(len(results), 17)

    def test_getByLastname(self):
        results = self.vsmart.Officials.getByLastname("Battle")
        self.assertEqual(len(results), 4)

    def test_getByLevenstein(self):
        results = self.vsmart.Officials.getByLevenstein("Battle")
        self.assertEqual(len(results), 42)

    def test_getByDistrict(self):
        results = self.vsmart.Officials.getByDistrict(31088)
        self.assertEqual(len(results), 17)

    def test_getByZip(self):
        results = self.vsmart.Officials.getByZip(90210)
        self.assertEqual(len(results), 27)


class NpatTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(NpatTestCase, self).setUp()

    def test_getByZip(self):
        results = self.vsmart.Npat.getNpat(176111)
        self.assertEqual(len(results), 10)


class MeasureTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(MeasureTestCase, self).setUp()

    def test_getMeasuresByYearState(self):
        results = self.vsmart.Measure.getMeasuresByYearState(2016, 'CA')
        print(results)
        self.assertEqual(len(results), 18)

    def test_getMeasure(self):
        results = self.vsmart.Measure.getMeasure(2142)
        self.assertEqual(len(results), 17)


class LeadershipTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(LeadershipTestCase, self).setUp()

    def test_getPositions(self):
        results = self.vsmart.Leadership.getPositions()
        self.assertEqual(len(results), 39)

    def test_getOfficials(self):
        results = self.vsmart.Leadership.getOfficials(leadershipId=311)
        self.assertEqual(len(results), 8)

class LocalTestCase(LiveTestAPITestCase):

    def setUp(self):
        super(LocalTestCase, self).setUp()

    def test_getCounties(self):
        results = self.vsmart.Local.getCounties('UT')
        self.assertEqual(len(results), 29)

    def test_getCities(self):
        results = self.vsmart.Local.getCities("UT")
        self.assertEqual(len(results), 22)

    def test_getOfficials(self):
        results = self.vsmart.Local.getOfficials(4018)
        self.assertEqual(len(results), 3)
