"""Print out all the melons in our inventory."""


from melons import melons


def add_new_characteristics(*argv):
    """"Adds new characteristics to track for each melon. 

    Set the default value of each characteristic to None.
    """
    for melon in melons:
        melon_info = melons[melon]

        for arg in argv:
            melon_info[arg] = melon_info.get(arg, None)


def print_melon_report():
    """Print each melon and its characteristics."""
    for melon in melons:
        print melon.upper()

        melon_info = melons[melon]
        for characteristic in melon_info:
            value = melon_info[characteristic]
            print "{}: {}".format(characteristic.capitalize(), value)

        print


add_new_characteristics('flesh color', 'rind color', 'average weight')

print_melon_report()