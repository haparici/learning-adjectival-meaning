import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Stimulus:
    def __init__(self, r1,r2,c1,c2,pelty):
        self.r1 = r1
        self.r2 = r2
        assert self.r1 <= 0.5, "Radii must be less than 0.5 to fit"
        assert self.r2 <= 0.5, "Radii must be less than 0.5 to fit"
        self.c1 = c1
        self.c2 = c2
        self.pelty = pelty ##TODO: Make this a String var instead

    def show(self,save=False):
        title = "Pelty" if self.pelty else "Not Pelty" 
        inner_circle = plt.Circle((0.5,0.5),self.r1,color=self.c1,fill=False)
        inner_circle.set_label("Inner Circle")
        outer_circle = plt.Circle((0.5,0.5),self.r2,color=self.c2,fill=False)
        outer_circle.set_label("Outer Circle")

        fig, ax = plt.subplots()
        ax.add_artist(inner_circle)
        ax.add_artist(outer_circle)
        fig.suptitle(title)
        plt.legend((inner_circle,outer_circle),("Radius = "+str(self.r1),"Radius = "+str(self.r2)))
        if save:
            plt.savefig("imgs/stimulus_"+str(self.r1)+"_"+str(self.r2)+".png")
        plt.show()


if __name__ == "__main__":
    testStimulus = Stimulus(.2,.4,"r","b",pelty=True)
    testStimulus.show(save=True)
    testStimulus2 = Stimulus(.1,.35,"g","b",pelty=False)
    testStimulus2.show(save=True)