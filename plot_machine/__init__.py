from plot_machine.conflicts import Conflict
from plot_machine.characters import Characters
from plot_machine.masterplot import Masterplot
import re


def capitalize(str_in):
    return re.sub(r"(\A\w)|" +  # start of string
                  "(?<!\.\w)([\.?!] )\w|" +  # after a ?/!/. and a space, but not after an acronym
                  "\w(?:\.\w)|" +  # start/middle of acronym
                  "(?<=\w\.)\w",  # end of acronym
                  lambda x: x.group().upper(),
                  str_in)


class Plotto(object):
    def __init__(self):
        self.conflicts = Conflict()
        self.characters = Characters()
        self.masterplot = Masterplot()

    def wild_combination(self):
        self.conflicts.wild_combination()
        self.characters.wild_combination()
        self.masterplot.wild_combination()
        return self

    @property
    def cast(self):
        return self.characters.cast

    def print(self):
        self.masterplot.print()
        print("\nThe Conflict:\n")
        self.conflicts.print()
        print("")
        self.characters.print()


if __name__ == "__main__":
    p = Plotto().wild_combination()
    print(p.masterplot)
    print(p.conflicts)
    for character in p.cast:
        print(character.name, character.gender, character.role)
