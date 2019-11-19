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
    def measure(data):
        # ix = pyro.sample("rule_choice_{}"".format(), dist.Categorical(probs=torch.ones(3) / 3))
        # return [rule1,rule2,rule3][ix](data)
        return rule1(data)

    def rule1(data):
        theta_1 = pyro.param("theta_1", torch.tensor(0.17),
                             constraint=constraints.positive)
        polarity_1 = pyro.param("polarity_1", torch.tensor(1.0))
        return (data.get_r1() - theta_1) * polarity_1 > 0

    def rule2(data):
        theta_1 = pyro.param("theta_1", torch.tensor(0.17),
                             constraint=constraints.positive)
        polarity_1 = pyro.param("polarity_1", torch.tensor(1.0))
        return (data.get_r1() - theta_1) * polarity_1 > 0

    def rule3(data):
        theta_1 = pyro.param("theta_1", torch.tensor(0.17),
                             constraint=constraints.positive)
        polarity_1 = pyro.param("polarity_1", torch.tensor(1.0))
        return (data.get_r1() - theta_1) * polarity_1> 0

    def compute(datum):
        p = torch.tensor([0.5])
        # depth = pyro.sample("x_{}".format(depth), dist.Bernoulli(p))
        test = measure(datum)
        # if depth[0] == 1:
        #     return test
        # else:
        #     return compute(datum) and test
    theta_1 = pyro.sample("theta_1",dist)
    polarity_1 = pyro.sample()
    for i in range(len(data)):
        res = compute(data[i])
        pyro.sample("obs_{}".format(i), dist.Categorical(touch.tensor([1- res, res])), obs=torch.tensor(data[i].get_pelty()))

def guide(data):
    pyro.sample("")


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
        a.append(pyro.param("theta_1").item())
        b.append(pyro.param("polarity_1").item())

    plt.plot(losses)
    plt.title("ELBO")
    plt.xlabel("step")
    plt.ylabel("loss");
    print('theta_1 = ',pyro.param("theta_1").item())
    print('polarity_1 = ', pyro.param("polarity_1").item())
