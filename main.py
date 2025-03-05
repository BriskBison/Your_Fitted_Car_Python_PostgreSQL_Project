import sys

from questa import Questions
from atton import Check
# from tables import Data

# Note, the tables.py file contains code that creates tables in PostgreSQL and then performs operations on them. 
# To properly perform these functions, you should connect to your local Postgre and enter the appropriate port and password at the beginning of the tables.py file.
# I've included instructions in the tables.py file for finding the port in PostgreSQL. The password should be the same as the one you chose when you installed PostgreSQL.
# If you can do this, please remove the " # " before " tables import Data " so that the program is fully executed and displays the statistics and tables :)
from numpan import Pando
import time

print("Welcome at our program. Let's find the best car for you :)")
print("We have to ask you a few question to check which car are you looking for.")

def engine():

    while True:

        q = Questions()

        q.question1()
        q.question2()
        q.question3()
        q.question4()


        value_to_find = [1]
        k1 = [key for key, value in q.cars.items() if value == value_to_find]

        value_to_find = [2]
        k2 = [key for key, value in q.cars.items() if value == value_to_find]

        value_to_find = [4]
        k4 = [key for key, value in q.cars.items() if value == value_to_find]


        check = [k1, k2, k4]

        for x in check:
            if len(x) == 0:
                check.remove(x)

        if len(k1) > 0:
            q.question5()

        if len(k2) > 0:
            q.question6()

        if len(k4) > 0:
            q.question7()


        c = Check()

        c.check()
        c.check1()
        c.check2()
        c.check3()
        c.check4()
        c.check5()
        c.check6()
        c.check7()

        try:
            while True:
                engine_check = input(
                    "Do you want to check the best car for you again or see more statistics about cars? "
                    "Type 'yes' or 'stats': ").lower().strip()
                if engine_check in ["yes", "stats"]:
                    break
                else:
                    print("Invalid input! Please type 'yes' or 'stats'.")

            if engine_check == "stats":
                time.sleep(2)
                print("Let's find out more about cars and your choice")
            elif engine_check == 'yes':
                engine()

            d = Data()

            print("Firstly, we have to create our tables")
            d.table1()
            d.enum()
            d.table2()
            time.sleep(2)

            print("Now we have to add our cars")
            d.values1()
            d.values2()
            time.sleep(2)

            queries = [
                ("How many American cars are also prepared for off-road", d.query1),
                ("Which cars have the longest names depending on the country", d.query2),
                ("Which cars have the least features", d.query3),
                ("Which cars are from Japan and America, and which are also suitable for off-road use or are fast",
                 d.query4)
            ]

            for desc, query_func in queries:
                print("\n")

                while True:
                    show_query = input(f"Do you want to see the result of: '{desc}'? (yes/no): ").lower().strip()
                    if show_query in ["yes", "no"]:
                        break
                    else:
                        print("Invalid input! Please type 'yes' or 'no'.")

                if show_query == "yes":
                    query_func()

        except Exception as e:
            print(f" An error occurred: {e}")
            print("Please try again.")

        time.sleep(2)
        print("\n")
        print("To have a better view, we can rank each car in the table")
        time.sleep(2)
        d.query5()
        print("\n")

        p = Pando()

        p.chart1()
        time.sleep(3)
        print("\n")

        p.chart2()
        time.sleep(3)
        print("\n")

        p.chart3()
        time.sleep(3)
        print("\n")

        p.chart4()
        time.sleep(3)
        print("\n")

        p.chart5()

        print("Thank you for taking part in the program. "
              "I hope you managed to find your best car. "
              "Remember to always drive carefully, fasten your seat belt and have limited trust in other drivers")
        sys.exit()

engine()
