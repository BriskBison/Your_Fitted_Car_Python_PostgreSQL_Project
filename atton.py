from questa import Questions

q = Questions()

class Check():

    attributes = {
        "safe": ["Dodge RAM", "Jeep Cherokee", "Toyota Hilux"],
        "quite_safe": ["Nissan Skyline GTR", "Toyota Supra", "BMW Serie 3", "Nissan 350z"],
        "comfortable": ["Dodge RAM", "Nissan Skyline GTR", "Enzo Ferrari", "Lamborghini Aventador"],
        "cheap": ["BMW Serie 3", "Toyota Supra", "Jeep Cherokee"],
        "long-lived": ["Dodge RAM", "Toyota Hilux", "BMW Serie 3", "Nissan Skyline GTR", "Toyota Supra"],
        "economic": ["Toyota Hilux", "BMW Serie 3", "Toyota Supra", "Nissan 350z"],
        "five-door": ["Dodge RAM", "Jeep Cherokee", "Toyota Hilux", "BMW Serie 3"],
        "three-door": ["Nissan 350z", "Toyota Supra", "Nissan Skyline GTR", "Enzo Ferrari", "Lamborghini Aventador"],
        "automatic": ["Dodge RAM", "Nissan Skyline GTR", "Nissan 350z", "Toyota Hilux"],
    }

    cars2 = []

    def check(self):
        for key, value in q.cars.items():
            if len(value) >= 2:
                self.cars2.append(key)

    cars3 = []

    def check1(self):
        for key, value in self.attributes.items():
            if set(value) & set(self.cars2):
                self.cars3.append(key)

    cars4 = []
    answered_questions = set()

    def check2(self):
        for feature in self.cars3:
            if feature not in self.answered_questions:
                while True:
                    try:
                        answer = input(f"Are you looking for a car which is {feature.replace('_', ' ')}? (yes/no) ").lower().strip()
                        if answer not in ["yes", "no"]:
                            raise ValueError("Invalid input! Please type 'yes' or 'no'.")
                        if answer == "yes":
                            self.cars4.append(feature)
                        self.answered_questions.add(feature)
                        break
                    except ValueError as e:
                        print(e)

    cars5 = []

    def check3(self):
        for feature in self.cars4:
            for car in self.attributes[feature]:
                if car in self.cars2 and car not in self.cars5:
                    self.cars5.append(car)

    car_counts = {}

    def check4(self):
        for feature in self.cars4:
            for car in self.attributes[feature]:
                if car in self.car_counts:
                    self.car_counts[car] += 1
                else:
                    self.car_counts[car] = 1

    def check5(self):
        for car, count in self.car_counts.items():
            if count >= 2:
                q.cars[car].append(count)

    cars6 = []
    cars7 = []
    cars8 = []

    def check6(self):
        for key, value in q.cars.items():
            if len(value) == 4:
                self.cars6.append(key)
            if len(value) == 3:
                self.cars7.append(key)
            if len(value) == 2:
                self.cars8.append(key)

    def check7(self):
        if len(self.cars6) > 1:
            print(f"Your most fitted cars are: {', '.join(self.cars6)} ")
            if len(self.cars7) == 1:
                print(f"Another good choice for you is {', '.join(self.cars7)} ")
            elif len(self.cars7) > 1:
                print(f"Cars which are also good for you: {', '.join(self.cars7)}")
        elif len(self.cars6) == 1:
            print(f"Your most fitted car is: {', '.join(self.cars6)} ")
            if len(self.cars7) == 1:
                print(f"For you, also a good option is: {', '.join(self.cars7)}")
            elif len(self.cars7) > 1:
                print(f"Cars which are also good for you: {', '.join(self.cars7)}")
        elif len(self.cars6) == 0:
            if len(self.cars7) == 1:
                print(f"It is hard to find one perfect car for you. "
                      f"There is a car which fits you the most: {', '.join(self.cars7)}")
                print(f"Cars you should also consider: {', '.join(self.cars8)}")
            elif len(self.cars7) > 1:
                print(f"It is hard to find one perfect car for you. "
                      f"There are cars which fit you the most: {', '.join(self.cars7)}")
                print(f"Cars you should also consider: {', '.join(self.cars8)}")
            elif len(self.cars7) == 0 and len(self.cars8) < 2:
                print(f"Sorry, we couldn't find the best car for you. We don't have enough information")
