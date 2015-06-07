from Posn_selector import Posn_Selector

class Posn_y(Posn_Selector):
    """
    To represent the y coordinate of a Posn
    """

    def __init__(self, sub_expr):
        super().__init__(sub_expr)

    def eval(self, defs):
        return self.eval_helper(defs).right
