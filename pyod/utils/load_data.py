'''
Utility functions for loading sample data and create pseudo data
'''
import os
import numpy as np
from scipy.io import loadmat


def generate_data(n_train=1000, n_test=500, contamination=0.1,
                  train_only=False):
    '''
    Utility function to generate synthesized data
    normal data is generated by a 2-d gaussian distribution
    outliers are generated by a 2-d uniform distribution

    :param train_only: generate train data only
    :param n_train: number of training points to generate
    :param n_test: number of test points to generate
    :param contamination: percentage of outliers
    :return: training data and test data (c_train and c_test are colors)
    '''
    n_outliers = int(n_train * contamination)
    n_inliers = int(n_train - n_outliers)

    n_outliers_test = int(n_test * contamination)
    n_inliers_test = int(n_test - n_outliers_test)

    offset = 2

    # generate inliers
    X1 = 0.3 * np.random.randn(n_inliers // 2, 2) - offset
    X2 = 0.3 * np.random.randn(n_inliers // 2, 2) + offset
    X_train = np.r_[X1, X2]

    # generate outliers
    X_train = np.r_[
        X_train, np.random.uniform(low=-6, high=6, size=(n_outliers, 2))]

    # generate target
    y_train = np.zeros([X_train.shape[0], 1])
    c_train = np.full([X_train.shape[0]], 'b', dtype=str)
    y_train[n_inliers:, ] = 1
    c_train[n_inliers:, ] = 'r'

    if train_only:
        return X_train, y_train, c_train

    # generate test data
    X1_test = 0.3 * np.random.randn(n_inliers_test // 2, 2) - offset
    X2_test = 0.3 * np.random.randn(n_inliers_test // 2, 2) + offset
    X_test = np.r_[X1_test, X2_test]

    # generate outliers
    X_test = np.r_[
        X_test, np.random.uniform(low=-8, high=8, size=(n_outliers_test, 2))]
    y_test = np.zeros([X_test.shape[0], 1])

    c_test = np.full([X_test.shape[0]], 'b', dtype=str)

    y_test[n_inliers_test:] = 1
    c_test[n_inliers_test:] = 'r'

    return X_train, y_train.ravel(), c_train, X_test, y_test.ravel(), c_test


def load_cardio():
    '''
    load cardio data
    :return:
    '''
    mat = loadmat(os.path.join('resources', 'cardio.mat'))
    X = mat['X']
    y = mat['y'].ravel()

    return X, y


def load_letter():
    '''
    load letter data
    :return:
    '''
    mat = loadmat(os.path.join('resources', 'letters.mat'))
    X = mat['X']
    y = mat['y'].ravel()

    return X, y
