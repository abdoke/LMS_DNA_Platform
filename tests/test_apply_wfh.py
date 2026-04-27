from venv import logger
from pages.leave_page import LeavePage
from pages.tracker_page import TrackerPage

def test_apply_wfh(login):
    logger.info("++++++++++Test case: Apply wfh started executing++++++++++")
    leave_page =LeavePage(login)
    leave_page.apply_wfh()

def test_cancel_leave(login):
    logger.info("++++++++++Test case: Cancel wfh started executing++++++++++")
    leave_page = LeavePage(login)
    leave_page.click_tracker()

    tracker = TrackerPage(login)
    tracker.click_filter()
    tracker.click_wfh()
    tracker.click_apply()
    tracker.click_wfh_cancel()
    tracker.click_confirm()