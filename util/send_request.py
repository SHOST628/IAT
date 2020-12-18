import requests


class SendRequest:
    def __init__(self):
        pass

    def get(self, api_data):
        if api_data is not None:
            header = api_data[0]
            detail = api_data[1]
            header_status = header["ACTIVE"].upper()  # y or n
            detail_status = detail["ACTIVE"].upper()
            if header_status == 'Y':
                if detail_status == 'Y':
                    try:
                        url = header["URL"]
                        parameters = detail['PARAMETERS']
                        request = url + '?' + parameters
                        result = requests.get(request)
                        return result
                    except:
                        raise Exception('testcase is not complete')
        print("No available testcase")
        return None


    def post(self):
        pass
