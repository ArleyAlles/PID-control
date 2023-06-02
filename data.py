import numpy as np

class Data():
    """
    Experimental points of process
    """
    y = np.array([0., 0.03264843, 0.06396447, 0.09400248, 0.12281462,
                  0.15045092, 0.17695937, 0.202386, 0.22677495, 0.25016858,
                  0.2726075, 0.29413067, 0.31477547, 0.33457775, 0.35357188,
                  0.37179086, 0.3892663, 0.40602857, 0.42210676, 0.43752879,
                  0.45232143, 0.46651038, 0.48012028, 0.49317474, 0.50569645,
                  0.51770713, 0.52922766, 0.54027803, 0.55087742, 0.56104425,
                  0.57079616, 0.5801501, 0.58912229, 0.59772832, 0.60598314,
                  0.61390107, 0.62149587, 0.62878072, 0.63576827, 0.64247066,
                  0.64889952, 0.65506601, 0.66098085, 0.66665429, 0.6720962,
                  0.67731603, 0.68232283, 0.6871253, 0.69173177, 0.69615026,
                  0.70038842, 0.70445363, 0.70835292, 0.71209309, 0.71568062,
                  0.71912174, 0.72242243, 0.72558841, 0.72862519, 0.73153803,
                  0.734332, 0.73701195, 0.73958252, 0.74204819, 0.74441324,
                  0.74668176, 0.74885771, 0.75094486, 0.75294682, 0.75486709,
                  0.75670899, 0.75847572, 0.76017035, 0.76179582, 0.76335495,
                  0.76485045, 0.76628493, 0.76766086, 0.76898063, 0.77024655])
    np.random.seed(49)
    noise = 0.01*np.random.normal(size=len(y)) #noise

    def __init__(self):
        pass

    @classmethod
    def output(cls, y=y, noise=noise, hasnoise=False):
        """
        Output dataset with possibility to add noise on the data
        :param y(array): output data without noise
        :param noise(array): noise with normal distribution
        :param hasnoise(bool): Opitional. If want to add noise to the dataset
        :return: output data with or without noise
        """
        if hasnoise:
            return y+noise
        return y

    @classmethod
    def time(cls):
        """
        Experimental time of process
        :return: time of process
        """
        return np.arange(0,8,0.1)
