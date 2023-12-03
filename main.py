from copy import copy

class Dials:
    def __init__(self, purple, yellow, blue, orange):
        self.orange = orange
        self.purple = purple
        self.yellow = yellow
        self.blue = blue

    def copy(self):
        return Dials(self.purple, self.yellow, self.blue, self.orange)

    def reset(self):
        if self.orange > 9:
            self.orange = 0
        if self.blue > 9:
            self.blue = 0
        if self.yellow > 9:
            self.yellow = 0
        if self.purple > 9:
            self.purple = 0

    def turn_orange(self):
        self.orange += 1
        self.purple += 1
        self.reset()
    
    def turn_purple(self):
        self.purple += 1
        self.yellow += 1
        self.reset()

    def turn_yellow(self):
        self.yellow += 1
        self.blue += 1
        self.reset()
    
    def turn_blue(self):
        self.blue += 1
        self.orange += 1
        self.reset()

    def get_state(self):
        return (self.orange, self.purple, self.yellow, self.blue)

    def __str__(self):
        return f"O: {self.orange}, P: {self.purple}, Y: {self.yellow}, B: {self.blue}"


start_dials = Dials(yellow=8, orange=0, blue=7, purple=6)

solutions = {
    "1" : {
        "yellow" : 2,
        "orange" : 7,
        "blue" : 4,
        "purple" : 5
    },
    "2" : {
        "yellow" : 8,
        "orange" : 5,
        "blue" : 7,
        "purple" : 6
    },
    "3" : {
        "yellow" : 6,
        "orange" : 2,
        "blue" : 3,
        "purple" : 5
    }
}
solution = solutions[2]

def check_solution(d):
    #print(d)
    #print(solution)
    if d.blue != solution["blue"]: return False
    if d.yellow != solution["yellow"]: return False
    if d.orange != solution["orange"]: return False
    if d.purple != solution["purple"]: return False
    return True

all_states = []
all_actions = 0
def recurse(in_dials, actions=[]):
    global all_states
    global all_actions
    if check_solution(in_dials): return actions
    if in_dials.get_state() in all_states: 
        print("Duplicate state")
        return None
    if len(actions) > 500:
        print("Max actions") 
        return None

    all_states = all_states + [in_dials.get_state()]

    y = in_dials.copy()
    y.turn_yellow()

    all_actions += 1
    rv = recurse(y, actions=copy(actions + ["turn yellow"]))
    if rv is not None: return rv

    o = in_dials.copy()
    o.turn_orange()
    all_actions += 1
    rv = recurse(o, actions=copy(actions + ["turn orange"]))
    if rv is not None: return rv

    b = in_dials.copy()
    b.turn_blue()
    all_actions += 1
    rv = recurse(b, actions=copy(actions + ["turn blue"]))
    if rv is not None: return rv

    p = in_dials.copy()
    p.turn_purple()
    all_actions += 1
    rv = recurse(p, actions=copy(actions + ["turn purple"]))
    if rv is not None: return rv

    return None

print(recurse(start_dials))