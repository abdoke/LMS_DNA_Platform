from venv import logger
from pages.leave_page import LeavePage
from pages.tracker_page import TrackerPage

def test_apply_leave(login):
    logger.info("++++++++++Test case: Apply leave started executing++++++++++")
    leave_page =LeavePage(login)
    leave_page.apply_leave()

def test_cancel_leave(login):
    logger.info("++++++++++Test case: Cancel leave started executing++++++++++")
    leave_page = LeavePage(login)
    leave_page.click_tracker()

    tracker = TrackerPage(login)
    tracker.click_filter()
    tracker.click_leaves()
    tracker.click_apply()
    tracker.click_cancel()
    tracker.click_confirm()