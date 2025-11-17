from tqdm import tqdm
import numpy as np

class Player(object):
    def __init__(self, name=None, travel_status=None):
        self.name = name
        self.travel_status = travel_status
        self.focus = 10
        self.fun = 0
        self.knowledge = 0

        # check for vips
        if self.name.lower() == "manisha":
            print("Hello Councilwoman Caleb...")
        elif self.name.lower() == "tim":
            print("I've always liked you Tim...")

    # methods

    # stats modifiers
    def mod_focus(self, num):
        self.focus += num

    def mod_fun(self, num):
        self.fun += num

    def mod_knowledge(self, num):
        self.knowledge += num

    def check_status(self):
        max_fun = 20
        max_focus = 20
        max_knowledge = 25

        self.fun = np.max([0, self.fun]) 
        self.focus = np.max([0, self.focus])
        self.knowledge = np.max([0, self.knowledge])

        (tqdm(range(max_fun), desc="Fun:      ",
            bar_format='{desc:<12}{percentage:3.0f}%|{bar:10}|{n_fmt}/{total_fmt}{bar:-10b}')).update(self.fun)
        (tqdm(range(max_focus), desc="Focus:    ",
            bar_format='{desc:<12}{percentage:3.0f}%|{bar:10}|{n_fmt}/{total_fmt}{bar:-10b}')).update(self.focus)
        (tqdm(range(max_knowledge), desc="Knowledge:",
            bar_format='{desc:<12}{percentage:3.0f}%|{bar:10}|{n_fmt}/{total_fmt}{bar:-10b}')).update(self.knowledge)
