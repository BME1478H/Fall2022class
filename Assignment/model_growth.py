**a) ....**
import numpy as np

def main():

    filename = **b)...**
    rate_params = **c)....**


    range_rate = np.arange(float(rate_params[0]),float(rate_params[1]),float(rate_params[2])) # note here we made a slight change: since the parameters that are read by sys library are strings, we have to convert them to floats.
    experiment_data = **d)...**

    # define a function that calcualates mean squared error
    def squared_error(prediction,data):
        residual = prediction - data
        mse = (residual**2).mean()          #or np.sum(residual**2)
        return mse

    # try the parameters and choose the one with the least squared error
    mse = []
    # note two modifications below: we are taking the N0 and the time vector from data
    N0 = experiment_data[0]
    t = np.linspace(0,10,len(experiment_data))
    for r in range_rate:
        prediction = N0*np.exp(r*t)
        mse.append(squared_error(prediction,experiment_data))

    best_fit = range_rate[np.argmin(mse)]
    print('We predict the rate of growth of this bacterial population to be',best_fit)

**e)...**
**d)...**
