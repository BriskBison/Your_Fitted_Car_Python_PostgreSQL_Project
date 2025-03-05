import sys

class Questions():

    cars = {
        "Dodge RAM": [],
        "Jeep Cherokee": [],
        "Toyota Hilux": [],
        "Nissan Skyline GTR": [],
        "Enzo Ferrari": [],
        "Lamborghini Aventador": [],
        "Toyota Supra": [],
        "BMW Serie 3": [],
        "Nissan 350z": [],
        "Aston Martin DB12": [],
    }

    def ask_question(self, question_text, valid_answers):
        while True:
            try:
                answer = input(question_text).lower().strip()
                if answer in valid_answers:
                    return answer
                else:
                    print(f"Wrong answer, please choose one of these: {', '.join(valid_answers)}")
            except Exception as e:
                print(f"ERROR! {e} Please try again.")


    def question1(self):
        answer1 = self.ask_question("Do you like off-road cars? Type 'yes' or 'no' ", ["yes", "no"])
        if answer1 == "yes":
            self.cars["Dodge RAM"].append(1)
            self.cars["Toyota Hilux"].append(1)
            self.cars["Jeep Cherokee"].append(1)

    def question2(self):
        answer2 = self.ask_question("Do you like to drift? Type 'yes' or 'no' ", ["yes", "no"])
        if answer2 == "yes":
            self.cars["Toyota Supra"].append(2)
            self.cars["BMW Serie 3"].append(2)
            self.cars["Nissan 350z"].append(2)

    def question3(self):
        answer3 = self.ask_question("Is your surname 'Bond'? Type 'yes' or 'no' ", ["yes", "no"])
        if answer3 == "yes":
            print("In that case for you there is only one choice - Aston Martin. Great taste, Mr./Mrs. Bond")
            sys.exit()

    def question4(self):
        answer4 = self.ask_question("Speed is very important for you? Type 'yes' or 'no' ", ["yes", "no"])
        if answer4 == "yes":
            self.cars["Nissan Skyline GTR"].append(4)
            self.cars["Enzo Ferrari"].append(4)
            self.cars["Lamborghini Aventador"].append(4)

    def question5(self):
        answer5 = self.ask_question("Do you prefer American or Japanese cars? "
                                    "Type 'American'/'Japanese', 'neither' or 'both' ", ["american", "japanese", "both", "neither"])
        if answer5 == "american":
            self.cars["Jeep Cherokee"].append(1)
            self.cars["Dodge RAM"].append(1)
            answer6 = self.ask_question("Do you prefer modern or old cars? "
                                        "Type 'modern'/'old' or 'both' ", ["modern", "old", "both"])
            if answer6 == "modern":
                self.cars["Dodge RAM"].append(1)
            elif answer6 == "old":
                self.cars["Jeep Cherokee"].append(1)
            elif answer6 == "both":
                self.cars["Jeep Cherokee"].append(1)
                self.cars["Dodge RAM"].append(1)
        elif answer5 == "japanese":
            self.cars["Toyota Hilux"].append(1)
        elif answer5 == "both":
            self.cars["Jeep Cherokee"].append(1)
            self.cars["Dodge RAM"].append(1)
            self.cars["Toyota Hilux"].append(1)
            answer6 = self.ask_question("Do you prefer modern or old cars? "
                                        "Type 'modern' / 'old' or 'both' ", ["modern", "old", "both"])
            if answer6 == "modern":
                self.cars["Dodge RAM"].append(1)
                self.cars["Toyota Hilux"].append(1)
            elif answer6 == "old":
                self.cars["Jeep Cherokee"].append(1)
            elif answer6 == "both":
                self.cars["Jeep Cherokee"].append(1)
                self.cars["Dodge RAM"].append(1)
                self.cars["Toyota Hilux"].append(1)

    def question6(self):
        answer7 = self.ask_question("Do you prefer German or Japanese cars? "
                                    "Type 'German'/'Japanese', 'neither' or 'both' ", ["german", "japanese", "both", "neither"])
        if answer7 == "japanese":
            self.cars["Nissan 350z"].append(2)
            self.cars["Toyota Supra"].append(2)
            answer8 = self.ask_question("Do you prefer shorter or longer cars? "
                                        "Type 'shorter'/'longer' or 'both' ", ["shorter", "longer", "both"])
            if answer8 == "shorter":
                self.cars["Nissan 350z"].append(2)
            elif answer8 == "longer":
                self.cars["Toyota Supra"].append(2)
            elif answer8 == "both":
                self.cars["Nissan 350z"].append(2)
                self.cars["Toyota Supra"].append(2)
        elif answer7 == "german":
            self.cars["BMW Serie 3"].append(2)
        elif answer7 == "both":
            self.cars["Nissan 350z"].append(2)
            self.cars["Toyota Supra"].append(2)
            self.cars["BMW Serie 3"].append(2)
            answer8 = self.ask_question("Do you prefer shorter or longer cars? "
                                        "Type 'shorter'/'longer' or 'both' ", ["shorter", "longer", "both"])
            if answer8 == "shorter":
                self.cars["Nissan 350z"].append(2)
                self.cars["BMW Serie 3"].append(2)
            elif answer8 == "longer":
                self.cars["Toyota Supra"].append(2)
            elif answer8 == "both":
                self.cars["Nissan 350z"].append(2)
                self.cars["Toyota Supra"].append(2)
                self.cars["BMW Serie 3"].append(2)

    def question7(self):
        answer9 = self.ask_question("Do you prefer Italian or Japanese cars? "
                                    "Type 'Italian'/'Japanese', 'neither' or 'both' ", ["italian", "japanese", "both", "neither"])
        if answer9 == "italian":
            self.cars["Enzo Ferrari"].append(4)
            self.cars["Lamborghini Aventador"].append(4)
            answer10 = self.ask_question("Do you prefer more sharp or more round cars? "
                                         "Type 'sharp'/'round' or 'both' ", ["sharp", "round", "both"])
            if answer10 == "sharp":
                self.cars["Enzo Ferrari"].append(4)
            elif answer10 == "round":
                self.cars["Lamborghini Aventador"].append(4)
            elif answer10 == "both":
                self.cars["Enzo Ferrari"].append(4)
                self.cars["Lamborghini Aventador"].append(4)
        elif answer9 == "japanese":
            self.cars["Nissan Skyline GTR"].append(4)
        elif answer9 == "both":
            self.cars["Enzo Ferrari"].append(4)
            self.cars["Lamborghini Aventador"].append(4)
            self.cars["Nissan Skyline GTR"].append(4)
            answer10 = self.ask_question("Do you prefer more sharp or more round cars? "
                                         "Type 'sharp'/'round' or 'both' ", ["sharp", "round", "both"])
            if answer10 == "sharp":
                self.cars["Enzo Ferrari"].append(4)
            elif answer10 == "round":
                self.cars["Lamborghini Aventador"].append(4)
                self.cars["Nissan Skyline GTR"].append(4)
            elif answer10 == "both":
                self.cars["Enzo Ferrari"].append(4)
                self.cars["Lamborghini Aventador"].append(4)
                self.cars["Nissan Skyline GTR"].append(4)
