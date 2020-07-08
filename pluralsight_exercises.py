# Group files by owner from a files dictionary
def group_by_owners(files):
    my_set = set(files.values())

    # Initialize dictionary keys
    my_dict = dict.fromkeys(my_set)

    # Initialize dictionary values as empty lists
    for owner in my_dict.keys():
        my_dict[owner] = []

    # Fill dictionary
    for file, owner in files.items():
        my_dict[owner].append(file)
    return my_dict


# Icecream machine able to create combinations of toppings and ingredients
class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings
        self.combinations = []

    def scoops(self):
        if (len(self.ingredients) <= 0) or (len(self.toppings) <= 0):
            # Do nothing
            self.combinations = []
        else:
            for ingredient in self.ingredients:
                for topping in self.toppings:
                    self.combinations.append([ingredient, topping])
        return self.combinations
