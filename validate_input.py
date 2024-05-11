class InputValidator:
    """Validator for user input in UI App version"""
    def __init__(self) -> None:
        pass

    def is_valid(self, inp: str, mini: float, maxi: float) -> bool:
        """Check if input is valid.
        It should be convertible to float and between mini and maxi.
        """
        return self.is_float(inp) and self.is_in_range(inp, mini, maxi)

    @staticmethod
    def is_float(inp: str) -> bool:
        """Check if user input is convertible to float."""
        is_valid = False
        try:
            inp = float(inp)
            is_valid = True
        except ValueError:
            pass
        return is_valid

    @staticmethod
    def is_in_range(inp: str, mini: float, maxi: float) -> bool:
        """Check if user input is between mini and maxi."""
        try:
            return mini <= float(inp) <= maxi
        except ValueError:
            return False
