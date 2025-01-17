import numpy as np
from Kernel import Kernel
import cvxopt
import cvxopt.solvers


class SVM(object):
    def __init__(self, kernel, C=None):
        self.kernel = kernel
        self.C = C
        if self.C is not None: self.C = float(self.C)

    def fit(self, X, y):
        n_samples, n_features = X.shape

        # Gram matrix
        K = np.zeros((n_samples, n_samples))
        for i in range(n_samples):
            for j in range(n_samples):
                K[i, j] = self.kernel(X[i], X[j])

        P = cvxopt.matrix(np.outer(y, y) * K)
        q = cvxopt.matrix(np.ones(n_samples) * -1)
        A = cvxopt.matrix(y, (1, n_samples), 'd')
        b = cvxopt.matrix(0.0)

        if self.C is None:
            G = cvxopt.matrix(np.diag(np.ones(n_samples) * -1))
            h = cvxopt.matrix(np.zeros(n_samples))
        else:
            tmp1 = np.diag(np.ones(n_samples) * -1)
            tmp2 = np.identity(n_samples)
            G = cvxopt.matrix(np.vstack((tmp1, tmp2)))
            tmp1 = np.zeros(n_samples)
            tmp2 = np.ones(n_samples) * self.C
            h = cvxopt.matrix(np.hstack((tmp1, tmp2)))

        # solve QP problem
        cvxopt.solvers.options['show_progress'] = False
        solution = cvxopt.solvers.qp(P, q, G, h, A, b)

        # Lagrange multipliers
        lambd = np.ravel(solution['x'])

        # Support vectors have non zero lagrange multipliers
        sv = lambd > 1e-5
        ind = np.arange(len(lambd))[sv]
        self.lambd = lambd[sv]
        self.sv = X[sv]
        self.sv_y = y[sv]
        # print("%d support vectors out of %d points" % (len(self.lambd), n_samples))

        # Intercept
        self.b = 0
        for n in range(len(self.lambd)):
            self.b += self.sv_y[n]
            self.b -= np.sum(self.lambd * self.sv_y * K[ind[n], sv])
        self.b /= len(self.lambd)

        # Weight vector
        if self.kernel == Kernel.linear_kernel:
            self.w = np.zeros(n_features)
            for n in range(len(self.lambd)):
                self.w += self.lambd[n] * self.sv_y[n] * self.sv[n]
        else:
            self.w = None

    def project(self, X):
        if self.w is not None:
            return np.dot(X, self.w) + self.b
        else:
            y_predict = np.zeros(len(X))
            for i in range(len(X)):
                s = 0
                for lambd, sv_y, sv in zip(self.lambd, self.sv_y, self.sv):
                    s += lambd * sv_y * self.kernel(X[i], sv)
                y_predict[i] = s
            return y_predict + self.b

    def predict(self, X):
        return np.sign(self.project(X))
