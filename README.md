# Elevator_System
Elevator System design Backend made using Django_rest_framework
It is comparable to a buiding with many elevators Contains the primary key that Django's default ID parameter has assigned as well. we can have various elevator systems.
<h1>API OVERVIEW</h1>
`GET/POST api/system/`
View all the elevator systems and add any system with the following request body<br>
{
system_name : string,<br>
total_floors: int<br>
number_of_elevators:int<br>
}


`GET api/system/{elevator-system-id}/show_elevators/`
Given an elevator system list all the elevators and their status.

![image](https://github.com/gargpuneet438/Elevator_System/assets/43969940/5817f25d-62cd-4b8f-ae29-4c7093d9d302)


`GET/PUT api/system/{elevator-system-id}/elevator/{elevator-number}/`
Get details of a specific elevator, given its elevator system id and elevator number 

![image](https://github.com/gargpuneet438/Elevator_System/assets/43969940/79bd5039-a76a-4b89-8eec-5b397f6a5a07)

Using PUT method we can do following things:<br>
Fetch/Update if the elevator is moving up or down currently<br>
Mark a elevator as not working or in maintenance <br>
Open/close the door.<br>
![image](https://github.com/gargpuneet438/Elevator_System/assets/43969940/d8d0764f-46f6-4c0a-8509-cac95b9084bf)


`POST api/system/{elevator-system-id}/elevator/{elevator-number}/make_request`
Input the elevator system, elevator number, and elevator URL to create a new request for a specific elevator. The form data is transmitted along with the requested and destination fields' inputs.

![image](https://github.com/gargpuneet438/Elevator_System/assets/43969940/f6168440-c256-4fe0-a731-e31ae1ebc69f)


`GET api/system/{elevator-system-id}/elevator/{elevator-number}/destination/`
Fetch the next destination floor for a given elevator

![image](https://github.com/gargpuneet438/Elevator_System/assets/43969940/039514dd-ef0c-4160-8327-1bed87a49686)


`GET api/system/{elevator-system-id}/elevator/{elevator-number}/req_current_status/`
List all the requests for a given elevator. Requests already served can be filtered with is_active parameter set false.

![image](https://github.com/gargpuneet438/Elevator_System/assets/43969940/dc91ea76-e989-4e1d-85fd-2587d5e68d5b)







