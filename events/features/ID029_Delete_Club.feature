Feature: Delete Club
As a Registered User
I want to delete a club
So that MyCampusApplication System users know that the club no longer exists

  Scenario: Authorized Club Representative Deletes Club (Normal Flow)
    Given Club Representative is logged in with <club_email>
     When Club Representative attempts to delete club and provide <club_password>
     Then a "Club Successfully Deleted" message is issued
     And the club is deleted from the system
     And the club's events are deleted from the system

      
      | club_email | club_password |
      | info@mcgillrow.com | mcgillrows |
      | contact@codemcgill.com | wecodeinC |
      | hi@theatremtl.com | shakespeare |


Scenario: Authorized Administrator Deletes Club (Alternate Flow)
    Given Administrator is logged in with <admin_user> and <admin_password>
     When club representative attempts to delete club
     Then a "Club Successfully Deleted" message is issued
     And the club is deleted from the system
     And the club's events are deleted from the system
      
      | admin_user | club_password |
      | admin_mycampus | mycampusrocks |
      | admin_jonathon | jonathonisthebest |
      | sys_admin | iknowhowtocode |


  Scenario: Unauthorized User Attempts to Delete Club (Error Flow)
    Given John Smith is not logged in
     When John Smith attempts to delete McGill Rows club
     Then a "Not Authorized to Delete Club" message is issued
     
     
  Scenario: Authorized User Attempts to Delete Club with Incorrect Password (Error Flow)
    Given McGill Codes representative is logged in with contact@codemcgill.com
     When Club Representative attempts to delete club 
     And provides incorrect password "wecodeinJava"
     Then a "Incorrect Password" message is issued
     And the club is deleted from the system
     And the club's events are deleted from the system
