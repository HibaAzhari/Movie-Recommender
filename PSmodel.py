# Production System model with "Rule" and "Condition" classes:

class ProductionSystem:
    def __init__(self, conditions):
        self.conditions = conditions # list of possible conditions
        self.rules = []
        self.firedRules = [] # list of fired Rules
        self.recommendation = ""

        # For Forward chaining
        self.WM = [] # list of active conditions
        # For Backward chaining
        self.movieData = []
    
    def reset(self):
        self.firedRules = []
        self.recommendation = ""
        self.WM = []
        self.movieData = []

    def setRules(self, rules):
        self.rules = rules
    
    # Fires condition by adding to WM
    def fire(self, condition):
        self.WM.append(condition)

    # Resets system
    def reset(self):
        self.WM = []
        self.firedRules = []
        self.movieData = []

    # Performs forward chaining (Recommends an item)
    def recommend(self):
        while(True):
            # Loop through all rules
            for rule in self.rules:
                # for each rule, if active and not fired
                if rule.active() and rule not in self.firedRules:
                    # fire
                    result = rule.fire()
                    # if a "final" condition was reached, return it
                    if result not in "":
                        self.recommendation = result
                        return
                    # else: keep repeating
    
    # Performs backward chaining (Gets movie info)
    def backward(self, movie):
        print("-- Rules fired in backward chaining --")
        # Loop through rules to find the movie
        for rule in self.rules:
            if movie in rule.resCond:
                for c in rule.reqCond:
                    # Add its descriptions to "movieData"
                    self.movieData.append(c)
                print(rule.desc)
                # Set the rule as "fired"
                self.firedRules.append(rule)
        # Loop through rules to find required conditions to result in movie conditions
        for c in self.movieData:
            # Check each rule in system
            for rule in self.rules:
                if rule not in self.firedRules:
                    # if found in resConds
                    if c in rule.resCond:
                        # Set rule as fired
                        self.firedRules.append(rule)
                        print(rule.desc)
                        # Add all requirements to "movieData"
                        for con in rule.reqCond:
                            self.movieData.insert(self.movieData.index(c),con)
        # remove mid-level conditions
        for r in self.rules:
            for c in self.movieData:
                if c in r.resCond:
                    self.movieData.remove(c)

        print()
        print("Input values to get: " + movie.desc)
        for d in self.movieData:
            print(d.desc)
        

    # Rule class
    # Represents an IF-THEN rule in the system            
    class Rule:
        def __init__(self, PS, reqCond, resCond, desc):
            self.PS = PS # Production system the rule belongs to
            self.reqCond = reqCond # list of required conditions
            self.resCond = resCond # list of resulting conditions
            self.desc = desc # string description of rule

        # Checks if reqConds are in WM
        def active(self):
            for cond in self.reqCond:
                if cond not in self.PS.WM:
                    return False
            return True

        # "Fires" the rule and returns the recommendation if final cond is found
        def fire(self):
            # Add rule to list of fired rules in PS
            self.PS.firedRules.append(self)
            print(self.desc)
            for cond in self.resCond:
                # Add all resConds to WM
                self.PS.WM.append(cond)
                # return cond description if it is final
                if cond.final:
                    return cond.desc
            return ""

# Condition class 
# A condition is any identifying feature of an item in the system (eg. movie name/genre)
class Condition:
    def __init__(self, desc, final):
        # String description of condition:
        self.desc = desc
        # Boolean of whether it is a final result (eg. movie to recommend)
        self.final = final