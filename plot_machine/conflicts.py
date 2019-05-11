import random


class Conflict(object):
    def __init__(self):
        self.conflict = ""
        self.grandScope = ""
        self.grandScopes = ["Love & Courtship", "Married Life", "Enterprise"]
        self.conflicts = {"Love & Courtship": ["Love's beginnings",
                                               "Love's misadventures",
                                               "The Marriage Proposal",
                                               "Love's rejection",
                                               "Marriage"],
                          "Married Life": ["Divorce",
                                           "Affair"],
                          "Enterprise": ["Misfortune",
                                         "Mistaken Judgement",
                                         "Helpfulness",
                                         "Deliverance",
                                         "Idealism",
                                         "Obligation",
                                         "Necessity",
                                         "Chance",
                                         "Personal Limitations",
                                         "Simulation",
                                         "Craftiness",
                                         "Transgression",
                                         "Revenge"]
                          }

    def wild_combination(self):
        i = random.randrange(len(self.grandScopes))
        gs = self.grandScopes[i]
        j = random.randrange(len(self.conflicts[gs]))
        self.grandScope = gs
        self.conflict = self.conflicts[gs][j]
        return self

    def print(self):
        print(self)

    def __str__(self):
        return self.grandScope + "; " + self.conflict

if __name__ == "__main__":
    c = Conflict()
    c.wild_combination()
    c.print()
