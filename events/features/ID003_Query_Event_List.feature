Feature: Query Event List

As a registered user of the MyCampus Application System
I would like to query the list of events in the system 
So that I can sign up to events that interest me

  Background: 
    Given the following events are in the system
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Zumba Dance   | 2021-03-01 | 3       | 40      | Dance Dance Dance!  | 5   | DNC      | Toronto  | Younge     | 428    | 777777     | 
  
  Scenario: Student requests list of all events (Normal Flow)
  
    Given student "Boba Fett" is logged in
     When the student requests a list of events
     Then the following list of events is generated
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Zumba Dance   | 2021-03-01 | 3       | 40      | Dance Dance Dance!  | 5   | DNC      | Toronto  | Younge     | 428    | 777777     | 
  
  Scenario: Student requests list of filtered events using keyword (Alternate Flow)
  
    Given student "Boba Fett" is logged in
     When the student requests a list of events with the keyword "workshop"
     Then the following list of events is generated
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
  
  Scenario: Student requests list of filtered events using unavailable keyword (Error Flow)
  
    Given student "Boba Fett" is logged in
     When the student requests a list of events with the keyword "cat"
     Then an error message "No events available for keyword: cat" should be issued