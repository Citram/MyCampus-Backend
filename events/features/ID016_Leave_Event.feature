Feature: Leave Event

As a registered user of the MyCampus Application System
I would like to be able to leave an event
So that I can inform the system that I am not attending

  Background: 
    Given the events are in the system
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
  
  Scenario: Student leaves existing event (Normal Flow)
    Given "JaneDoe" is logged in with password "pass_!test123"
      And student is an attendee of the event "Java Workshop"
     When the student requests to leave event "Java Workshop"
      And event date is after current date
     Then student should be removed from the list of event attendees
  
  Scenario: Student requests to leave an existing past event (Error Flow)
    Given "JaneDoe" is logged in with password "pass_!test123"
      And student is an attendee of the event "C++ Workshop"
     When the student requests to leave event "C++ Workshop"
      And event date is before current date
     Then an error message "Event has already occurred" is given

   Scenario: Student requests to leave an existing past event (Error Flow)
    Given "JaneDoe" is logged in with password "pass_!test123"
      And student is not an attendee of the event "Java Workshop"
     When the student requests to leave event "Java Workshop"
     Then an error message "User is not signed up for event." is given
  
  
  
  
