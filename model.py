import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.distributions.constraints as constraints

import pyro
import pyro.infer
import pyro.optim
import pyro.distributions as dist
from pyro.infer import MCMC, NUTS

from num_to_img import Stimulus

def model(data):
    def grad(datum):
        '''
        computes the rule if the adj is gradable
        '''
        return rule1(datum)
        # return [rule1,rule2,rule3][i](datum)

    def rule1(datum):
        return 1 if (datum.get_r1() - threshold) * (polarity*2-1) > 0 else 0
    #
    # def rule2(datum):
    #     return 1 if (datum.get_r1() - threashold) * (polarity*2-1) > 0 else 0

    def compute(datum):
        test = grad(datum)
        if torch.bernoulli(torch.tensor([0.5])) == 1:
            return test and compute(datum)
        else:
            return test

    #TODO: figure out why this polarity sample is not working
    #set polarity to 1, the program infers the threashold
    polarity = 1 #pyro.sample("polarity", dist.Bernoulli(torch.tensor([0.5])))
    #print(polarity)


    threshold = pyro.sample("threshold", dist.Uniform(0.3,2.0))

    for i in range(len(data)):
        res = torch.tensor(compute(data[i]),dtype = torch.float32)
        pyro.sample("obs_{}".format(i), dist.Bernoulli(res), obs=torch.tensor(data[i].get_pelty(),dtype = torch.float32))


if __name__ == "__main__":
    pyro.clear_param_store()
    data = []
    data.append(Stimulus(0.1,0.2,'b','g',"pelty"))
    data.append(Stimulus(0.1,0.3,'b','g',"pelty"))
    data.append(Stimulus(0.1,0.4,'b','g',"pelty"))
    data.append(Stimulus(0.2,0.3,'b','g',"not pelty"))
    data.append(Stimulus(0.3,0.4,'b','g',"not pelty"))

    nuts_kernel = NUTS(model)
    mcmc = MCMC(nuts_kernel,
                num_samples=1000,
                num_chains=1)
    mcmc.run(data)
    mcmc.summary(prob=0.95)
