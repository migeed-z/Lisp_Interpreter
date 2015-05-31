from sExpr import sExpr
from BslError import BSLError

class FuncApplication(sExpr):

    def __init__(self, name, sl):
        """

        :param name: Name of the function
        :param sl: List of sExpr representing the parameters
        """
        self.name = name
        self.sl = sl

    def eval(self, defs):
        definition = defs.get(self.name) #this is a function defintion
        body = definition.body
        params = definition.params

        vals = self.sl.helper_eval(params)
        defs = self.helper_extend(defs, params, vals)

        return body.eval(defs)

    def helper_extend(self, defs, params, vals):
        """

        :param defs: Scope representing the definitions
        :param params: list of Strings representing parameters
        :param vals: list of numbers representing the values of the parameters
        :return:
        """

        if len(params) != len(vals):
            raise BSLError("Params and Vals must be equal")

        while len(params) != 0:
            name = params.pop()
            val = vals.pop()
            defs = defs.extend(name, val)

        return defs





