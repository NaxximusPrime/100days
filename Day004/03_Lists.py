states_of_america = ["Delaware", "Pennsylvania"]

# print unchanged list
print(states_of_america)

# change an item
states_of_america[1] = "Pencilvania!"

# add a single item to the end
states_of_america.append("Honululu")

# extend the list by multiple items
states_of_america.extend(["Ullumullu", "Jack the Ripper Land"])

# last item output
num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

# print changed list
print(states_of_america)
