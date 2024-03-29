from stimulus import Stimulus

if __name__=="__main__":

	#C1
	#Examples
	folder = "c1"
	example_stimuli = [Stimulus(.10,.15,"g","r","Not pelty"),
					Stimulus(.02,.1,"r","g","Not pelty"),
					Stimulus(.1,.30,"g","r","Pelty"),
					Stimulus(.1,.4,"g","r","Pelty")]

	test_stimuli = [Stimulus(.1,.45,"g","r"),
				Stimulus(.10,.2,"g","r")]

	for stimulus in example_stimuli:
		stimulus.show(save=True,folder=folder)

	for stimulus in test_stimuli:
		stimulus.show(plot_title="Is this pelty?",save=True,folder=folder)

	#C2
	#Examples
	folder = "c2"
	example_stimuli = [Stimulus(.02,.10,"r","g","Not pelty"),
					Stimulus(.08,.10,"r","g","Not pelty"),
					Stimulus(.10,.30,"g","r","Pelty"),
					Stimulus(.10,.4,"g","r","Pelty")]

	test_stimuli = [Stimulus(.1,.45,"g","r"),
					Stimulus(.10,.2,"g","r")]

	for stimulus in example_stimuli:
		stimulus.show(save=True,folder=folder)

	for stimulus in test_stimuli:
		stimulus.show(plot_title="Is this pelty?",save=True,folder=folder)


	#C3
	#Examples
	folder = "c3"
	example_stimuli = [Stimulus(.02,.2,"r","g","Not pelty"),
					Stimulus(.18,.2,"g","r","Not pelty"),
					Stimulus(.10,.30,"g","r","Pelty"),
					Stimulus(.10,.4,"g","r","Pelty")]

	test_stimuli = [Stimulus(.1,.45,"g","r"),
					Stimulus(.10,.2,"g","r")]

	for stimulus in example_stimuli:
		stimulus.show(save=True,folder=folder)

	for stimulus in test_stimuli:
		stimulus.show(plot_title="Is this pelty?",save=True,folder=folder)


"""
	# For Quiz 1
	# Test Examples
	folder = "Q1"
	#will they hypothesize on specific colors or radius distance?
	stimulus1 = Stimulus(.05,.35,"y","b","Not pelty")
	stimulus2 = Stimulus(.20,.25,"b","g","Pelty")
	stimulus1.show(save=True,folder=folder)
	stimulus2.show(save=True,folder=folder)

	test_stimuli = [Stimulus(.05,.35,"b","g"),
				Stimulus(.20,.25,"y","b"),
				Stimulus(.10,.20,"r","r"),
				Stimulus(.15,.30,"b","b")]

	for stimulus in test_stimuli:
		stimulus.show("Is this pelty?",save=True,folder=folder)


	# For Quiz 2
	# Test Examples
	folder = "Q2"
	#will they pick the equal colors or the radius distance?
	stimulus1 = Stimulus(.1,.3,"r","r","Pelty")
	stimulus1.show(save=True,folder=folder)

	test_stimuli = [Stimulus(.1,.3,"b","b"),
				Stimulus(.05,.35,"r","r"),
				Stimulus(.1,.3,"g","y"),
				Stimulus(.08,.32,"r","b")]

	for stimulus in test_stimuli:
		stimulus.show("Is this pelty?",save=True,folder=folder)


	# For Quiz 3
	# Test Examples
	folder = "Q3"
	#possibility of compound hypothesis since s1 and s2 so different
	stimulus1 = Stimulus(.05,.35,"y","y","Pelty")
	stimulus2 = Stimulus(.20,.25,"b","g","Pelty")
	stimulus3 = Stimulus(.15,.35,"r","k","Not pelty")
	stimulus1.show(save=True,folder=folder)
	stimulus2.show(save=True,folder=folder)
	stimulus3.show(save=True,folder=folder)

	test_stimuli = [Stimulus(.15,.30,"b","g"),
				Stimulus(.18,.22,"y","b"),
				Stimulus(.10,.20,"r","r"),
				Stimulus(.08,.35,"b","b")]

	for stimulus in test_stimuli:
		stimulus.show("Is this pelty?",save=True,folder=folder)
"""


