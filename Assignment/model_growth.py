#Part 1

import numpy as np
import sys

def main():
    # read in the data from the .csv passed to our script
    filename = sys.argv[1] #(b, 0.5 marks)
    experiment_data = np.loadtxt(filename,delimiter = ',') #(c, 0.5 marks)

    # store the command-line arguments that represent the start, stop, and step size in the variable rate_params
    rate_params = [sys.argv[2], sys.argv[3], sys.argv[4]] #(d, 0.5 marks)
    # note: since the parameters that are read by sys.argv are strings, we have to convert them to floats using float(a_string)
    range_rate = np.arange(float(rate_params[0]), float(rate_params[1]), float(rate_params[2]))

    # define a function that calculates mean squared error
    def squared_error(prediction, data):
        residual = prediction - data
        mse = (residual**2).mean()
        return mse

    # try the parameters and choose the one with the smallest squared error
    mse = []
    # note two modifications below: we are taking the N0 and the time vector from data
    N0 = experiment_data[0]
    t = np.linspace(0, 10, len(experiment_data))
    for r in range_rate:
        prediction = N0*np.exp(r*t)
        mse.append(squared_error(prediction, experiment_data))

    best_fit = range_rate[np.argmin(mse)]
    print('We predict the rate of growth of this bacterial population to be', best_fit)

# write the code necessary to make sure the main() function is called when we run the script from command line (e, 1 mark)
if __name__ == '__main__':
    main()
