class InputValidator:
    def __init__(self) -> None:
        pass

    def is_valid(self, inp: str, mini: float, maxi: float) -> bool:
        return self.is_float(inp) and self.is_in_range(inp, mini, maxi)


    @staticmethod
    def is_float(inp: str) -> bool:
        is_valid = False
        try:
            inp = float(inp)
            is_valid = True
        except ValueError:
            pass
        return is_valid

    @staticmethod
    def is_in_range(inp: str, mini: float, maxi: float) -> bool:
        try:
            return mini <= float(inp) <= maxi
        except ValueError:
            return False

