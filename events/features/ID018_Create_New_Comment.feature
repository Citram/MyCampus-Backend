Feature: Create_New_Comment
As a registered user of the MyCampus Application System
I would like to create a new comment under a posted event
So that my comment may be seen by the people viewing the post

  Scenario: Making a new comment (Normal flow)
    Given A user <user_id> is logged into his account 
     When He wants to comment a string <str> on a posted event <evt_id> as <user_id>
     Then A comment is added to the system attached to the posted event <evt_id>
     
     
      | user_id | evt_id | str |
      | 19 | 12 | I liked this |
      | 420 | 7 | Can't miss this |
      | 428 | 911 | Where do we need to go exactly |

  Scenario: Making a new comment as a user that is not logged in (Error flow)
    Given A user <user_id> is not logged into his account 
     When He wants to comment a string <str> on a posted event <evt_id> as <user2_id>
     Then The user is redirected to a page indicating unauthorised access
     
     
      | user_id | user2_id | evt_id | str |
      | 18 | 19 | 12 | I liked this |
      | 260 | 420 | 7 | Can't miss this |
      | 78 | 428 | 911 | Where do we need to go exactly |
      
      
  Scenario: Making a new comment as a user that does not exist (Error flow)
    Given A user <user_id> is logged into his account 
    And <user2_id> does not exist
     When He wants to comment a string <str> on a posted event <evt_id> as <user2_id>
     Then The user is redirected to a page indicating non-existent user
     
     
      | user_id | user2_id | evt_id | str |
      | 18 | 19 | 12 | I liked this |
      | 260 | 420 | 7 | Can't miss this |
      | 78 | 428 | 911 | Where do we need to go exactly |

  Scenario: Making a new comment on an event that does not exist (Error flow)
    Given A user <user_id> is logged into his account 
    And <evt_id> does not exist
     When He wants to comment a string <str> on a posted event <evt_id> as <user_id>
     Then The user is redirected to a page indicating non-existent event
     
     
      | user_id | evt_id | str |
      | 19 | 12 | I liked this |
      | 420 | 7 | Can't miss this |
      | 428 | 911 | Where do we need to go exactly |

      

