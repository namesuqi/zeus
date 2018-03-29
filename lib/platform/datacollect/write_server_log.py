import sys
import types
import write_program.data_provider


def write_all_log():
    m = sys.modules['write_program.data_provider']
    attstr = dir(m)
    for str in attstr:
        att = getattr(m, str)
        if type(att) == types.ModuleType:
            subattstr = dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt) == types.TypeType and issubclass(subatt, m.DataProvider):
                    tmpObj = subatt()
                    tmpObj.clear_data()
                    tmpObj.make_data()
                    tmpObj.write_log()

def write_one_log(task_name):
    m = sys.modules['write_program.data_provider']
    attstr = dir(m)
    for str in attstr:
        att = getattr(m, str)
        if type(att) == types.ModuleType:
            subattstr = dir(att)
            for substr in subattstr:
                subatt = getattr(att, substr)
                if type(subatt) == types.TypeType and subatt.__name__ == task_name and issubclass(subatt,
                                                                                                  m.DataProvider):
                    tmpObj = subatt()
                    tmpObj.clear_data()
                    tmpObj.make_data()
                    tmpObj.write_log()
            else:
                continue
            break


if __name__ == '__main__':
    write_all_log()
    # writeonelog("server_push_prefetch_task")
