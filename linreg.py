import numpy
from sklearn import linear_model

# Function to normalize data:
def normalize(X):
    mean_r = []
    std_r = []
 
    X_norm = X
 
    n_c = X.shape[1]
    for i in range(n_c):
        m = numpy.mean(X[:, i])
        s = numpy.std(X[:, i])
        mean_r.append(m)
        std_r.append(s)
        X_norm[:, i] = (X_norm[:, i] - m) / s
 
    return X_norm

# Load data matrix from file:
data = numpy.loadtxt('matrix.dat')

# Randomize the examples in the matrix:
numpy.random.shuffle(data)

# First column (column 0) in matrix is Qcooling value, which is y.
# Second column (column 1) in matrix is Tsupply.

# The rest of the matrix (columns 2 - end) are the Tzone values for each zone.
# This is placed in X:
X = data[:, 2:]

# Subtract Tsupply from Tzone for each zone:
for i in range(1,X.shape[1]):
    X[:, i] -= data[:, 1]
    
# Normalize the value of X:
X = normalize(X)

# Extend X to include all-ones feature:
beta = numpy.array([numpy.ones(X.shape[0])]).T
X = numpy.concatenate((beta, X), axis=1)

# Set y to Qcooling value:
y = numpy.array([data[:,0]]).T

# Create split between training and test data (currently 9:1):
split = int(X.shape[0] * 0.1)

X_train = X[:-split]
X_test = X[-split:]

y_train = y[:-split]
y_test = y[-split:]

# Train the linear regression model using Scikit's least-squares implementation:
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

# Output the trained coefficients:
print('Coefficients: \n', regr.coef_)

# Output mean percentage error, square error, and variance score:
print('Mean percentage error: %.2f' % numpy.mean((numpy.abs(regr.predict(X_test) - y_test) / y_test) * 100))
print("Residual sum of squares: %.2f" % numpy.mean((regr.predict(X_test) - y_test) ** 2))
print('Variance score: %.2f' % regr.score(X_test, y_test))