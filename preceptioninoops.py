class Perceptron:

    def _init_(self, n_inputs):
        
        self.n_inputs = n_inputs
        self.weights = np.zeros(n_inputs)
        self.bias = 0