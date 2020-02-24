Feature: Edit Event

As a registered user of the MyCampus Application System
I would like to be able to edit events that I have created
So that I can inform other students of changes 

  Scenario: Student edits existing Event (Normal Flow)
     When the student requests to edit event JavaWorkshop  
      | evt_name        | evt_date   | min_cap | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | JavaWorkshop    | 2021-01-01 | 1       | 10      | Join java workshop!   | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop    | 2021-02-01 | 2       | 30      | Advanced C++          | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Python Workshop | 2021-01-01 | 1       | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 1       | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
     Then the event with name JavaWorkshop should be updated with its new fields and stored in the system
  
  Scenario: Student edits existing event without specifying at least one field (Error Flow)
     When the student requests to edit an existing event without specifying at least one field
      | evt_name      | evt_date   | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      |               | 2021-01-01 | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop   |            | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Java Workshop | 2021-01-01 | 10      | Join java workshop!   |     | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop  | 2021-02-01 | 30      | Advanced C++          | 7   | OUT      |          | Main St.   | 21     | 123456     | 
  
     Then the request should be invalidated
      And an error message "This field is required" should be printed
  
  Scenario: Student edits exsting Event while specifying at least one invalid field (Error Flow)
     When the student requests to edit an event with at least one invalid field
      | evt_name        | evt_date   | min_cap | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | Java Workshop   | 2021-01-01 | -1      | 10      | Join java workshop!   | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop    | 2019-02-01 | 1       | 30      | Advanced C++          | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Python Workshop | 2021-01-01 | 1       | 10000   | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 1       | 30      | Advanced Go           | -7  | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
     Then the request should be invalidated
  
  