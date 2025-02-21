""""Jamie Garcia SDEV 300 Section 6380 Project 3"""

# list the 3 data structures, give 1 reason you'd use that type o  data structe to store data vs the others
# and a reason why you chose the data type over the other two to hold information about the states
import sys
import os
import matplotlib.pyplot as plt

SUBDIRECTORY_PATH = "images"

state_list = [
    {
        "name": "Alabama",
        "capital": "Montgomery",
        "population": "5108468",
        "flower": "Camellia",
    },
    {
        "name": "Alaska",
        "capital": "Junaeu",
        "population": "733406",
        "flower": "Alpine forget-me-not",
    },
    {
        "name": "Arizona",
        "capital": "Phoenix",
        "population": "7431344",
        "flower": "Saguaro Cactus Blossom",
    },
    {
        "name": "Arkansas",
        "capital": "Little Rock",
        "population": "3067732",
        "flower": "Apple Blossom",
    },
    {
        "name": "California",
        "capital": "Sacramento",
        "population": "38965193",
        "flower": "California Poppy",
    },
    {
        "name": "Colorado",
        "capital": "Denver",
        "population": "5877610",
        "flower": "Columbine",
    },
    {
        "name": "Connecticut",
        "capital": "Hartford",
        "population": "3617176",
        "flower": "Mountian Laurel",
    },
    {
        "name": "Delaware",
        "capital": "Dover",
        "population": "1031890",
        "flower": "Peach Blossom",
    },
    {
        "name": "Florida",
        "capital": "Tallahassee",
        "population": "22610726",
        "flower": "Orange Blossom",
    },
    {
        "name": "Georgia",
        "capital": "Atlanta",
        "population": "11029227",
        "flower": "Cherokee Rose",
    },
    {
        "name": "Hawaii",
        "capital": "Honolulu",
        "population": "1435138",
        "flower": "Yellow Hibiscus",
    },
    {"name": "Idaho", "capital": "Boise", "population": "1964726", "flower": "Syringa"},
    {
        "name": "Illinois",
        "capital": "Springfield",
        "population": "12549689",
        "flower": "Violet",
    },
    {
        "name": "Indiana",
        "capital": "Indianapolis",
        "population": "6862199",
        "flower": "Peony",
    },
    {
        "name": "Iowa",
        "capital": "Des Moines",
        "population": "3207004",
        "flower": "Wild Rose",
    },
    {
        "name": "Kansas",
        "capital": "Topeka",
        "population": "2940546",
        "flower": "Sunflower",
    },
    {
        "name": "Kentucky",
        "capital": "Frankfort",
        "population": "4526154",
        "flower": "Giant Golderrod",
    },
    {
        "name": "Louisiana",
        "capital": "Baton Rouge",
        "population": "4573749",
        "flower": "Magnolia",
    },
    {
        "name": "Maine",
        "capital": "Augusta",
        "population": "1395722",
        "flower": "White Pine Cone",
    },
    {
        "name": "Maryland",
        "capital": "Annapolis",
        "population": "6180253",
        "flower": "Black-eyed Susan",
    },
    {
        "name": "Massachusetts",
        "capital": "Boston",
        "population": "7001399",
        "flower": "Mayflower",
    },
    {
        "name": "Michigan",
        "capital": "Lansing",
        "population": "10037261",
        "flower": "Apple Blossom",
    },
    {
        "name": "Minnesota",
        "capital": "St. Paul",
        "population": "5737915",
        "flower": "Lady Slipper",
    },
    {
        "name": "Mississippi",
        "capital": "Jackson",
        "population": "2393690",
        "flower": "Magnolia",
    },
    {
        "name": "Missouri",
        "capital": "Jefferson City",
        "population": "6196156",
        "flower": "Hawthorne Blossom",
    },
    {
        "name": "Montana",
        "capital": "Helena",
        "population": "1132812",
        "flower": "Bitterroot",
    },
    {
        "name": "Nebraska",
        "capital": "Licoln",
        "population": "1978379",
        "flower": "Goldenrod",
    },
    {
        "name": "Nevada",
        "capital": "Carson City",
        "population": "3194176",
        "flower": "Sagebush",
    },
    {
        "name": "New Hampshire",
        "capital": "Concord",
        "population": "1402054",
        "flower": "Purple Lilac",
    },
    {
        "name": "New Jersey",
        "capital": "Trenton",
        "population": "9290841",
        "flower": "Violet",
    },
    {
        "name": "New Mexico",
        "capital": "Santa Fe",
        "population": "2114371",
        "flower": "Yucca Flower",
    },
    {
        "name": "New York",
        "capital": "Albany",
        "population": "19571216",
        "flower": "Rose",
    },
    {
        "name": "North Carolina",
        "capital": "Raleigh",
        "population": "10835491",
        "flower": "Flowering Dogwood",
    },
    {
        "name": "North Dakota",
        "capital": "Bismark",
        "population": "783926",
        "flower": "Wild Prairie Rose",
    },
    {
        "name": "Ohio",
        "capital": "Columbus",
        "population": "11785935",
        "flower": "Red Carnation",
    },
    {
        "name": "Oklahoma",
        "capital": "Oklahoma City",
        "population": "4053824",
        "flower": "Oklahoma Rose",
    },
    {
        "name": "Oregon",
        "capital": "Salem",
        "population": "4233358",
        "flower": "Oregon Grape",
    },
    {
        "name": "Pennsylvania",
        "capital": "Harrisburg",
        "population": "12961683",
        "flower": "Mountain Laurel",
    },
    {
        "name": "Rhode Island",
        "capital": "Providence",
        "population": "1095962",
        "flower": "Violet",
    },
    {
        "name": "South Carolina",
        "capital": "columbia",
        "population": "5373555",
        "flower": "Yellow Jessamine",
    },
    {
        "name": "South Dakota",
        "capital": "Pierre",
        "population": "919318",
        "flower": "Pasque",
    },
    {
        "name": "Tennessee",
        "capital": "Nashville",
        "population": "7126489",
        "flower": "Iris",
    },
    {
        "name": "Texas",
        "capital": "Austin",
        "population": "30503301",
        "flower": "Bluebonnets",
    },
    {
        "name": "Utah",
        "capital": "Salt Lake City",
        "population": "3417734",
        "flower": "Sego Lily",
    },
    {
        "name": "Vermont",
        "capital": "Montpelier",
        "population": "647464",
        "flower": "Red Clover",
    },
    {
        "name": "Virginia",
        "capital": "Richmond",
        "population": "8715698",
        "flower": "American Dogwood",
    },
    {
        "name": "Washington",
        "capital": "Olympia",
        "population": "7812880",
        "flower": "Rhododendron",
    },
    {
        "name": "West Virginia",
        "capital": "Charleston",
        "population": "1770071",
        "flower": "Rhododendron",
    },
    {
        "name": "Wisconsin",
        "capital": "Madison",
        "population": "5910955",
        "flower": "Wood Violet",
    },
    {
        "name": "Wyoming",
        "capital": "Cheyenne",
        "population": "584057",
        "flower": "Indian Paintbrush",
    },
]


# function to for putting states in alphabetical order
def state_order():
    """Display all states in alphabetical order"""
    print("the list in alphabetical order is: ")
    for state in sorted(state_list, key=lambda x: x["name"]):
        print(f"{state['name']}: Capital: {state['capital']}", end=" ")
        print(f"Population: {state['population']}, Flower: {state['flower']}")
        print(" ")
    print(
        "***************************************************************************************"
    )


# function to searcn for a specific state
def search_state():
    """search for a specific state and give details about that state"""
    state_input = input("what state are you looking for information about?: ")
    image_file = f"{state_input.lower()}_flower.jpg"
    image_path = os.path.join(SUBDIRECTORY_PATH, image_file)
    if os.path.isfile(image_path):
        image = plt.imread(image_path)
        plt.figure(figsize=(8, 6))
        plt.imshow(image)
        plt.axis("off")
        plt.show()
    else:
        print(f"Sorry, that image for {state_input} was not found.")


# function to provide a bar graph
def state_graph():
    """great a graph based on the top 5 states populations"""
    for data in state_list:
        data["population"] = int(data["population"])
    sorted_states = sorted(state_list, key=lambda x: x["population"], reverse=True)
    top_states = sorted_states[:5]

    state_names = [data["name"] for data in top_states]
    populations = [data["population"] for data in top_states]

    plt.figure(figsize=(10, 6))
    plt.bar(state_names, populations)
    plt.title("top 5 most Populated States")
    plt.xlabel("state")
    plt.ylabel("Population")
    plt.xticks(rotation=45, ha="right")
    plt.show()


# function to update the overall state population


def state_update():
    """update a states overall population"""
    for state in state_list:
        state["population"] = int(state["population"])
    state_to_update = input("Enter the state name: ")

    for state in state_list:
        if state["name"].lower() == state_to_update.lower():
            update_population = int(
                input("Enter the new population for", state_to_update, ": ")
            )
            state["population"] = update_population
            print(
                "Population for", state_to_update, " update to", update_population, "."
            )
            continue
        else:
            print("sorry, ", state_to_update, "is not on the list of states")

    # initial prompt and introduction to user interface
    print("Welcome and thank you for using my program")


while True:
    print("Please choose a number from the following menu")
    print("**************************************************************************")
    print("to Display all U.S. States in Alphabetical order along with", end=" ")
    print("the Capital, State Population, and Flower type: 1")
    print("To Search for a specific state and display the appropriate", end=" ")
    print("Capital name, State Population, and Flower type: 2")
    print("To provide a bar graph of the top 5 populated States showing", end=" ")
    print("thier overall population type: 3")
    print("To update the overall state population for a specific state type: 4")
    print("To exit the program type: 5")

    answer = input("Please enter a number choice from 1 to 5: ")

    if answer == "5":
        print("Thank you for using my program!")
        sys.exit()
    elif answer.isdigit() and 1 <= int(answer) <= 4:
        if answer == "1":
            state_order()
        elif answer == "2":
            search_state()
        elif answer == "3":
            state_graph()
        elif answer == "4":
            state_update()
    else:
        print("Invalid input. Please try again")
