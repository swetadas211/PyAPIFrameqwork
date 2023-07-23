# Python API Automation Framework
________________________________

### CRUD - Integration Teset cases for the Restfull Booker
 URL - https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking
1. GET 2. POST 3. PATCH 4. DELETE
2. Repsonse Body, Header, Staus code
3. AUTH - Cookies based Auth , Basic Auth 
3. JSON Schema verification

## Tech Stack
1. Request Module
2. PyTest, PyTest-html
3. Allure Report
4. Faker,  CSV, JSON, YAML
5. Run via Commandline - Jenkins

## How to Run loacally & see the report
  ### D:\pythonProject\PyAPIFrameqwork\tests> 
pytest Integration_test/test_create_booking.py -s -v --alluredir=./reports --html=report.html

## P. S  - 


## How To Run via jenkins