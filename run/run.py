import os,sys
sys.path.append(os.path.dirname(__file__))
from config.read_config import ReadConfig
from common.send_email import Email


def run_case():
    """exectue all testcase"""

    report_path = ReadConfig().get_report_path("path")
    email = Email()
    email.send_email()



if __name__ =="__main__":
    run_case()
