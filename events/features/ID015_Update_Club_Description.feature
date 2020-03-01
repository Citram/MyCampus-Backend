  Feature: Update Club Description
  
  As a club representative having a club account on the MyCampus Application System
  I would like to edit my club's description in the system
  So that the club can update their public profile 
  
  Scenario: Update club description as a logged in club represenative (Normal flow)
    Given A club representative is logged into the club account <club_name> and <club_id>
     When The representative inputs a new string <str> for the club description of <club_name> and <club_id>
     Then The club description in the system is updated to the new string <str>
     
      |club_name  |str  |
      |CSUS  |Tutoring for all ECSE and COMP classes  |
      |Mcgill DND  |Gaming for geeks and nerds  |
      |CTF  |Characterisation Task force  |
     
  Scenario: Unauthorized request to modify description of a different club (Error flow)
    Given A club representative is logged into the club account <club_name> and <club_id>
     When The representative inputs a new string <str> for the club description of <club2_name> and <club2_id>
     Then The user is redirected to an error page indicating unauthorized request
     
     
      |club_name  |club_id  |club2_name  |club2_id  | str |
      | CSUS | 19 | McGill DND | 428 | Please don't join |
      | CSUS | 19 | CSUS | 420 |The old and depecrated account|
      | CTF | 69 | CSUS | 12 | Computer Task force |


  Scenario: The requested club does not exist (Error flow)
    Given A club representative is logged into the club account <club_name>
    And The club account for <club_name> does not exist
     When The representative inputs a new string for the club description of <club2_name> and <club2_id>
     Then The user is redirected to an error page indicating that the requested club does not exist
           
           
      |club_name  |club_id  |club2_name  |club2_id  | str |
      | CSUS | 19 | McGill DND | 428 | Please don't join again |
      | CSUS | 19 | CSUS | 420 |The old and depecrated account again |
      | CTF | 69 | CSUS | 12 | Computer Task force again |
      | CTF | 69 | McGill DND | 428 | Computer Task force again |




