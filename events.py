from player import Player
import pandas as pd
import hashlib

anyevent_df = pd.read_csv('any_whatever.csv')



def timify(text):
    words = text.split()
    result = []
    
    for word in words:
        hash_val = int(hashlib.md5(word.encode()).hexdigest(), 16)
        if len(word) <= 3 or hash_val % 2 == 0:
            tim_word = "Tim"
        else:
            tim_word = "Timmy"
        if word[0].isupper():
            tim_word = tim_word.capitalize()
        if word.isupper():
            tim_word = tim_word.upper()
        if word and not word[-1].isalnum():
            tim_word += word[-1]
        result.append(tim_word)
    
    return " ".join(result)

print(timify("That's one small step for a man, a giant leap for mankind."))


class RandomEvent:
    def __init__(self, Player):
        # random event generation will occur
        # pick a random event from the list
        rand_event = anyevent_df.sample()
        self.prompt = rand_event['prompt'].iloc[0]
        self.mod_foc = rand_event['focus'].iloc[0]
        self.mod_fun = rand_event['fun'].iloc[0]
        self.mod_know = rand_event['knowledge'].iloc[0]


        # modify the player states
        Player.mod_fun(self.mod_fun)
        Player.mod_focus(self.mod_foc)
        Player.mod_knowledge(self.mod_know)

        # print to user
        if Player.name.lower() == "tim":
            self.prompt = timify(self.prompt)
        print(self)

    def __repr__(self):
        return "Random Event! \n {} You get {} Fun, {} Focus, {} Knowledge".format(self.prompt, self.mod_fun, self.mod_foc, self.mod_know)
