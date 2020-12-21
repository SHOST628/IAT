from util.send_request import SendRequest
import xlrd


class DataProcess:
    """
    get a row data from excel
    """
    def __init__(self, workbook, sheet_name):
        self.workbook = workbook
        self.sheet_name = sheet_name

    def _gen_dict(self, key_list, value_list):
        return dict(zip(key_list, value_list))

    def get_row_dict(self, value_row, key_row=0):
        """
        merge sheet requestd header and data into a dict
        :param value_row: detail
        :param key_row: header
        :return:
        """
        sheet = self.workbook.sheet_by_name(self.sheet_name)
        header = sheet.row_values(key_row)
        detail = sheet.row_values(value_row)
        hd_dict = self._gen_dict(header, detail)
        return hd_dict


class MergeProcess:
    """
    merge header and detail into queue
    """
    def __init__(self, workbook, sheet_header_name):
        self.sheet = workbook.sheet_by_name(sheet_header_name)
        indexs = range(1, self.sheet.nrows)
        self.api_names = self.sheet.col_values(1)
        self.api_names.remove("APINAME")
        self.requesth_header = self.sheet.row_values(0)
        self.api_ids = dict(zip(self.api_names, indexs))
        self.data_queue = []

    def merge_requesth_d(self, requestd_dict):
        api_name = requestd_dict["APINAME"]
        if api_name in self.api_ids.keys():
            api_name_index = self.api_ids[requestd_dict["APINAME"]]
            requesth_row_data = self.sheet.row_values(api_name_index)
            api_header_dict = dict(zip(self.requesth_header, requesth_row_data))
            self.data_queue.append(api_header_dict)
            self.data_queue.append(requestd_dict)
            return self.data_queue
        print("Sheet【REQUESTH】can not find apiname: {}".format(api_name))
        return None


class DataCollection:
    def __init__(self, excel_name):
        self.excel_name = excel_name
        self.header_sheet_name = "REQUESTH"
        self.detail_sheet_name = "REQUESTD"

    def collect(self):
        pass


excel_name = "../testcase/testcase.xlsx"
workbook = xlrd.open_workbook(excel_name)
sheet_header_name = "REQUESTH"
sheet_detail_name = "REQUESTD"
dataprocess = DataProcess(workbook, sheet_detail_name)
row_one = dataprocess.get_row_dict(1)
mergeprocess = MergeProcess(workbook, sheet_header_name)
queue = mergeprocess.merge_requesth_d(row_one)
print(queue)
request = SendRequest()
res = request.get(queue)
# print(res.text)
