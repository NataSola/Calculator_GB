import module_fractions.div_mod as fdiv
import module_fractions.mult_mod as fmul
import module_fractions.subt_mod as fsub
import module_fractions.sum_mod as fsum
import view
import guid

# oper = '/'

# a = 6
# b = 2

def button_click():
    value_a = view.get_value()
    oper = view.get_operator
    value_b = view.get_value()
    func = guid.dict_fract[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)






