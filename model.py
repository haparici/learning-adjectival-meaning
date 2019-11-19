import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.distributions.constraints as constraints

import pyro
import pyro.infer
import pyro.optim
import pyro.distributions as dist
from a import Stimulus

def model(data):
    def measure(datum):
        return rule1(datum)

    def rule1(datum):
        return 1 if (datum.get_r1() - 0.17) * (polarity*2-1) > 0 else 0

    def compute(datum):
        # p = torch.tensor([0.5])
        # depth = pyro.sample("x_{}".format(depth), dist.Bernoulli(p))
        test = measure(datum)
        return test
        # if depth[0] == 1:
        #     return test
        # else:
        #     return compute(datum) and test

    polarity = pyro.sample("polarity", dist.Categorical(torch.tensor([0.5,0.5])))

    for i in range(len(data)):
        res = compute(data[i])
        pyro.sample("obs_{}".format(i), dist.Categorical(torch.tensor([1 - res, res],dtype = torch.float32)), obs=torch.tensor(data[i].get_pelty()))

def guide(data):
    polarity_param = pyro.param("polarity_param",torch.tensor(0.7))
    pyro.sample("polarity",dist.Categorical(torch.tensor([1 - polarity_param.item(), polarity_param.item()],dtype = torch.float32)))


if __name__ == "__main__":
    pyro.clear_param_store()
    data = []
    data.append(Stimulus(0.1,0.2,'b','g',"pelty"))
    data.append(Stimulus(0.1,0.3,'b','g',"pelty"))
    data.append(Stimulus(0.1,0.4,'b','g',"pelty"))
    data.append(Stimulus(0.2,0.3,'b','g',"not pelty"))
    data.append(Stimulus(0.3,0.4,'b','g',"not pelty"))

    # setup the inference algorithm
    svi = pyro.infer.SVI(model, guide, optim=pyro.optim.SGD({"lr": 0.001, "momentum":0.1}),
    loss=pyro.infer.Trace_ELBO())

    n_steps = 5000
    # do gradient steps
    for step in range(n_steps):
        svi.step(data)
        # b.append(pyro.param("polarity_param").item())

    print('polarity_1 = ', pyro.param("polarity_param").item())
