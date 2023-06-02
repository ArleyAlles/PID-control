from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from data import Data

class CurveFit():
    """
    Obtaining parameters of 1ª order transfer function
    """
    def __init__(self):
        pass

    @staticmethod
    def func(time:list, K:float, T:float):
        """
        1ª order transfer function. K and T are the desired
        parameters
        :return: Calculated output --> (y(t))
        """
        return K*(1-np.exp(-time/T))

    @classmethod
    def fit_curve(cls, output:list, time:list):
        """
        :param output: output experimental dataset
        :param time: experimental time
        :return: parameters
        """
        param, _ = curve_fit(cls.func, time, output)
        return param

    @classmethod
    def graph(cls, output:list, time:list):
        """
        Plot generation
        :param output: output experimental dataset
        :param time: experimental time
        """
        param = cls.fit_curve(output, time)
        fig, ax = plt.subplots(1, 1)
        ax.plot(time, output, 'r')
        ax.plot(time, cls.func(time, *param))
        ax.set_xlabel("Time", fontsize=16)
        ax.set_ylabel("Output", fontsize=16)
        plt.show()


if __name__=='__main__':
    time = Data.time()
    output = Data.output(hasnoise=True)
    parametros = CurveFit.graph(output, time)
