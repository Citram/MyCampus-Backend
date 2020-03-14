Feature: Edit User Attribute

As a registered McGill student
I would like to edit the information about my user in the system
So that I can ensure that the information in the system is accurate

  Background: 
    Given the following users are in the system:
      | username  | password     | email               | 
      | mycampus1 | android1298  | test@mail.mcgill.ca | 
      | citram37  | django234243 | cit@mail.mcgill.ca  | 
  
  Scenario: Edit Password (Normal Flow)
    Given student with username "mycampus1" is logged in
     When student requests to change password to "android1234"
      And student is enters old password "android1298"
     Then the password of "mycampus1" is updated to "android1234"
  
  Scenario: Edit Email (Alternate Flow)
    Given student with username "mycampus1" is logged in
     When student requests to change password to "test2@mail.mcgill.ca"
     Then the email of "mycampus1" is updated to "test2@mail.mcgill.ca"
  
  Scenario: Edit Password Confirmation Password Incorrect (Error Flow)
    Given student with username "mycampus1" is logged in
     When student requests to change password to "android1234"
      And student is enters old password "android1234"
     Then the error message "Please enter the correct confirmation password" is issued
  
  Scenario: Edit Password New Password Incorrect Format (Error Flow)
    Given student with username "mycampus1" is logged in
     When student requests to change password to "abcd"
      And student is enters old password "android1298"
     Then the error message "Password is too short." is issued
  
  Scenario: Edit Email New Email Incorrect Format (Error Flow)
    Given student with username "mycampus1" is logged in
     When student requests to change password to "test2@gmail.com"
     Then the error message "Only @mail.mcgill.ca emails are permitted." is issued
  