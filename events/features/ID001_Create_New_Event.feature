  Feature: Create New Event
  
  As a registered user of the MyCampus Application System
  I would like to be able to create events 
  So that I can reach out to other students on the system 
  
  Scenario: Event doesn't have a limit registering capacity (Normal Flow)
    Given Student "Lisa Bard" is logged in
     When the student requests to create an event
       | evt_name      |  evt_date |max_cap| evt_details            |  fee | category | city | street | number | postalcode |
       | Java Workshop |  2021-01-01 | 10    | Join java workshop!   | 7 | GAM | Montreal | Sherbrooke | 400 | H1A0B3 |
     Then the event should with name <evt_name> should be created and stored in the system
                  | evt_name      |  evt_date |max_cap| evt_details            |  fee | category | city | street | number | postalcode |
            | Java Workshop |  2021-01-01 | 10    | Join java workshop!   | 7 | GAM | Montreal | Sherbrooke | 400 | H1A0B3 |

    
