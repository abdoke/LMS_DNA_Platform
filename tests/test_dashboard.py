from utils.test_data import TestData
from pages.leave_page import LeavePage

def test_dashboard(login):
    #page=login
    dashboard = LeavePage(login)
    expected_email = "hashedintestuser108@deloitte.com"
    expected_role = "Quality Engineer-I"
    expected_emp_id = "Emp Id - 5500967"

    #Verification of 4 categories displayed
    count = dashboard.validate_leave_categories_count()
    print("Total leave categories are: " + str(count) )
    assert count == 4, f"Expected 4 categories, found{count} "

    #printing the leave details
    dashboard.print_leave_details()

    #profile click
    dashboard.click_profile()

    #get user info
    user = dashboard.user_validation()
    assert user["email"] ==  expected_email, f"Email mismatch Expected: {expected_email}, Got :{user['email']}"
    assert user["role"] ==  expected_role, f"ROle mismatch Expected: {expected_role}, Got :{user['role']}"
    assert user["emp_id"] ==  expected_emp_id, f"Emp_id mismatch Expected: {expected_emp_id}, Got :{user['emp_id']}"


    #side panel option count
    actual_options_count = dashboard.get_side_option_count()
    print("Side option count " + str(actual_options_count))
    assert actual_options_count == 3, f"Side options mismatch Expected: {4}, Got {actual_options_count}"

