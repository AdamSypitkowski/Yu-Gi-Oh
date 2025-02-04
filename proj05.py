########################################################################################################################
#
#   Project 5
#       Yu-Gi-Oh!
#           Imports a csv file of different Cards which gets converted to a list.
#           The list of cards can then be iterated 1 of 3 different ways
#               The cards are printed along with the Min, Max, and Med stats
#               A query is entered and that string is searched for inside one of the categories
#                   The data that equals the query is then added to a new list which gets
#                   printed and the Min, Max, and Med stats are calculated.
#               A deck of cards is entered in where the Card ID number is present. That card ID number is
#                   used to appended cards in the main list to a separate list in which the cards are
#                   printed and the Min, Max, Med are stats are calculated and printed.
#
########################################################################################################################


import csv, operator
from operator import itemgetter

# Strings
FILE_NOT_FOUND = "\nFile not Found. Please try again!"

DISPLAY_DATA_HEADER = f"{'Name':<50}{'Type':<30}{'Race':<20}{'Archetype':<40}{'TCGPlayer':<12}"

INVALID = "\nInvalid option. Please try again!"
FILE_PROMPT = "\nEnter cards file name: "
NUM_OF_CARDS = "\nThere are {} cards in the dataset."

QUERY = "\nEnter query: "
CATEGORY = "\nEnter category to search: "
CATEGORY_ERROR = "\nIncorrect category was selected!"
SEARCH_RESULTS = "\nSearch results"


DECKLIST_NAME = "\nEnter decklist filename: "
THANK_YOU = "\nThanks for your support in Yu-Gi-Oh! TCG"

MENU = "\nYu-Gi-Oh! Card Data Analysis" \
           "\n1) Check All Cards" \
           "\n2) Search Cards" \
           "\n3) View Decklist" \
           "\n4) Exit" \
           "\nEnter option: "

CATEGORIES = ["id", "name", "type", "desc", "race", "archetype", "card price"]

def open_file(prompt_str):
    '''
    Opens the designated file, and returns a file pointer of the opened file. If the file does not exist,
    The file not found statement is printed.
    '''

    try:
        fp = open(prompt_str, "r", encoding = "utf-8")
    except:
        print(FILE_NOT_FOUND)
    return fp

def read_card_data(fp):
    '''
    Takes a file pointer as input and returns an organized list of all cards in the file pointer.
    The file is sorted by the cost of the card.
    '''

    card_lst = []
    reader = csv.reader(fp)
    next(reader, None)

    for row in reader:
        name_str = row[1]
        final_name = name_str[:45]
        final_row = [row[0], final_name, row[2], row[3], row[4], row[5], float(row[6])]
        card_lst.append(tuple(final_row))

    sort_lst = sorted(card_lst, key=itemgetter(6,1))
    return sort_lst

def read_decklist(fp, card_data):
    '''
    Inputs the file pointer of the decklist and the total card data.
    The file pointer is read and a list is created out of each line
    of the file. The cards that are in the deck are computed using a loop
    the sorted loop is then returned.
    '''

    # Creation of both lists
    deck_lst = []
    file_lst = fp.read().split("\n")

    # Nested loops to check if the cards are equal
    for j in range(len(file_lst)):
        if file_lst[j].isnumeric():
            for i in range(len(card_data)):
                if file_lst[j] == (card_data[i])[0]:
                    # If the card data equals the file, it is appended to the deck_list
                    deck_lst.append(card_data[i])
                    break

    # Sorting the deck_list created
    sort_deck_lst = sorted(deck_lst, key=itemgetter(6,1))
    return sort_deck_lst

def search_cards(sort_lst, query, category_index):
    '''
    Searches for a user generated phrase inside the list of cards.
    If the phrase is found, the card is appended to a list to be printed
    '''

    print_lst = []

    for i in range(len(sort_lst)):
        item = (sort_lst[i])[category_index]
        value = item.find(query)

        if value != -1:
            print_lst.append(sort_lst[i])

    return print_lst

def compute_stats(card_data):
    '''
    Sorts cards based on their price. The minimum price, maximum, and median prices
    are all calculated, then the card_data list is looped in to determine if a card
    has one of the chosen price values
    '''

    # creation of lists to be used
    minimum_lst = []
    maximum_lst = []
    median_lst = []
    card_median_lst = []

    # To make a list of only card prices
    for i in range(len(card_data)):
        card_median_lst.append((card_data[i])[6])

    # Determining median value
    if len(card_median_lst) % 2 == 0:
        index = round((len(card_median_lst)) / 2)
    else:
        index = round((len(card_median_lst)-1) / 2)
    median_val = (card_median_lst[index])

    for i in range(len(card_data)):
        # Calculating the minimum value
        if card_data[i][6] == card_median_lst[0]:
            minimum_lst.append(card_data[i])

        # Calculating the maximum value
        if card_data[i][6] == card_median_lst[len(card_median_lst)-1]:
            maximum_lst.append(card_data[i])

        # Calculating the median value
        if card_data[i][6] == median_val:
            median_lst.append(card_data[i])

    return minimum_lst, minimum_lst[0][6], maximum_lst, maximum_lst[0][6], median_lst, median_val

def display_data(card_data):
    '''
    Prints each card in order to display Name,Type, Race, Archetype, and TCG Player
    '''

    print(DISPLAY_DATA_HEADER)
    total = 0

    for i in range(len(card_data)):
        print(f"{(card_data[i][1])[:50]:50}{(card_data[i][2])[:30]:30}{(card_data[i][4])[:20]:20}{(card_data[i][5])[:40]:40}{(card_data[i][6]):12.2f}")
        total += card_data[i][6]

    print(f"\n{'Totals':50}{'':30}{'':20}{'':40}{total:12,.2f}")
    return


def display_stats(min_cards, min_price, max_cards, max_price, med_cards, med_price):
    '''
    Prints the statistics of each card with the minimum, maximum, and median prices
    '''

    print(f"\nThe price of the least expensive card(s) is {min_price:.2f}")
    for i in range(len(min_cards)):
        print(f"\t{min_cards[i][1]}")

    print(f"\nThe price of the most expensive card(s) is {max_price:.2f}")
    for i in range(len(max_cards)):
        print(f"\t{max_cards[i][1]}")

    print(f"\nThe price of the median card(s) is {med_price:.2f}")
    for i in range(len(med_cards)):
        print(f"\t{med_cards[i][1]}")

    return

def main():
    # Reads File to determine if it is accessible
    good_file = False
    while good_file == False:
        file_input = input(FILE_PROMPT)
        try:
            fp = open_file(file_input)
            good_file = True

        except:
            continue

    card_lst = read_card_data(fp)
    fp.close()

    # This is just for fun so the loop runs
    input_code = 'EASTER EGG'

    while input_code != '4':
        input_code = input(MENU)

        # Action 1 as labled in the project header, where the list of cards is printed
        if input_code == '1':
            print(NUM_OF_CARDS.format(len(card_lst)))
            print_cards = card_lst[:50]
            display_data(print_cards)

            min_lst, min_val, max_lst, max_val, med_lst, med_val = compute_stats(card_lst)
            display_stats(min_lst, min_val, max_lst, max_val, med_lst, med_val)

        # Action 2 where the card list is sorted to contain a specific phrase
        elif input_code == '2':
            query = input(QUERY)
            in_category = False

            # Loop to determine which category to use to search for the phrase
            while in_category == False:
                category = (input(CATEGORY)).lower()
                for i in range(len(CATEGORIES)):
                    if category == CATEGORIES[i]:
                        category_index = i
                        in_category = True

                # Assures that the category actually exists
                if in_category == False:
                    print(CATEGORY_ERROR)

            # Printing display for the information gathered
            final_lst = search_cards(card_lst, query, category_index)
            print(SEARCH_RESULTS)

            if len(final_lst) == 0:
                print(f"\nThere are no cards with '{query}' in the '{category}' category.")
            else:
                print(f"\nThere are {len(final_lst)} cards with '{query}' in the '{category}' category.")

                display_data(final_lst)
                min_lst, min_val, max_lst, max_val, med_lst, med_val = compute_stats(final_lst)
                display_stats(min_lst, min_val, max_lst, max_val, med_lst, med_val)
d2ld
        # Input code for using a decklist. Prints out all information according to the deck
        elif input_code == '3':
            decklist = input(DECKLIST_NAME)
            fp = open(decklist, 'r')
            deck_lst = read_decklist(fp, card_lst)

            print(SEARCH_RESULTS)
            display_data(deck_lst)
            min_lst, min_val, max_lst, max_val, med_lst, med_val = compute_stats(deck_lst)
            display_stats(min_lst, min_val, max_lst, max_val, med_lst, med_val)

        # Break Statement
        elif input_code == '4':
            break

        # Catch-All clause which makes sure the command entered is valid.
        else:
            print(INVALID)

    print(THANK_YOU)

    return


if __name__ == "__main__":
    main()
