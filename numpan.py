import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from questa import Questions
from atton import Check
from collections import Counter

q = Questions()
c = Check()

MYLABELS = ["off-roads", "speed", "drifting"]

class Pando():

    def chart1(self):
        print("Let's see a table showing which cars are best suited to you")
        result = c.cars7 + c.cars8
        data = result
        df = pd.DataFrame(data)
        print(df)

    def chart2(self):
        print("Let's see a table showing which cars are completely not for you")
        filtered_cars = {key: value for key, value in q.cars.items() if len(value) <= 2}
        df2 = pd.DataFrame(filtered_cars.keys(), columns=["Car Name"])
        print(df2)

    def chart3(self):
        print("Let's check which cars have the most useful features")
        all_cars = [car for cars_list in c.attributes.values() for car in cars_list]
        car_counts = Counter(all_cars)
        df3 = pd.DataFrame(car_counts.items(), columns=["Car Name", "Count"])
        df_sorted = df3.sort_values(by="Count", ascending=False).reset_index(drop=True)
        print(df_sorted)

    def chart4(self):

        print("Studies show that people most often choose safe, off-road cars. Let's see it on a round diagram")
        y = np.array([47, 38, 15])
        plt.pie(y, labels = MYLABELS)
        plt.legend()
        plt.pie(y)
        plt.show()


    def chart5(self):

        print("We can also see this on a bar chart")
        values = [47, 38, 15]
        colors = ['red', 'blue', 'green']

        plt.bar(MYLABELS, values, color=colors)
        plt.title("Bar Chart")
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.show()