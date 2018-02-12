py-votesmart changelog
==========================

0.3.5
-----
    * Fork and restructure package from Nathan Danielsen (@ndanielsen)

0.3.4
-----
    * Python3 support from Al Johri (@AlJohri)
    * Fix getOfficesByTypeLevel from Al Johri (@AlJohri)

0.3.3
-----
    * candidate rating fix from Dan Drinkard
    * getBillsByOfficial fix from Mike Shultz

0.3.2
-----
    * workaround for bugged responses from votesmart API with blank strings

0.3.1
-----
    * some bugfixes related to changes in votesmart API

0.3.0
-----
    * new votes.getByBillNumber and officials.getStatewide methods
    * Fixed __repr__ so that eval(repr(obj)) == obj for all VotesmartApiObjects
    * zip code lookup methods (contributed by Michael Stephens)
    * fix bugs in installation and elections with a single stage (thanks slinkp)

0.2.1
-----
    * fixes to places where PVS returns single items where lists are expected
    * fix allowing fetching of BillDetail amendments (thanks Josh Eastburn)

0.2.0
-----
    * first public release (superceded unpythonic internal library)
