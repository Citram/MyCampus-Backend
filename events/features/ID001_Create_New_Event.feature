Feature: Create New Event

As a registered user of the MyCampus Application System
I would like to be able to create events 
So that I can reach out to other students on the system 

  Scenario: Student creates Event with minimum capacity (Normal Flow)
    Given Student "Lisa Bard" is logged in
     When the student requests to create an event
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
  
     Then the event should with name <evt_name> should be created and stored in the system
      | evt_name      | evt_date   | min_cap | max_cap | evt_details         | fee | category | city     | street     | number | postalcode | 
      | Java Workshop | 2021-01-01 | 1       | 10      | Join java workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 2       | 30      | Advanced C++        | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
  
  
  Scenario: Student creates Event without minimum capacity (Alternate Flow)
    Given Student "Lisa Bard" is logged in
     When the student requests to create an event without a minimum capacity
      | evt_name        | evt_date   | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | Python Workshop | 2021-01-01 | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
  
     Then the event should with name <evt_name> should be created and stored in the system
      | evt_name        | evt_date   | min_cap | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | Python Workshop | 2021-01-01 | 1       | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 1       | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 

  Scenario: Student creates event without specifying at least one field (Error Flow)
    Given Student "Lisa Bard" is logged in
     When the student requests to create an event without specifying at least one field
      | evt_name      | evt_date   | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      |               | 2021-01-01 | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop   |            | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Java Workshop | 2021-01-01 | 10      | Join java workshop!   |     | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 30      | Advanced C++          | 7   | OUT      |          | Main St.   | 21     | 123456     | 
  
     Then the request should be invalidated
      And an error message "This field is required" should be printed

        
  Scenario: Student creates Event without specifying at least one invalid field (Error Flow)
    Given Student "Lisa Bard" is logged in
     When the student requests to create an event with at least one invalid field
      | evt_name        | evt_date   | min_cap | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | Java Workshop   | 2021-01-01 | -1      | 10      | Join java workshop!   | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop    | 2019-02-01 | 1       | 30      | Advanced C++          | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Python Workshop | 2021-01-01 | 1       | 10000   | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 1       | 30      | Advanced Go           | -7  | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
     Then the request should be invalidated
  
  