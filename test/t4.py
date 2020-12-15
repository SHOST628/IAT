import xlrd
import xlwt


class DataProcess:
    def __init__(self, excel_name, sheet_name):
        self.workbook = xlrd.open_workbook(excel_name)
        self.sheet_name = sheet_name

    def _gen_dict(self, key_list, value_list):
        return dict(zip(key_list, value_list))

    def get_row_dict(self, value_row, key_row=0):
        sheet = self.workbook.sheet_by_name(self.sheet_name)
        header = sheet.row_values(key_row)
        detail = sheet.row_values(value_row)
        hd_dict = self._gen_dict(header, detail)
        return hd_dict


# data = xlrd.open_workbook("../testcase/testcase.xlsx")
# sheet_name = data.sheet_names()
# sheet0 = data.sheet_by_index(1)
# row_zero = sheet0.row_values(0)
# row_one = sheet0.row_values(1)
# print(gen_dict(row_zero,row_one))
data = DataProcess("../testcase/testcase.xlsx", "REQUESTD")
data.get_row_dict(1)





