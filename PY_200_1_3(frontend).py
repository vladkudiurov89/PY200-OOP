class FrontendCalc:
    def __init__(self, name, num_1, num_2):
        self.name = name
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def execute():
        while True:
            exp = input('Enter number operator number')
            if exp == "Exit":
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
                print(BackendCalc.test_add(num_1, num_2))
            elif op == '-':
                print(BackendCalc.test_sub(num_1, num_2))
            elif op == '*':
                print(BackendCalc.test_mul(num_1, num_2))
            elif op == '/':
                print(BackendCalc.test_div(num_1, num_2))


class BackendCalc:
    frontends = {}

    def __init__(self, num_1, num_2):
        super().__init__(num_1, num_2)

    @classmethod
    def test_add(cls, frontend_type, num_1, num_2):
        try:
            cls.frontends[frontend_type] += 1
        except TypeError("num_1 and num_2 must be float"):
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 + num_2

    @classmethod
    def test_sub(cls, num_1, num_2, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except TypeError("num_1 and num_2 must be float"):
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 - num_2

    @classmethod
    def test_mul(cls, num_1, num_2, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except TypeError("num_1 and num_2 must be float"):
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 * num_2

    @classmethod
    def test_div(cls, num_1, num_2, frontend_type):
        try:
            cls.frontends[frontend_type] += 1
        except TypeError("num_1 and num_2 must be float"):
            cls.frontends[frontend_type] = 1
        if not (isinstance(num_1, (int, float)) and isinstance(num_2, (int, float))):
            raise TypeError("num_1 and num_2 must be float")
        return num_1 // num_2


