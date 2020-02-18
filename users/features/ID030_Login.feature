Feature: Delete Event

As a registered user of the MyCampus Application System
I would like to delete events that I have created 
So that I can inform other users that an event will not be happening

  Scenario: Login with existing user (Normal Flow)
    Given the following users are in the system:
      | username  | password     | password2    | 
      | mycampus1 | android1298  | android1298  | 
      | citram37  | django234243 | django234243 | 
     When student "mycampus1" with password "android1298" requests user access to the MyCampus Application System
     Then the system should authenticate the student
  
   Scenario: Login with non-existing user (Error Flow)
    Given the following users are in the system:
      | username  | password     | password2    | 
      | mycampus1 | android1298  | android1298  | 
      | citram37  | django234243 | django234243 | 
     When student "mycampus2" with password "android1298" requests user access to the MyCampus Application System
     Then the system should not authenticate the user

   Scenario: Login with incorrect password(Error Flow)
    Given the following users are in the system:
      | username  | password     | password2    | 
      | mycampus1 | android1298  | android1298  | 
      | citram37  | django234243 | django234243 | 
     When student "mycampus1" with password "django234243" requests user access to the MyCampus Application System
     Then the system should not authenticate the user
  
  
  
 
  
  