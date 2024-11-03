import json
import csv


class CountryMedals:
    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total_medals(self):
        """total number of medals"""
        return int(self.gold) + int(self.silver) + int(self.bronze)

    def to_json(self):
        return json.dumps({
            "Country": self.name,
            "Gold": self.gold,
            "Silver": self.silver,
            "Bronze": self.bronze,
            "Total medals": self.total_medals()
        })

    def get_medals(self, medal_type):
        """obtain the number of relative medals"""
        if medal_type == 'gold':
            return self.gold
        elif medal_type == 'silver':
            return self.silver
        elif medal_type == 'bronze':
            return self.bronze
        elif medal_type == 'total':
            return self.total_medals()
        else:
            return None

    def print_summary(self):
        """output medals information for input country """
        total = self.total_medals()
        print(f"{self.name} received {self.total_medals()} medals in total; "
              f"{self.gold} gold, {self.silver} silver, and "
              f"{self.bronze} bronze.")

    def medal_difference(self, country_2):
        """compare the medals difference"""
        difference = {
            'gold': self.gold - country_2.gold,
            'silver': self.silver - country_2.silver,
            'bronze': self.bronze - country_2.bronze,
            'total': self.total_medals() - country_2.total_medals()
        }

        return difference

    def compare(self, country_2):
        """compare the medals difference between two countries"""
        print(f"Medals comparison between '{self.name}' and '{country_2.name}':")

        diff = self.medal_difference(country_2)

        """compare gold medal"""
        if diff['gold'] == 0:
            print(f"-Both {self.name} and {country_2.name} received {self.gold} gold medals(s).")
        elif diff['gold'] > 0:
            print(
                f"-{self.name} received {self.gold} gold medal(s), {diff['gold']} more than "
                f"{country_2.name}, which received {country_2.gold} of them.")
        else:
            # abs() ensure return value is positive
            print(
                f"-{self.name} received {self.gold} gold medal(s), {abs(diff['gold'])} fewer "
                f"than {country_2.name}, which received {country_2.gold} of them.")

        """compare silver medal"""
        if diff['silver'] == 0:
            print(f"-Both {self.name} and {country_2.name} received {self.silver} silver medals(s).")
        elif diff['silver'] > 0:
            print(
                f"-{self.name} received {self.silver} silver medal(s), {diff['silver']} more than "
                f"{country_2.name}, which received {country_2.silver} of them.")
        else:
            print(
                f"-{self.name} received {self.silver} silver medal(s), {abs(diff['silver'])} fewer "
                f"than {country_2.name}, which received {country_2.silver} of them.")

        """compare bronze medals"""
        if diff['bronze'] == 0:
            print(f"-Both {self.name} and {country_2.name} received {self.bronze} bronze medals(s).")
        elif diff['bronze'] > 0:
            print(
                f"-{self.name} received {self.bronze} bronze medal(s), {diff['bronze']} more "
                f"than {country_2.name}, which received {country_2.bronze} of them.")
        else:
            print(
                f"-{self.name} received {self.bronze} bronze medal(s), {abs(diff['bronze'])} fewer "
                f"than {country_2.name}, which received {country_2.bronze} of them.")

        """compare total medals"""
        if diff['total'] == 0:
            print()
            print(f"Overall, {self.name} and {country_2.name} have the same total medal(s) {self.total_medals()}.")
        elif diff['total'] > 0:
            print()
            print(
                f"Overall, {self.name} received {self.total_medals()} medal(s), {diff['total']} "
                f"more than {country_2.name}, which received {country_2.total_medals()} medal(s).")
        else:
            print()
            print(
                f"Overall, {self.name} received {self.total_medals()} medal(s), {abs(diff['total'])} "
                f"less than {country_2.name}, which received {country_2.total_medals()} medal(s).")

    def load_csv_file(self, filename):
        countries = {}
        with open(filename, 'r', encoding='UTF-8-sig') as file:
            # read the csv file in dictionary
            file_reader = csv.DictReader(file, delimiter=',', quotechar='"')
            for row in file_reader:
                # print(row)
                country_name = row['Team/NOC']

                # try to skip the country name if they are null
                if not country_name:
                    continue

                # if value is null, set to 0
                country = CountryMedals(
                    name=country_name,
                    gold=int(row.get('Gold', 0) or 0),
                    silver=int(row.get('Silver', 0) or 0),
                    bronze=int(row.get('Bronze', 0) or 0)
                )
                # put the objects into the dict
                countries[country.name] = country

        return countries

    def get_sorted_list_of_country_names(self, countries):
        return sorted(countries.keys())

    def sort_countries_by_medal_type_ascending(self, countries, medal_type):
        sorted_countries = sorted(
            countries.values(),
            key=lambda medals: medals.get_medals(medal_type)
        )
        return sorted_countries

    def sort_countries_by_medal_type_descending(self, countries, medal_type):
        sorted_countries = sorted(
            countries.values(),
            key=lambda medals: medals.get_medals(medal_type),
            reverse=True
        )
        return sorted_countries

    def read_positive_integer(self):
        while True:
            user_input = int(input("Enter the threshold (a positive integer): "))
            try:
                if user_input >= 0:
                    return user_input
                else:
                    print("Please enter a positive integer (0 or higher)")
            except ValueError:
                print("Invalid input, please try again!")

    def read_country_name(self, countries):
        while True:
            print("Available countries:", ", ".join(countries.keys()))
            user_input = input("Insert a country name ('q' for quite): ").strip().title()

            if user_input in countries:
                return user_input
            else:
                print("Invalid country name, please choose valid country from the available option.")

    def read_medal_type(self):
        medals_list = ['gold', 'silver', 'bronze', 'total']
        while True:
            # print("Available countries:", ", ".join(medals_list))
            medal_type = input(
                "Insert a medal type (chose among 'gold', 'silver', 'bronze', or 'total'): ").strip().lower()

            if medal_type in medals_list:
                return medal_type
            else:
                print("Invalid medal type. Please choose from the available options.")

    def execution_loop(self):
        countries = instance.load_csv_file('medals.csv')

        while True:
            user_input = input("Insert a command (Type 'H' for help ):").strip().upper()

            if user_input == 'H':
                print()
                print("List of commands:")
                print("- (H)elp shows the list of comments;")
                print("- (L)ist shows the list of countries present in the dataset;")
                print("- (S)ummary prints out a summary of the medals won by a single country;")
                print("- (C)ompare allows for a comparison of the medals won by two countries;")
                print(
                    "- (M)ore, given a medal type, lists all the countries that received more medals than a threshold;")
                print(
                    "- (F)ewer, given a medal type, lists all the countries that received fewer medals than a "
                    "threshold;")
                print("- (E)xport, save the medals table as '.json' file;")
                print("- (Q)uit.")

            # List shows the list of countries present in the dataset
            elif user_input == 'L':
                country_name = instance.get_sorted_list_of_country_names(countries)
                print()
                print(f"The dataset contains {len(countries)} countries: {', '.join(country_name)}")
                print()

            # Summary prints out a summary of the medals won by a single country;
            elif user_input == 'S':
                user_input_country = self.read_country_name(countries)
                if user_input_country in countries:
                    select_country = user_input_country
                    select_country = countries[select_country]
                    select_country.print_summary()
                print()

            # Compare allows for a comparison of the medals won by two countries;
            elif user_input == 'C':
                print()
                print("Compare two countries")
                country1 = input(">>Insert a country name ('q' for quit): ").strip().title()

                if country1 not in countries:
                    print(f"Country '{country1}' is not found in the dataset")
                    print("Please try again")
                    continue

                print()
                print(f"Insert the name of the country you want to compare against {country1}")
                country2 = input(">>Insert a country name ('q' for quit): ").strip().title()

                print()
                if country2 not in countries:
                    print(f"Country '{country1}' is not found in the dataset")
                    print("Please try again")
                    continue

                countries[country1].compare(countries[country2])

            # More, given a medal type, lists all the countries that received more medals than a threshold
            elif user_input == 'M':
                print("Given a medal type, lists all the countries that received more medals than a threshold;")
                medal_type = self.read_medal_type()
                medal_num = self.read_positive_integer()

                # extract the country in which medals number bigger than threshold
                over_countries_list = []
                for country in countries.values():
                    if country.get_medals(medal_type) > medal_num:
                        over_countries_list.append(country)

                # cover the list to dict
                over_countries_dict = {}
                for country in over_countries_list:
                    country_name = country.name
                    over_countries_dict[country_name] = country

                # sort the value in descending order
                sorted_countries = self.sort_countries_by_medal_type_descending(over_countries_dict, medal_type)

                print(f"Countries that received more than {medal_num} '{medal_type}' medals:")
                print()
                for country in sorted_countries:
                    print(f" - {country.name} received {country.get_medals(medal_type)}")
                print()

            # Fewer, given a medal type, lists all the countries that received fewer medals than a threshold;")
            elif user_input == 'F':
                print("Given a medal type, lists all the countries that received more medals than a threshold;")
                medal_type = self.read_medal_type()
                medal_num = self.read_positive_integer()

                # extract the country in which medals number bigger than threshold
                over_countries_list = []
                for country in countries.values():
                    if country.get_medals(medal_type) < medal_num:
                        over_countries_list.append(country)

                # cover the list to dict
                over_countries_dict = {}
                for country in over_countries_list:
                    country_name = country.name
                    over_countries_dict[country_name] = country

                # sort the value in descending order
                sorted_countries = self.sort_countries_by_medal_type_ascending(over_countries_dict, medal_type)

                print(f"Countries that received more than {medal_num} '{medal_type}' medals:")
                print()
                for country in sorted_countries:
                    print(f" - {country.name} received {country.get_medals(medal_type)}")
                print()

            # Export, save the medals table as '.json' file;
            elif user_input == 'E':
                filename_input = input("Enter the file name (.json): ")
                filename = filename_input + '.json'

                # Converting data from all countries into a nested dictionary
                # countries_dict = {
                #     country_name: {
                #         "Gold": country_medals.gold,
                #         "Silver": country_medals.silver,
                #         "Bronze": country_medals.bronze,
                #         "Total medals": country_medals.total_medals()
                #     }
                #     for country_name, country_medals in countries.items()
                # }

                countries_dict = {}

                for country_name, country_medals in countries.items():
                    json_string = country_medals.to_json()
                    country_data = json.loads(json_string)
                    countries_dict[country_name] = country_data

                with open(filename, 'w', encoding='UTF-8-sig') as file:
                    json.dump(countries_dict, file, indent=4)

                print(f"File '{filename}' correctly saved.")

            # quite the loop
            elif user_input == 'Q':
                break

            else:
                print("Invalid input, please enter the valid choice.")


# create an instance before call the methods
instance = CountryMedals(None, 0, 0, 0)
instance.execution_loop()

