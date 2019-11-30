import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

"""Vector Specifications
    - Radii will be standardized between (0,0.5) (so the graph fits in a unit square)
    - There will be 8 color objects, designated by matplotlib's color options
    (link below). Each will be designated by a letter in 'bgrcmykw' 
    https://matplotlib.org/2.0.2/api/colors_api.html
    - Pelty will be a string that needs to be parsed to get a value [0,1]
    - The overall vector will look like [r1,r2,c1,c2,pelty]
"""
COLORS = 'bgrcmykw'

class Stimulus:
    def __init__(self, r1,r2,c1,c2,pelty=None):
        self.r1 = r1
        self.r2 = r2
        assert self.r1 <= 0.5, "Radii must be less than 0.5 to fit"
        assert self.r2 <= 0.5, "Radii must be less than 0.5 to fit"
        self.c1 = c1
        self.c2 = c2
        assert self.c1 in COLORS, "Not a valid color"
        assert self.c2 in COLORS, "Not a valid color"

        if pelty is not None:
            self.pelty_string = pelty[0].upper()+pelty[1:].lower()
            self.pelty = self.parse_pelty(self.pelty_string)
        else:
            self.pelty_string = ""
            self.pelty = None

    def get_r1(self):
        return self.r1

    def get_r2(self):
        return self.r2

    def get_c1(self):
        return self.c1

    def get_c2(self):
        return self.c2

    def get_pelty(self):
        if self.pelty is not None:
            return self.pelty

    def get_pelty_string(self):
        return self.pelty_string

    def parse_pelty(self,pelty_string):
        """Takes a string describing an object's peltyness and returns a numerical 
        value inferred."""

        if self.pelty_string.lower() == "pelty":
            return 1
        elif self.pelty_string.lower() == "not pelty":
            return 0
        else:
            return None

    def to_vector(self):
        #TODO: Should we be returning pelty_string or pelty value?
        return np.array([self.r1, self.r2, self.c1, self.c2, self.pelty_string])

    def __eq__(self,obj):
        return obj.r1 == self.r1 and obj.r2 == self.r2 and obj.c1 == self.c1 and obj.c2 == self.c2 and obj.pelty_string == self.pelty_string

    def __str__(self):
        return "%s stimulus with inner radius %.3f, outer radius %.3f, colors %s and %s." % (self.pelty_string, self.r1, self.r2, self.c1, self.c2)

    def show(self,plot_title=None,save=False,folder=None):
        """Displays the stimulus in a graph"""
        if plot_title:
            title=plot_title
        else:
            title = "Pelty" if self.pelty == 1 else "Not Pelty" if self.pelty == 0 else ""
        inner_circle = plt.Circle((0.5,0.5),self.r1,color=self.c1,fill=False)
        inner_circle.set_label("Inner Circle")
        outer_circle = plt.Circle((0.5,0.5),self.r2,color=self.c2,fill=False)
        outer_circle.set_label("Outer Circle")

        fig, ax = plt.subplots(figsize=(6,6))
        ax.add_artist(inner_circle)
        ax.add_artist(outer_circle)
        fig.suptitle(title)
        plt.legend((inner_circle,outer_circle),("Radius = "+str(self.r1),"Radius = "+str(self.r2)))
        if save:
            if folder:
                plt.savefig("imgs/"+folder+"/"+self.pelty_string+"_stimulus_"+str(self.r1)+"_"+str(self.r2)+"_"+self.c1+"_"+self.c2+".png")
            else:
                plt.savefig("imgs/"+self.pelty_string+"_stimulus_"+str(self.r1)+"_"+str(self.r2)+"_"+self.c1+"_"+self.c2+".png")
        else:
            plt.show()

def read_stimuli_from_file(filename):
    stimuli = []
    with open(filename) as fp:
        line = fp.readline() #skip first line
        line = fp.readline()
        while line and len(line) > 1:
            entries = line.strip("\n").split(",")
            assert len(entries) == 5, "Invalid number of arguments for a Stimulus"
            r1 = float(entries[0])
            r2 = float(entries[1])
            c1, c2, pelty = entries[2:]
            stimuli.append(Stimulus(r1,r2,c1,c2,pelty))
            line = fp.readline()

    return stimuli

def vector_to_stimulus(vector):
    assert len(vector) == 5, "Wrong number of arguments"
    r1,r2,c1,c2,pelty = vector
    assert type(r1) == int or type(r1) == float, "Radius must be an int or float"
    assert type(r2) == int or type(r2) == float, "Radius must be an int or float"
    assert c1 in COLORS, "Not a valid color"
    assert c2 in COLORS, "Not a valid color"
    return Stimulus(r1,r2,c1,c2,pelty)


if __name__ == "__main__":

    # some basic tests
    vector = [.2,.4,"r","b","Pelty"]
    stimulus = vector_to_stimulus(vector)
    assert stimulus.get_r1() == .2
    assert stimulus.get_r2() == .4
    assert stimulus.get_c1() == "r"
    assert stimulus.get_c2() == "b"
    assert stimulus.get_pelty_string() == "Pelty"

    stimulus2 = Stimulus(.1,.35,"g","b","Not pelty")
    vector2 = stimulus2.to_vector()
    assert np.array_equal(vector2, np.array([.1,.35,"g","b","Not pelty"]))

    stimuli = read_stimuli_from_file("stimuli_test.txt")
    assert stimuli[0] == stimulus
    assert stimuli[1] != stimulus

    #uncomment below to show graphs
    # stimulus.show()
    # stimulus2.show()

    print("All tests passed")

