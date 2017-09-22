class Three_Neurons_Network(Neural_Network):
    def __init__(self, input_size, output_size):
        super().__init__(input_size, output_size)

    def initialize_param(self, initializer=tfe.Initializer.Zero.value):
        self.params['W0'] = initializer(shape=(self.input_size, self.output_size), name='W0').get_variable()
        self.params['b0'] = initializer(shape=(self.output_size,), name='b0').get_variable()
        self.params['W1'] = initializer(shape=(self.input_size, self.output_size), name='W1').get_variable()
        self.params['b1'] = initializer(shape=(self.output_size,), name='b1').get_variable()
        self.params['W2'] = initializer(shape=(self.input_size, self.output_size), name='W2').get_variable()
        self.params['b2'] = initializer(shape=(self.output_size,), name='b2').get_variable()

    def layering(self, activator=tfe.Activator.ReLU.value):
        self.activator = activator
        u0 = tfl.Affine(self.params['W0'], self.input_node, self.params['b0'], name='A0')
        o0 = activator(u0, name="O0")

        u1 = tfl.Affine(self.params['W1'], self.input_node, self.params['b1'], name='A1')
        o1 = activator(u1, name="O1")

        u2 = tfl.Affine(self.params['W2'], self.input_node, self.params['b2'], name='A2')

        self.output = activator(u2, name="O2")
        self.error = tfl.SquaredError(self.output, self.target_node, name="SE")
