Hello and welcome :)

I will try to describe the program as briefly as possible

1. main.py = this is the main program file

2. questa.py = this is the file with the first series of questions for the user used in main.py

3. atton.py = this is the file with the second series of questions for the user used in main.py

4. tables.py = this is the file in which I connect to PostgreSQL, I also create two tables there based on the user's previous choices and add values ​​to the tables. This file also contains queries that I use to present statistical data in the main.py file

5. numpan.py = this is the file that contains operations in the pandas and matplotlib libraries. Using pandas I display subsequent statistical data in the main.py file, while using matplotlib I display graphs.


**Here are the steps to follow to properly run the project**

-> To run the program, download all files from github using the git clone command.

-> Then open the code using an IDE and make sure that all libraries are installed

-> Run the program



**The program's operation:**

The program is designed to select the best car for the user, from the dictionary, which is presented in the questa.py file. At the beginning, the dictionary values ​​are empty lists, and each user answer will add a point to the dictionary or add nothing. In this way, at the end of the program, the car with the most points will be selected (or more than one if there is a draw) and cars that also scored a lot of points will be shown as an alternative for the user.

Cars are initially divided into three classes: off-road, drift, speed and a car for James Bond = which returns only one result. Such classification occurs already in the first three questions, therefore the append to the dictionary is (1), (2), (3), because in the end it is not the sum of points that is counted, but the length of the list of points. For this reason, the value of points does not matter, and the division of 1, 2 or 3 into each category makes sorting easier. Then you can choose cars that have for example (3) in the dictionary value to select a given class.

In the second part of the program, so in the atton.py file, cars are assigned to specific features. First, an initial selection is made based on the questions from the first round, from the questa.py file. In this way, the users are asked which feature is important to them, but only about those cars that have already been indicated by them (this is specifically the check() function). So if the user indicated in the previous questions that the speed of the car is not important to them - which is why all fast cars have 0 points at this point - they will not be asked about the features typical of fast cars, unless they overlap with other choices that the user has made, e.g. they will be three-door.

The biggest advantage of the program is that it is very easily modifiable. In a situation where you need to add a car, all you need to do is:
- add it to the dictionary
- match it to the appropriate question in the questa.py file
- match it to the feature in the atton.py file
- add car to the table in PostgreSQL

The second part of the program is displaying statistical data about these cars.

Since this is my program, created 100% from scratch, I will allow myself to share the biggest difficulties I encountered while creating it:

- it took me a long time to come up with the right logic for adding points
- initially I did not know that you can iterate the dictionary by key & value, I was wrongly convinced that only by key or only by value. This discovery completely changed my capabilities
- it was also difficult for me to create try and except the correct answer in check2 and the entire ask_question() function, which contains the correct answers and compares them with those from the user


© 2025 Karol B. Krawczyk, All Rights Reserved
