import pytest

@pytest.mark.run(order=1)
def test_create_booking_tc1():
    assert True==True

@pytest.mark.run(order=2)
def test_create_booking_tc2():
    assert True == False

@pytest.mark.run(order=3)
def test_create_booking_tc3():
    assert True == True



# -s: Allows pytest to display the standard output for any print statements in your test functions.
# -v: Increases verbosity to see more details about the test execution.
# --alluredir=./reports:  Specifies the directory where Allure test reports will be generated.
# --html=report.html:  Specifies the file where an HTML test report will be generated.