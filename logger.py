from datetime import datetime as dt
from guid import dict_log


def get_log(res, oper):
    dtime = dt.now()
    print('{}; Операция: {}; Результат: {}'
            .format(dtime, oper, res))