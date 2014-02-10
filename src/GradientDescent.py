from numpy import linalg
import math
import numpy as np
import matplotlib.pyplot as plt

class GradientDescent:
    'Gradient Descent class for optimization'

    #--------------------------
    # Private member variables
    #--------------------------


    """
    @brief Constructor
    @param gamma     step-size (initial if using Armijo)
    @param u_initial initial u value
    """
    def __init__(self, gamma, u_initial, maxIter=1000, thresh=1e-5):

        # main variables
        self._U     = []                 # Vector of u's
        self._F     = []                 # Vector of f(u)'s
        self._U.append(u_initial)        # Add initial u to vector
        self._gammaInit = gamma          # Initial gamma
        self._gamma = gamma              # Gradient descent step size
        self._maxIterations = maxIter    # Max iterations before giving up
        self._threshold = thresh         # Convergence threshold

        # Armijo variables
        self._useArmijo = False          # Whether or not to use Armijo step size
        self._alpha = 0.5                # Armijo parameter b/t 0 & 1
        self._beta  = 0.5                # Armijo parameter b/t 0 & 1
        
    """
    @brief Setter for _maxIterations private member variable
    @param maxIter max number of iterations for gradient descent
    """
    def setMaxIterations(self, maxIter):
        self._maxIterations = maxIter

    """
    @brief Setter for convergence threshold
    @param thresh desired convergence threshold
    """
    def setConvergenceThreshold(self, thresh):
        self._threshold = thresh

    """
    @brief Get Armijo k value
           F(u - (b^k * df(u)/dt)) - F(u) < -a * b^k * norm(df/dt)^2
           When true, pick gamma = b^k
    """
    def getStepSize(self):
        k = 1.0
        f = self._F[-1]
        u = self._U[-1]
        df = self.df(u)
        while True:
            fa = self.f(u - (self._beta**k * df))
            eq = fa - f + (self._alpha * self._beta**k * (linalg.norm(df))**2)
            if eq <= 0.0001:
                # print 'k = %d, g = %f\n' % (k, self._beta**k)
                return self._beta**k # new gamma
            k += 1                   # increment k
        print 'Failed to get Armijo step size!'
        return -1

    """
    @brief Whether or not to use Armijo step size
    @param use True or False boolean
    """
    def useArmijo(self, use):
        self._useArmijo = use

    """
    @brief Gradient descent function
    """
    def run(self):
        success = False
        # iterate until found min or reach max iterations
        for i in range(0, self._maxIterations):
            u = self._U[-1]
            self._F.append(self.f(u))
            if self._useArmijo:
                self._gamma = self.getStepSize()
            if self._gamma == -1:
                print "Failed to find gamma in Armijo method"
                exit(-1)
            u = u - (self._gamma * self.df(u))
            self._U.append(u)
            error = linalg.norm(self.df(u))
            if error < self._threshold:
                print '\nFound minimum after %d iterations:\n\tu_min \t\t= %.3f\n\tf(u_min) \t= %.3f\n\terror \t\t= %.3g' \
                    % (i, u, self.f(u), error)
                success = True
                break
        if success == False:
            print 'Couldn\'t find minimum after max iterations of {}'.format(self._maxIterations)
        return [self._U, self._F]

    """
    @brief Return the function values over the given time range
    @param time Time range to compute f(u) over
    """
    def getFunctionOverRange(self, time):
        F = []
        for t in time:
            F.append(self.f(t))
        return F

    """
    @brief Prints a plot of f(u) and u(t)
    """
    def plot(self, title):
        # Plot of F(u)
        Umin = self._U[-1]
        Fmin = self._F[-1]
        u = np.linspace(0.0, 8.0, 5.0/0.01)
        F = self.getFunctionOverRange(u)

        fig1 = plt.figure()
        plt.subplot(211)
        plt.plot(u, F, 'k')
        plt.title('%s\nFunction versus control input ($\gamma_i$ = %.2f)' % (title, self._gammaInit), fontdict=self._font)
        plt.xlabel('control input, u', fontdict=self._font)
        plt.ylabel('function, f(u)', fontdict=self._font)
        plt.text(Umin-.5, Fmin+10, '$F(u_{min})$ = %.2f\n$u_{min}$ = %.2f' % (Fmin, Umin))
        plt.plot(self._U[0], self._F[0], 'go', label="$u_i$") # Initial value
        plt.plot(Umin, Fmin, 'ro', label="$u_{min}$") # Final minimum value
        plt.legend()

        # # Plot of u(t)
        plt.subplot(212)
        plt.plot(np.linspace(0.0, len(self._U), len(self._U)), self._U, 'k')
        plt.title('Control input versus iteration', fontdict=self._font)
        plt.xlabel('iteration #', fontdict=self._font)
        plt.ylabel('control input, u(t)', fontdict=self._font)

        plt.tight_layout()
        plt.draw()
        plt.show()

    """
    @brief Set font for plots
    @param font Desired font
    """
    def setPlotFont(self, font):
        self._font = font

    #------------------------
    # User-defined functions
    #------------------------

    """
    @brief Function evaluted at u
    @param u input value to evaluate function at
    """
    def f(self, u):
        return u**3 - 7.0*u**2 + 2.0*u + 1.0

    """
    @brief Derivative of f(u)
    @param u input value to evaluate derivative at
    """
    def df(self, u):
        return 3.0*u**2 - 14.0*u + 2.0

    """
    @brief 2nd Derivative of f(u)
    @param u input value to evalute 2nd derivative at
    """
    def ddf(self, u):
        return 6.0*u - 14.0

    _font = {'family' : 'serif',
            'color'  : 'darkred',
            'weight' : 'normal',
            'size'   : 16,
            }
