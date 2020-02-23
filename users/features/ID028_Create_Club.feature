Feature: Create New Club
As a Club Representative
I want to create a club in the MyCampus Application System
So that I can create events for my club for other users to participate in

  Scenario: Club Representative Creates Club (Normal Flow)
    Given club <club_name> with club email <club_email> is a club type <club type>
     When club representative of <club_name> requests a new club in the MyCampus Application System
      | club_name   | club_email             | club_type  | password    | password2   | 
      | McGill Row  | info@mcgillrow.com     | Sports     | mcgillrows  | mcgillrows  | 
      | Code McGill | contact@codemcgill.com | Technology | wecodeinC   | wecodeinC   | 
      | Theatre MTL | hi@theatremtl.com      | Arts       | shakespeare | shakespeare | 
     Then a new club application is generated in the system
      | club_name   | club_email             | club_type  | 
      | McGill Row  | info@mcgillrow.com     | Sports     | 
      | Code McGill | contact@codemcgill.com | Technology | 
      | Theatre MTL | hi@theatremtl.com      | Arts       | 
  
  Scenario: Create Duplicate Club Name (Error Flow)
    Given club <club_name> with club email <club_email> is a club type <club type>
     When club representative of <club_name> requests a new club in the MyCampus Application System
      | club_name  | club_email             | club_type  | password   | password2  | 
      | McGill Row | info@mcgillrow.com     | Sports     | mcgillrows | mcgillrows | 
      | McGill Row | contact@codemcgill.com | Technology | wecodeinC  | wecodeinC  | 
     Then an error message "A club with that club name already exists." is issued
  
  Scenario: Create Duplicate Club Email (Error Flow)
    Given club <club_name> with club email <club_email> is a club type <club type>
     When club representative of <club_name> requests a new club in the MyCampus Application System
      | club_name   | club_email         | club_type  | password   | password2  | 
      | McGill Row  | info@mcgillrow.com | Sports     | mcgillrows | mcgillrows | 
      | Code McGill | info@mcgillrow.com | Technology | wecodeinC  | wecodeinC  | 
     Then an error message "A club with that email already exists." is issued
  
  Scenario: Create club with non-matching passwords (Error Flow)
    Given club <club_name> with club email <club_email> is a club type <club type>
     When club representative of <club_name> requests a new club in the MyCampus Application System
      | club_name  | club_email         | club_type | password   | password2   | 
      | McGill Row | info@mcgillrow.com | Sports    | mcgillrows | mcgillcodes | 
     Then an error message "The two password fields didn’t match." is issued    
  
  
