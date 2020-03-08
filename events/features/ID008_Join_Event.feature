Feature: Join Event

As a registered user of the MyCampus Application System
I would like to be able to join an event
So that I can be admitted into the event

  Background: 
    Given the following events are in the system
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
  
  Scenario: Student joins event not at max capacity (Normal Flow)
    Given Student "Jan" is logged in with password "mycampus1234"
     When the student requests to join event "Java Workshop"
      And number of attendees of the event "Java Workshop" has not reached maximum capacity
      And event "Java Workshop" date is after current date
     Then student should be added to the list of event attendees of "Java Workshop"
  
  Scenario: Student requests to join event past event (Error Flow)
    Given Student "Jan" is logged in with password "mycampus1234"
     When the student requests to join event "C++ Workshop"
      And event "C++ Workshop" date is before current date
     Then a error message "Event has already occurred." is issued

  Scenario: Student requests to join full event (Error Flow)
    Given Student "Jan" is logged in with password "mycampus1234"
      And max capacity of "Java Workshop" has been reached
     When the student requests to join event "Java Workshop"
     Then a error message "Max capacity of event reached." is issued
  
  Scenario: Student requests to join event non-existing event (Error Flow)
    Given Student "Jan" is logged in with password "mycampus1234"
     When the student requests to join event "Python Workshop"
     Then a error message "Event not found" is issued
