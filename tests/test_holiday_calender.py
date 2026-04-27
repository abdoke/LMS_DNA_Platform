from venv import logger
from pages.holiday_calender_page import HolidayCalender
from pages.leave_page import LeavePage

def test_holiday_calender(login):
    logger.info("++++++++++Test case: Holiday calender details started executing++++++++++")
    leave_page =LeavePage(login)
    leave_page.click_holiday_calender()

    holiday_list = HolidayCalender(login)
    holiday_list.fetch_leave_details()

