from pages.leave_page import LeavePage

def test_apply_leave(login):
    leave_page =LeavePage(login)
    leave_page.apply_leave()