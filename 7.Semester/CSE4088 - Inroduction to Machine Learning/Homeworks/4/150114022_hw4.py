import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn import svm

columns = ['digit', 'intensity', 'symmetry']
#Read the train and test data
features_train = pd.read_table('features.train.txt', sep= '\s+', names=columns)
features_test = pd.read_table('features.test.txt', sep= '\s+', names=columns)

dict_one_vs_all = dict( # Output labels for one vs all
    {'zero_vs_all':  0, 'one_vs_all': 1,
     'two_vs_all':   2, 'three_vs_all': 3,
     'four_vs_all':  4, 'five_vs_all': 5,
     'six_vs_all':   6, 'seven_vs_all': 7,
     'eight_vs_all': 8, 'nine_vs_all': 9
    })

def create_one_vs_all(df, classifiers):
    one_vs_all = pd.DataFrame(df, copy=True)
    for class_label, digit in classifiers.items():
        labels = one_vs_all.loc[one_vs_all['digit'] == digit, 'digit']
        labels.loc[:] = 1.0 # +1 for one
        one_vs_all[class_label] = labels

    one_vs_all.fillna(-1.0, inplace=True) # -1 for all
    return one_vs_all

features_train_one_vs_all = create_one_vs_all(features_train, dict_one_vs_all)

def dataset(df, class_label): #Get dataset, inputs and outputs
    ins = np.array(df.loc[:, ['intensity', 'symmetry']])
    outs = np.array(df.loc[:, class_label])
    data = np.column_stack((ins, outs))
    return data


class SVM: # Support Vector Machine (SVM) class
    def __init__(self, Q=2, rbf=False):

        self.Q = Q # Degree of the polynomial
        self.rbf = rbf # RBF or polynomial kernel

    def train(self, inputs, outputs, C=0.01): # Training SVM
        xn = inputs
        yn = outputs
        N = len(xn)

        mat = []
        for row_idx in range(0, N):
            for col_idx in range(0, N):
                if self.rbf:
                    kernel = np.exp(-1.0 * (np.linalg.norm(xn[row_idx] - xn[col_idx]) ** 2))
                else:
                    kernel = (1.0 + np.dot(xn[row_idx].T, xn[col_idx])) ** self.Q
                val = yn[row_idx] * yn[col_idx] * kernel
                mat.append(val)
        mat = np.array(mat).reshape((N, N))

        # form matrices for quadratic programming solver
        dim = len(xn[0])
        P = matrix(mat, tc='d')
        q = matrix(-np.ones(N), tc='d')
        b = matrix(0.0, tc='d')
        A = matrix(yn, tc='d')
        A = A.trans()
        G = matrix(-np.identity(N), tc='d')

        G_zero = -np.identity(N)
        h_zero = np.zeros(N)
        G_C = np.identity(N)
        h_C = C * np.ones(N)

        G = matrix(np.concatenate((G_zero, G_C)), tc='d')
        h = matrix(np.concatenate((h_zero, h_C)), tc='d')


        solvers.options['show_progress'] = False

        sol = solvers.qp(P, q, G, h, A, b)
        alpha = np.array(list(sol['x']))

        sv = []
        sv_alphas = []
        sv_outputs = []
        for n in range(0, N):
            if alpha[n] > 1e-5 and alpha[n] <= C:  # => xn[n] is support vector
                sv.append(xn[n])
                sv_alphas.append(alpha[n])
                sv_outputs.append(yn[n])


        num_sv = len(sv) # compute number of support vectors

        bs = []
        for m in range(0, num_sv):

            b = sv_outputs[m]
            for n in range(0, num_sv):
                if self.rbf:
                    kernel = np.exp(-1.0 * (np.linalg.norm(sv[n] - sv[m]) ** 2))
                else:
                    kernel = (1.0 + np.dot(sv[n].T, sv[m])) ** self.Q

                b -= sv_alphas[n] * sv_outputs[n] * kernel
            bs.append(b)

        return np.array(sv_alphas), np.array(sv), np.array(sv_outputs), b

    def error(self, sv_alphas, sv, sv_outputs, b, inputs, outputs): # Calculate the error
        x = inputs
        y = outputs
        num_sv = len(sv)

        gs = []
        for xm in x:
            signal = 0.0
            for n in range(0, num_sv):
                if self.rbf:
                    kernel = np.exp(-1.0 * (np.linalg.norm(sv[n] - xm) ** 2))
                else:
                    kernel = (1.0 + np.dot(sv[n].T, xm)) ** self.Q
                signal += sv_alphas[n] * sv_outputs[n] * kernel
            signal += b
            gs.append(signal)

        g = np.array(np.sign(gs))
        return 100. * np.sum(y != g) / len(y)


def in_out_sample_errors(classifiers, features_train, features_test=None, Cs=[0.01], Qs=[2], kernel='poly',
                         gamma=1.0, coef0=1.0):
    for class_label in classifiers.keys():
        for C in Cs:
            for Q in Qs:
                dataset_train = dataset(features_train, class_label)
                inputs_train = dataset_train[:, 0:2]
                outputs_train = dataset_train[:, 2]

                if kernel == 'poly':
                    clf = svm.SVC(C=C, kernel=kernel, gamma=gamma, coef0=coef0, degree=Q)
                elif kernel == 'rbf':
                    clf = svm.SVC(C=C, kernel=kernel, gamma=gamma)
                clf.fit(inputs_train, outputs_train)

                error_in_sample = 1.0 - clf.score(inputs_train, outputs_train)

                if not features_test.empty:
                    dataset_test = dataset(features_test, class_label)
                    inputs_test = dataset_test[:, 0:2]
                    outputs_test = dataset_test[:, 2]

                    error_out_sample = 1.0 - accuracy_score(outputs_test, clf.predict(inputs_test))

                if features_test.empty:
                    print(
                        'C = {0} and Q = {1}, ({2}) Ein = {3}%, '
                        'and # of support vectors = {4}.\n'
                        .format(C, Q, class_label, round(error_in_sample, 3), len(clf.support_vectors_)))

                elif kernel == 'poly':
                    print(
                        'C = {0} and Q = {1}, "{2}" Ein = {3}%, '
                        ' Eout = {4}% and # of support vectors = {5}.\n'
                        .format(C, Q, class_label, round(error_in_sample, 3), round(error_out_sample, 3),
                                len(clf.support_vectors_)))
                elif kernel == 'rbf':
                    print('C = {0}: "{2}"  Ein = {3}% and '
                          ' Eout = {4}%\n'
                          .format(C, gamma, class_label, round(error_in_sample, 3), round(error_out_sample, 3)))


print("\n\nProblem 2, 3 and 4:\n")
in_out_sample_errors(dict_one_vs_all, features_train_one_vs_all, pd.DataFrame(), Cs=[0.01], Qs=[2], kernel='poly')

classifiers_one_vs_one = dict({'one_vs_five': [1,5]})


def create_one_vs_one(df, classifiers):
    for class_label in classifiers.keys():
        digits = classifiers[class_label]
        one_vs_one = pd.DataFrame(df.loc[df['digit'].isin(digits), :], copy=True)
        for digit in digits:
            labels = one_vs_one.loc[one_vs_one['digit'] == digit, 'digit']
            labels.loc[:] = 1.0
            one_vs_one[class_label] = labels
            break

    one_vs_one.fillna(-1.0, inplace=True)
    return one_vs_one

features_train_one_vs_one = create_one_vs_one(features_train, classifiers_one_vs_one)
features_test_one_vs_one = create_one_vs_one(features_test, classifiers_one_vs_one)


print("\n\nProblem 5: ")
in_out_sample_errors(classifiers_one_vs_one, features_train_one_vs_one, features_test_one_vs_one,
                     Cs=[0.001, 0.01, 0.1, 1.0], Qs=[2], kernel='poly')

print("\n\nProblem 6:\n")
in_out_sample_errors(classifiers_one_vs_one, features_train_one_vs_one, features_test_one_vs_one,
                     Cs=[0.0001,0.001, 0.01, 0.1, 1.0], Qs=[2, 5], kernel='poly')



def cv_error(classifiers, features_train, Cs, num_folds, shuffle, num_runs):
    errors_cv = OrderedDict.fromkeys(Cs, 0.0)
    low_cv_counts = OrderedDict.fromkeys(Cs, 0)

    for class_label in classifiers.keys():
        dataset_train = dataset(features_train, class_label)
        inputs_train = dataset_train[:, 0:2]
        outputs_train = dataset_train[:, 2]

        for i in range(0, num_runs):
            k_fold = KFold(n_splits=num_folds, shuffle=shuffle)
            run_errors_cv = []
            for C in Cs:
                clf = svm.SVC(C=C, kernel='poly', gamma=1.0, coef0=1.0, degree=2)
                scores = cross_val_score(clf, inputs_train, outputs_train, cv=k_fold)
                error_cv = 1.0 - scores.mean()
                errors_cv[C] += error_cv
                run_errors_cv.append(error_cv)

            min_error_cv = np.argmin(run_errors_cv)
            low_cv_counts[list(low_cv_counts.keys())[min_error_cv]] += 1

        low_cv_count = max(low_cv_counts, key=low_cv_counts.get)

        print(
            'C = {0} is selected the most often, ({1}/{2} runs) \nAverage '
            ' Ecv = {3}'.format(low_cv_count, low_cv_counts[low_cv_count], num_runs,
                                      round(errors_cv[low_cv_count] / num_runs, 3)))


print("\n\nProblem 7 and problem 8:\n")
cv_error(classifiers_one_vs_one, features_train_one_vs_one, Cs=[0.0001, 0.001, 0.01, 0.1, 1.0], num_folds=10,
                shuffle=True, num_runs=100)

print("\n\nProblem 9 and problem 10:\n")
in_out_sample_errors(classifiers_one_vs_one, features_train_one_vs_one, features_test_one_vs_one,
                     Cs=[0.01, 1., 100., 1.*10**4, 1.*10**6], kernel='rbf', gamma=1.0)

