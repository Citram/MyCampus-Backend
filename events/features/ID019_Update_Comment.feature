Feature: Update Comment
As a Registered User
I would like to be able to modify a comment
So that I can correct any possible mistakes 

  Scenario: Registered User Modifies a Comment (Normal Flow)
  Given user <user_name> is user id <user_id> is of status <user_status> logged in
  When user <user_name> requests modification of a comment with id <comment_id> 
  And content <comment_content>
  Then the content is updated to <comment_content> in the system
  
      | user_name  | user_id | user_status | comment_id | comment_content
      |  Peppa Pig | A0001 | logged in | a1001 |  "I want to go!"
      | George Pig | Z9998  | logged out |z0990 |  "But there are no dinosaurs!"


  Scenario: User not logged in (Error Flow)
  Given "George Pig" is logged out
  When "George Pig" requests modification of a comment with id 
  Then a "You must be logged in to delete a comment :(" message is issued
  
  Scenario: Attempt to modify another user's comment (Error Flow)
  Given "George Pig" with user id Z9998 is logged in
  When "George Pig" requests deletion of a comment with id a1001
  And a1001 is not associated with the Z9998
  Then a "You can only modify your own comment :)" message is issued
  
  
