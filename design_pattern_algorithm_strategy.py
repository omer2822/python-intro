class AlgorithmStrategy:
    def __init__(self, algorithm):
        self.algorithm = algorithm

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def run_algorithm(self, data):
        return self.algorithm.run(data)


class Algorithm:
    def run(self, data):
        raise NotImplementedError("Subclasses must implement run() method.")


class AlgorithmA(Algorithm):
    def run(self, data):
        # Algorithm A implementation goes here
        pass


class AlgorithmB(Algorithm):
    def run(self, data):
        # Algorithm B implementation goes here
        pass
