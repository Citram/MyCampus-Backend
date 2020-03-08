Feature: Create New User

As a registered McGill student
I would like to become a user of the MyCampus Application System
So that I can create events and participate in other events created by my peers 

  Scenario: Create user (Normal Flow)
    Given student with username <username>
     When student <username> with password <password> requests user access to the MyCampus Application System
      | username  | password     | password2    | 
      | mycampus1 | android1298  | android1298  | 
      | citram37  | django234243 | django234243 | 
     Then a new user with username <username> is generated in the system
      | username  | 
      | mycampus1 | 
      | citram37  | 

  Scenario: Create duplicate user (Error Flow)
    Given student with username <username>
     When student <username> with password <password> requests user access to the MyCampus Application System
      | username  | password     | password2    | 
      | mycampus1 | android1298  | android1298  | 
      | mycampus1 | django234243 | django234243 | 
     Then a error message "A user with that username already exists." is issued

  Scenario: Create user with non-matching passwords (Error Flow)
    Given student with username <username>                                                            
     When student <username> with non-matching passwords requests user access to the MyCampus Application System
      | username  | password    | password2   |
      | mycampus1 | android1298 | django12345 |
     Then a error message "The two password fields didn’t match." is issued    