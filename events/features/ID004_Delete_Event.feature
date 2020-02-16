Feature: Delete Event

As a registered user of the MyCampus Application System
I would like to delete events that I have created 
So that I can inform other users that an event will not be happening

  Scenario: Student deletes existing Event (Normal Flow)
    Given the following events exist in the database:
      | evt_name        | evt_date   | min_cap | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | JavaWorkshop    | 2021-01-01 | 1       | 10      | Join java workshop!   | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop    | 2021-02-01 | 2       | 30      | Advanced C++          | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Python Workshop | 2021-01-01 | 1       | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 1       | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
     When the student requests to delete event JavaWorkshop  
     Then the event should with name JavaWorkshop should be deleted from the system
  
  Scenario: Student deletes existing Event (Error Flow)
    Given the following events exist in the database:
      | evt_name        | evt_date   | min_cap | max_cap | evt_details           | fee | category | city     | street     | number | postalcode | 
      | JavaWorkshop    | 2021-01-01 | 1       | 10      | Join java workshop!   | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | C++ Workshop    | 2021-02-01 | 2       | 30      | Advanced C++          | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
      | Python Workshop | 2021-01-01 | 1       | 10      | Join python workshop! | 7   | GAM      | Montreal | Sherbrooke | 400    | H1A0B3     | 
      | Go Workshop     | 2021-02-01 | 1       | 30      | Advanced Go           | 7   | OUT      | Ottawa   | Main St.   | 21     | 123456     | 
     When the student requests to delete event CWorkshop  
     Then the error message "Event not found" should be issued
  
 
  
  
 
  
  