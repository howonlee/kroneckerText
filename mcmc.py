"""
Metropolis-Hastings for MCMC
"""
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import operator

def lnprob(x):
    return -0.5 * np.sum(x ** 2)

def run_mcmc(ndim, lnprob, p0, num_steps=1000):
    curr_probs = np.array(p0)
    curr_lnprob = lnprob(curr_probs)
    for i in xrange(num_steps):
        curr_q = npr.multivariate_normal(curr_probs, np.identity(5)) #covariance is just default stuff
        new_lnprob = lnprob(curr_q)
        diff = new_lnprob - curr_lnprob
        if diff < 0:
            diff = np.exp(diff) - npr.rand()
        else:
            curr_probs = curr_q
            curr_lnprob = new_lnprob
        yield curr_probs, curr_lnprob

if __name__ == "__main__":
    p0 = npr.random(5)
    p = list(run_mcmc(5, lnprob, p0))
    ps = map(operator.itemgetter(0), p)
    ps = map(operator.itemgetter(0), ps)
    plt.plot(range(1000), ps)
    plt.show()
