.. image:: https://travis-ci.org/ndanielsen/py-votesmart.svg?branch=develop
    :target: https://travis-ci.org/ndanielsen/py-votesmart
.. image:: https://coveralls.io/repos/github/ndanielsen/py-votesmart/badge.svg?branch=develop
    :target: https://coveralls.io/github/ndanielsen/py-votesmart?branch=develop

================
py-votesmart
================

Python 3 supported library for interacting with the Project Vote Smart API.

The Project Vote Smart API provides detailed information on politicians,
including bios, votes, and NPAT responses.
(http://votesmart.org/services_api.php)

All code is under a BSD-style license, see LICENSE for details.

================
Backstory
================
py-votesmart is a fork of the python-votesmart which is a project of Sunlight Labs (c) 2008.
Originally written by James Turk <jturk@sunlightfoundation.com>.

Original Source: https://github.com/votesmart/python-votesmart

Installation
============
py-votesmart is compatible with Python 2.7 or later, but it is preferred to use Python 3.5 or later to take full advantage of all functionality. The simplest way to install py-votesmart is from PyPI with pip, Python’s preferred package installer.

    >>> pip install py-votesmart

Usage
=====

To initialize the api, all that is required is for it to be imported and for an
API key to be defined.

(If you do not have an API key visit http://votesmart.org/services_api.php to
register for one.)

Import ``votesmart`` from ``votesmart``:

    >>> from votesmart import votesmart

And set your API key:

    >>> votesmart.apikey = '<YOUR KEY>'

---------------
address methods
---------------

Official API documentation at http://api.votesmart.org/docs/Address.html

The methods ``getCampaign(candidateId)``, ``getCampaignByElection(electionId)``,
and ``getOffice(candidateId)`` all return a list of ``Address`` objects based on
the provided election or candidate id.

Example of getting Nancy Pelosi's office:

    >>> addr = votesmart.address.getOffice(26732)[0]
    >>> print(addr.street, addr.city, addr.state)
    90 7th Street
    Suite 2-800 San Francisco CA

``getCampaignWebAddress(candidateId)`` and ``getOfficeWebAddress(candidateId)``
return a list of ``WebAddress`` objects based on the provided election or
candidate id.

Example of getting Nancy Pelosi's web addresses:
    >>> for x in votesmart.address.getOfficeWebAddress(26732):
    ...     print(x)
    http://demleader.tumblr.com/
    http://pelosi.house.gov/contact-me/email-me
    https://instagram.com/nancypelosi/
    https://plus.google.com/+NancyPelosi
    https://www.facebook.com/NancyPelosi
    https://www.flickr.com/photos/speakerpelosi/
    https://www.pinterest.com/nancypelosi/
    http://twitter.com/NancyPelosi
    http://www.democraticleader.gov/
    http://www.house.gov/pelosi/
    http://www.youtube.com/user/nancypelosi

--------------------
candidatebio methods
--------------------

Official API documentation at http://api.votesmart.org/docs/CandidateBio.html

``getBio(candidateId)`` and ``getAddlBio(candidateId)`` get a Bio object and
a series of AddlBio objects.

Example of getting Nancy Pelosi's bio:

    >>> bio = votesmart.candidatebio.getBio(26732)
    >>> print('Born', bio.birthDate, 'in', bio.birthPlace)
    Born 03/26/1940 in Baltimore, MD

    >>> for fact in votesmart.candidatebio.getAddlBio(26732):
    ...     print(fact)
    Father's Occupation: Congressman for Baltimore, Mayor of Baltimore
    Number of Grandchildren: 9

------------------
candidates methods
------------------

Official API documentation at http://api.votesmart.org/docs/Candidates.html

* ``getByOfficeState(officeId, stateId=None, electionYear=None)``
* ``getByLastname(lastName, electionYear=None)``
* ``getByLevenstein(lastName, electionYear=None)``
* ``getByElection(electionId)``
* ``getByDistrict(districtId, electionYear=None)``
* ``getByZip(zip5, zip4=None)``

All six methods return a list containing one or more Candidate objects.

Example of fetching all candidates for the NJ Gubernatorial race:

    >>> for candidate in sorted(votesmart.candidates.getByOfficeState(3, 'NJ', electionYear=2009), key=lambda x: str(x)):
    ...    print(candidate)
    Alvin Lindsay
    Brian Levine
    Carl Bergmanson
    Christian Keller
    Christopher Christie
    Christopher Daggett
    David Brown
    David Meiswinkle
    Gary Steele
    Gary Stein
    Gregory Pason
    Jason Cullen
    Jeff Boss
    Jon Corzine
    Joshua Leinsdorf
    Kenneth Kaplan
    Kostas Petris
    Richard Merkt
    Roger Bacon
    Steven Lonegan

You will notice that several candidates appear twice, this is due to an
unfortunate issue with the Vote Smart API where candidates with multiple
parties, or election statuses are duplicated.  Be careful when consuming
candidate data to dedupe using the fields you find useful.

(See http://github.com/sunlightlabs/python-votesmart/issues/closed/#issue/1)

-----------------
committee methods
-----------------

Official API documentation at http://api.votesmart.org/docs/Committee.html

``getTypes()`` returns a listing of all CommitteeType.

Example:

    >>> for c in votesmart.committee.getTypes():
    ...     print(c.committeeTypeId, c.name)
    H House
    S Senate
    J Joint

``getCommitteesByTypeState(typeId=None, stateId=None)`` returns a listing of
Committee objects, if either typeId isn't specified all committees for that
state will be returned, if state isn't specified then congressional committees
will be returned.

Example of getting all joint committees:

    >>> for c in votesmart.committee.getCommitteesByTypeState(typeId='J'):
    ...     print(c)
    Joint Committee on Printing
    Joint Committee on Taxation
    Joint Committee on the Library
    Joint Economic Committee

``getCommittee(committeeId)`` get extended details on a committee in a
CommitteeDetail object.

Example of getting details on the House Ways & Means committee:

    >>> committee = votesmart.committee.getCommittee(23)
    >>> print(committee)
    Ways and Means

``getCommitteeMembers(committeeId)`` gets a list of CommitteeMember objects
representing members of the given committee.

Example of getting all members of the House Ways & Means committee:

    >>> for member in sorted(votesmart.committee.getCommitteeMembers(23)[0:5], key=lambda x: str(x)):
    ...     print(member)
    Representative Diane Black
    Representative Earl Blumenauer
    Representative Kevin Brady
    Representative Sander Levin
    Representative Xavier Becerra

----------------
district methods
----------------

Official API documentation at http://api.votesmart.org/docs/District.html

``getByOfficeState(officeId, stateId, districtName=None)`` and ``getByZip(zip5, zip4=None)`` return a list of
District objects matching the specified criteria.

Example of getting all House districts for North Carolina:

    >>> for district in votesmart.district.getByOfficeState(5, 'NC'):
    ...     print(district)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13

----------------
election methods
----------------

Official API documentation at

``getElection(electionId)`` fetches a single Election object by electionId.

Example of getting details on NC 2008 Gubernatorial election:

    >>> election = votesmart.election.getElection(684)
    >>> print(election.name)
    North Carolina Gubernatorial 2008
    >>> for stage in election.stages:
    ...     print(stage.name, stage.electionDate)
    Primary 2008-05-06
    General 2008-11-04


``getElectionByYearState(year, stateId=None)`` and ``getElectionByZip(zip5, zip4=None, year=None)`` get all Election objects
matching a given criteria.  If stateId is not specified it defaults to national
elections.

Example of getting details on all elections in North Carolina in 2008:

    >>> for election in votesmart.election.getElectionByYearState(2008, 'NC'):
    ...     print(election)
    North Carolina Congressional 2008
    North Carolina Gubernatorial 2008
    North Carolina State Legislative 2008
    North Carolina State Judicial 2008


``getStageCandidates(electionId, stageId, party=None, districtId=None, stateId=None)``
gets a list of StageCandidate objects matching the given criteria.

Example of getting all North Carolina 2008 Gubernatorial primary candidates:

    for candidate in votesmart.election.getStageCandidates(684, 'P')

------------------
leadership methods
------------------

Official API documentation at http://api.votesmart.org/docs/Leadership.html

``getPositions(stateId=None, officeId=None)`` gets a list of LeadershipPosition
objects matching the given criteria.

Example of getting all Alaska leadership positions:

    >>> for pos in votesmart.leadership.getPositions('AK'):
    ...     print(pos.officeName, pos.name)
    State House Speaker
    State Senate President
    State Senate Majority Leader
    State House Majority Leader
    State House Majority Whip
    State Senate Minority Leader
    State House Minority Leader
    State House Minority Whip

-------------
local methods
-------------

Official API documentation at http://api.votesmart.org/docs/Local.html

``getCounties(stateId)`` and ``getCities(stateId)`` return lists of counties or
cities as Locality objects.

Example of getting all cities in Alaska:

    >>> for city in votesmart.local.getCities('AK'):
    ...     print(city.name, city.localId)
    Anchorage 1
    Fairbanks 2
    Juneau 4322

``getOfficials(localId)`` gets all Officials known for a given locality.

Example of getting all officials from Anchorage, AK:

    >>> for official in votesmart.local.getOfficials(1)[0:1]:
    ...     print(official)
    Mayor Ethan Berkowitz

---------------
measure methods
---------------

Official API documentation at http://api.votesmart.org/docs/Measure.html

``getMeasuresByYearState(year, stateId)`` gets a list of Measure objects for
the provided year and state.

Example of getting all 2008 Maryland Ballot Measures:

    >>> for measure in votesmart.measure.getMeasuresByYearState(2008, 'MD'):
    ...     print(measure.measureId, measure.title)
    1260 Video Lottery
    1261 Early Voting

``getMeasure(measureId)`` gets a MeasureDetail object providing more details
about a particular measure.

Example of getting more details on Maryland 2008 Early Voting measure:

    >>> measure = votesmart.measure.getMeasure(1260)
    >>> print(measure.source)       # just print the url -- summary is long
    http://www.elections.state.md.us/elections/2008/questions/index.html

------------
npat methods
------------

Official API documentation at http://api.votesmart.org/docs/Npat.html

NPATs are not converted into objects, the getNpat method is exceptional in that
it returns a python dict representing the NPAT in question.

Example of checking John McCain's NPAT:

    >>> print(votesmart.npat.getNpat(53270)['surveyMessage'])
    John Sidney McCain III is currently being tested through the 2016 Political Courage Test.<br><br>Deadline for returning the National Political Awareness Test is 10/27/2016

--e-----------
office methods
--------------

Official API documentation at http://api.votesmart.org/docs/Office.html

``getTypes()`` gets a list of OfficeType objects representing all office types
that the PVS API tracks.

Example call:

    >>> for type in votesmart.office.getTypes():
    ...     print(type)
    P: Presidential and Cabinet
    C: Congressional
    J: Supreme Court
    G: Governor and Cabinet
    K: State Judicial
    L: State Legislature
    S: State Wide
    H: Local Judicial
    N: Local Legislative
    M: Local Executive

``getBranches()`` gets a list of OfficeBranch objects representing all branches
that the PVS API tracks.

Example call:

    >>> for branch in votesmart.office.getBranches():
    ...     print(branch)
    E: Executive
    L: Legislative
    J: Judicial

``getLevels()`` gets a list of all OfficeLevel objects representing all office
levels that the PVS API tracks.

Example call:

    >>> for level in votesmart.office.getLevels():
    ...     print(level)
    F: Federal
    S: State
    L: Local

``getOfficesByType(typeId)``, ``getOfficesByLevel(levelId)``,
``getOfficesByTypeLevel(typeId, levelId)``, and
``getOfficesByBranchLevel(branchId, levelId)`` return a list of Office objects
based on the provided parameters.

Example of getting all Executive titles for the Local level:

    >>> for office in votesmart.office.getOfficesByBranchLevel('E', 'L'):
    ...     print(office)
    Mayor
    Public Advocate
    Council
    Comptroller
    Village Manager
    Mayor Pro Tempore

-----------------
officials methods
-----------------

Official API documentation at http://api.votesmart.org/docs/Officials.html

* ``getStatewide(stateId=None)``
* ``getByOfficeState(officeId, stateId=None)``
* ``getByLastname(lastName)``
* ``getByLevenstein(lastName)``
* ``getByElection(electionId)``
* ``getByDistrict(districtId)``
* ``getByZip(zip5, zip4=None)``

All officials methods return a list containing one or more Candidate objects.

Example of fetching all senators from California.

    >>> for official in votesmart.officials.getByOfficeState(6, 'CA'):
    ...    print(official)
    Senator Barbara Boxer
    Senator Dianne Feinstein

--------------
rating methods
--------------

Official API documentation at http://api.votesmart.org/docs/Rating.html

``getCategories(stateId=None)`` gets a list of Category objects for a given
state (national if no state provided).

Example of getting a few of the issue categories for New York:

    >>> for category in sorted(votesmart.rating.getCategories('NY')[0:5], key=lambda x: str(x)):
    ...     print(category)
    11: Business and Consumers
    13: Civil Liberties and Civil Rights
    2: Abortion
    5: Animals and Wildlife
    75: Abortion and Reproductive

``getSigList(categoryId, stateId=None)`` gets a list of Sig objects representing
all special interest groups associated with a particular category.  Optionally
a state can be provided to restrict results to a SIG operating within a
particular state.

Example of getting a few groups concerned with Environmental Issues:

    >>> for sig in votesmart.rating.getSigList(30)[0:5]:
    ...     print(sig)
    22: American Forest and Paper Association
    934: American Lands Alliance
    1792: American Society of Landscape Architects
    1081: American Wilderness Coalition
    1789: Associated Equipment Distributors


``getSig(sigId)`` gets all details available for a special interest group.

Example getting all details for Sierra Club:

    >>> sig = votesmart.rating.getSig(657)
    >>> print(sig.address, sig.city, sig.state)
    50 F Street, Northwest, Eighth Floor Washington DC

``getCandidateRating(candidateId, sigId)`` gets a Rating object representing
a candidate's rating by a particular special interest group.

Example checking how Sierra Club rated Nancy Pelosi:

    >>> for rating in votesmart.rating.getCandidateRating(26732, 657):
    ...     print(rating)
    Representative Nancy Pelosi supported the interests of the Sierra Club 100 percent in 2012.
    <BLANKLINE>
    Representative Nancy Pelosi supported the interests of the Sierra Club 100 percent in 2003.

-------------
state methods
-------------

Official API documentation at http://api.votesmart.org/docs/State.html

``getStateIDs()`` returns State objects for all states (and state-like entities)

Example of printing a few of the states returned from getStateIds:

    >>> for state in votesmart.state.getStateIDs()[0:5]:
    ...     print(state)
    NA National
    AS American Samoa
    FL Florida
    MI Michigan
    MO Missouri

``getState(stateId)`` returns a StateDetail object with all known details on
a given state.

Example of getting several details about the state of Virginia:

    >>> va = votesmart.state.getState('VA')
    >>> print(va.population, va.motto)
    8,185,867 (2012 est.) Sic Semper Tyrannis [Thus Always to Tyrants]

-------------
votes methods
-------------

Official API documentation at http://api.votesmart.org/docs/Votes.html

``getCategories(year, stateId=None)`` gets a list of Category objects for a
given year and optionally a state (national if no state provided).

Example of getting a few of the national bill categories for 2008:

    >>> for category in sorted(votesmart.votes.getCategories(2008)[0:5], key=lambda x: str(x)):
    ...     print(category)
    11: Business and Consumers
    2: Abortion
    4: Agriculture and Food
    75: Abortion and Reproductive
    7: Arts, Entertainment, and History

``getBill(billId)`` returns a BillDetail object providing details on a particular
bill.

Example of getting details on HR 7321 Auto Industry Financing bill:

    >>> bill = votesmart.votes.getBill(8528)
    >>> print(bill.officialTitle)
    HR 7321:  To authorize financial assistance to eligible automobile manufacturers, and for other purposes.
    >>> for sponsor in bill.sponsors:
    ...     print(sponsor)
    Barney  Frank
    >>> for action in bill.actions:
    ...     print(action)
    2008-12-10 - Passage
    2008-12-10 - Introduced


``getBillAction(actionId)`` returns a BillAction object providing details on
a particular action taken on a bill.

Example of getting details on an action for HR 5576:

    >>> print(votesmart.votes.getBillAction(8272))
    HR 5576: Making appropriations for the Departments of Transportation, Treasury, and Housing and Urban Development, the Judiciary, District of Columbia, and independent agencies for the fiscal year ending September 30, 2007, and for other purposes.

``getBillActionVotes(actionId)`` and
``getBillActionVoteByOfficial(actionId, candidateId)`` retrieve lists of Vote
objects for a given action (and official).

Example of getting Nancy Pelosi's vote on passage of HR 7321:

    >>> print(votesmart.votes.getBillActionVoteByOfficial(23069, 26732))
    Pelosi, Nancy: Yea


There are 8 methods that return Bill objects based on various parameters:

* ``getByBillNumber(billNumber)``
* ``getBillsByCategoryYearState(categoryId, year, stateId=None)``
* ``getBillsByYearState(year, stateId=None)``
* ``getBillsByOfficialYearOffice(candidateId, year, officeId=None)``
* ``getBillsByCandidateCategoryOffice(candidateId, categoryId, officeId=None)``
* ``getBillsBySponsorYear(candidateId, year)``
* ``getBillsBySponsorCategory(candidateId, categoryId)``
* ``getBillsByStateRecent(stateId=None, amount=None)``

Example of getting a few recently tracked bills for 2008:

    >>> for bill in votesmart.votes.getBillsByYearState(2008)[-5:]:
    ...     print(bill)
    S 3001 Defense Authorizations Bill
    S 1200 Indian Health Care Improvement Act Amendments of 2008
    S Amdt 5064 Striking Telecom Immunity from the Foreign Intelligence Surveillance Bill
    HR 6867 Emergency Extended Unemployment Compensation
    HR 6052 Public Transportation and Alternative Fuel Grants


``getVetoes(candidateId)`` returns all vetoes for a particular executive.

Example of getting all of George W. Bush's vetoes:

    >>> for veto in votesmart.votes.getVetoes(22369):
    ...     print(veto)
    HR 6331 Medicare Bill
    HR 6124 Second Farm, Nutrition, and Bioenergy Act of 2007 (Farm Bill)
    HR 2419 Farm, Nutrition, and Bioenergy Act of 2007 (Farm Bill)
    HR 2082 Intelligence Authorization Act for Fiscal Year 2008
    HR 1585 National Defense Authorization Act for Fiscal Year 2008
    HR 3963 Children's Health Insurance Program Reauthorization Act of 2007 (CHIP)
    HR 3043 Departments of Labor, Health and Human Services, and Education, and Related Agencies Appropriations Act, 2008
    HR 1495 Water Resources Development Act of 2007
    HR 976 State Children's Health Insurance Program (CHIP) Reauthorization
    S 5 Stem Cell Research Act of 2007
    HR 1591 Emergency Supplemental Appropriations Bill of 2007 with Iraq Withdrawal Timeline
    HR 810 Stem Cell Research Enhancement Act of 2005
