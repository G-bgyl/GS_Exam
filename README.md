__This is a explanation of the code for SW_exam.__

__Author__: Alicia Ge

### Get started
All the code are in file G`S_SW_Exam.py`. All code detailed explanations are in this file. 

File `GS_MotorVehecle.db` is an output of the code.

### How to run the code:

1. In command line, go to the directory `GS_Exam`.
2. run file `python3 GS_SW_Exam.py`, the aggregated metrics will print to standard output.
3. Copy any VIN number from the output above, and press Enter;
4. The detail info of the vehicle will print out.



### Code explanation
There are two main class: FakeMotorData and MotorVehicleDB.
1. Class FakeMotorData()
- The class FakeMotorData is able to randomly create fake data, connect to database, insert data from the database and get car details from the database.
- Function get_motors_data() returns information searched based on VIN number.
2. Class MotorVehicleDB()
- The class MotorVehicleDB is able to create two tables: Motors and Claims within the database, where two tables are linked by foreign key `VIN`.
- The function get_summary() returns aggregate info for fleet.


### Further thoughts
For sorted list of car data, I would add a function search_car() in Class FakeMotorData. the function should accept a field that the sorting based on, and use SQL statement to grab info from database.

Some thing like:'''Select * from Motors order by ____ desc'''