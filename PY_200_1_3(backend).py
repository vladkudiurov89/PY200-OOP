class FrontendCalc:
    def __init__(self, name, backend):
        self.BackendCalc = None
        self.backend = backend
        self.name = name

    @staticmethod
    def execute(backend):
        while True:
            exp = input('Enter number operator number')
            if exp == 'exit':
                break
            num = exp.split()
            if 3 != len(num):
                print('Expression have: element operator element')
                continue
            num_1, op, num_2 = num
            try:
                num_1 = int(num_1)
                num_2 = int(num_2)
            except TypeError('num_1 or num_2 must be int or float'):
                num_1 = float(num_1)
                num_2 = float(num_2)

            if op == '+':
                print(backend.test_add(num_1, num_2))
            elif op == '-':
                print(backend.test_sub(num_1, num_2))
            elif op == '*':
                print(backend.test_mul(num_1, num_2))
            elif op == '/':
                print(backend.test_div(num_1, num_2))


class BackendCalc:
    frontends = {}

    @staticmethod
    def staticmethod(frontends=None):
        return frontends

    def __init__(self, num_1, num_2):
        super().__init__(num_1, num_2)

    def test_add(self, frontend_type, num_1, num_2):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('num_1 or num_2 must be int or float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")

        return num_1 + num_2

    def test_sub(self, num_1, num_2, frontend_type):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('num_1 or num_2 must be int or float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 - num_2

    def test_mul(self, num_1, num_2, frontend_type):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('num_1 or num_2 must be int or float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 * num_2

    def test_div(self, num_1, num_2, frontend_type):
        try:
            self.frontends[frontend_type] += 1
        except TypeError('num_1 or num_2 must be int or float'):
            self.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 // num_2


