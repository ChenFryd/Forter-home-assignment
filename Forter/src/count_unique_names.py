from nicknames import NickNamer
from nltk import edit_distance

MAX_TYPOS = 1 #maximum amount of typod allowed, counted witn edit_distance
nn = NickNamer()

def change_max_typos(new_max_typos):
    """
    changes the maximum amount of typos allowed
    :param new_max_typos: the new maximum amount of typos allowed
    """
    global MAX_TYPOS
    MAX_TYPOS = new_max_typos
def get_max_typos():
    return MAX_TYPOS
def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard):
    """
    returns the amount of unique names
    :param billFirstName: the first name on the billing address, can contain middle names
    :param billLastName:  the last name on the billing address
    :param shipFirstName:  the first name on the shipping address, can contain middle names
    :param shipLastName:  the last name on the shipping address
    :param billNameOnCard:  the name on the card, can be reversed?
    :return: the amount of unique names
    """
    #first we need parse all the names to be with the same format
    names = [parseName(billFirstName +" "+ billLastName), parseName(shipFirstName +" "+shipLastName), parseName(billNameOnCard)]

    #next we need to compare all the names to see if they are unique
    amount_of_unique_names = count_names(names)
    if amount_of_unique_names == 1:
        return 1

    #if the names are not unique we need to check if the bill name on card is reversed
    names[2]["first_name"], names[2]["last_name"] = names[2]["last_name"], names[2]["first_name"]
    amount_of_unique_names_reversed = count_names(names)

    return min(amount_of_unique_names, amount_of_unique_names_reversed)



def count_names(names):
    """
    :param names: list of dict of names with length of 3, the keys are first_name, middle_name, last_name
    :return the amount of unique names in the names dictionary
    """
    unique_names = set()
    for i in range(3):
        for j in range(i+1, 3):
            if check_is_different_person(names[i], names[j]):
                unique_names.add(frozenset(names[i].items()))
                unique_names.add(frozenset(names[j].items()))
    if len(unique_names) == 0: #if there is not unique names on the set, it means there is only one person
        return 1
    return len(unique_names)



def check_is_different_person(name1, name2):
    """
    checks if the two names are different people
    :param name1: name of the first person
    :param name2: name of the second person
    :return: True if the names are different people, False if the names are the same person
    """
    if name1 == name2:
        return False
    edit_distance_total = check_two_first_names(name1["first_name"], name2["first_name"])
    if edit_distance_total > MAX_TYPOS:
        return True
    edit_distance_total += edit_distance_two_names(name1["middle_name"], name2["middle_name"])
    if edit_distance_total > MAX_TYPOS:
        return True
    edit_distance_total += edit_distance_two_names(name1["last_name"], name2["last_name"])
    if edit_distance_total > MAX_TYPOS:
        return True
    return False

def edit_distance_two_names(name1, name2):
    """
    returns the edit distance between two names, used here in middle names and last names
    :param name1:
    :param name2:
    :return:
    """
    if name1 == name2: #if the names are the same we just return 0
        return 0
    if not name1 or not name2: #if we compare middle names and one of them is empty
        return 0
    return edit_distance(name1, name2)
def check_two_first_names(name1, name2):
    """
    checks if the two first names are the same, checks the cannonical (formal name) of the nicknames too
    :param name1: name of the first person
    :param name2: name of the second person
    :return: True if the first names are the same, False if the first names are different
    """
    if name1 == name2:
        return 0
    min_edit_distance = float("inf")
    possible_names_1 = {name1}.union(nn.canonicals_of(name1))
    possible_names_2 = {name2}.union(nn.canonicals_of(name2))
    for nick_name1 in possible_names_1:
        for nick_name2 in possible_names_2:
            edit_dif = edit_distance(nick_name1, nick_name2)
            if edit_dif == 0:
                return 0
            if edit_dif < min_edit_distance:
                min_edit_distance = edit_dif
    return min_edit_distance

def parseName(name):
    if not name:
        return None
    name = name.lower().split(" ")
    if len(name) < 2:
        raise Exception("Name must have at least two parts")
    first_name = name.pop(0)
    if not first_name:
        raise Exception("First name must not be empty")

    last_name = name.pop(-1)
    if not last_name:
        raise Exception("last name must not be empty")
    middle_name = " ".join(name) if name else ""
    return {"first_name": first_name, "middle_name": middle_name, "last_name": last_name}
