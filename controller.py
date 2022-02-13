import view
import guid


def button_click():
    value_a = view.get_value()
    oper = view.get_operator()
    value_b = view.get_value()
    func = guid.dict_fract[oper]
    func.init(value_a, value_b)
    result = func.do_it()
    view.get_result(result)