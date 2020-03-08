Feature: Delete Comment
As a Registered User
I would like to be able to delete a comment
So that the comment no longer appears in the system 

  Scenario: Registered User Deletes a Comment (Normal Flow)
  Given user <user_name> is user id <user_id> is of status <user_status> logged in
  When user <user_name> requests deletion of a comment with id <comment_id> 
  And content <comment_content>
  Then the comment is deleted from the system
  
      | user_name  | user_id | login_status | comment_id | event_id | comment_content
      |  Peppa Pig | A0001 |logged in | a1001 |  00001 |"This will be awesome!"
      | George Pig | Z9998  | logged out |z0990 |  00001 |"But there are no dinosaurs!"

  Scenario: Event Organizer deletes a Comment (Alternate Flow)
  Given user of status <org_status> organizer
  And status <login_status> logged in
  When user requests deletion of a comment with id <comment_id> 
    And content <comment_content>
  And <comment_id> is associated with <event_id>
  Then the comment is deleted from the system
  And a "Comment deleted" message is issued
  
  | user_name  | user_id | org_status | login_status | comment_id | event_id | comment_content
      |  Peppa Pig | A0001 | organizer | logged in | a1001 |  00001 |"This will be awesome!"
      | George Pig | Z9998  | other | logged out |z0990 |  00001 |"But there are no dinosaurs!"
      | Suzie Sheep | M6667  | other | logged in |m4443 |  00001 |"I will be there"
 
 
  Scenario: User not logged in (Error Flow)
  Given "George Pig" is logged out
  When "George Pig" requests deletion of a comment with id 
  Then a "You must be logged in to delete a comment :(" message is issued
  
  Scenario: Attempt to delete another user's comment (Error Flow)
  Given "Suzie Sheep" with user id M6667 is logged in
  When "Suzie Sheep" requests deletion of a comment with id z0990
  And z0990 is not associated with the M6667
  Then a "You can only delete your own comment :)" message is issued
