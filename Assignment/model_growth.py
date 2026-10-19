# Assignment 5 - Part 1
import sys
import numpy as np


def main():
    # Read the dataset supplied on the command line.
    filename = sys.argv[1]
    experiment_data = np.loadtxt(filename, delimiter=',')

    # Start, stop, and step for candidate growth rates.
    rate_params = sys.argv[2:5]
    range_rate = np.arange(float(rate_params[0]), float(rate_params[1]), float(rate_params[2]))

    def squared_error(prediction, data):
        residual = prediction - data
        mse = (residual**2).mean()
        return mse

    mse = []
    N0 = experiment_data[0]
    t = np.linspace(0, 10, len(experiment_data))
    for r in range_rate:
        prediction = N0 * np.exp(r * t)
        mse.append(squared_error(prediction, experiment_data))

    best_fit = range_rate[np.argmin(mse)]
    print('We predict the rate of growth of this bacterial population to be', best_fit)


if __name__ == '__main__':
    main()


# Assignment 5 - Part 2
# question a
# git add Assignment/dummy_story.txt
# question b
# git commit -m "Add a sentence to dummy_story"
# question c
# git push origin HEAD
