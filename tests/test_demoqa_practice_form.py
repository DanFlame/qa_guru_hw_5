from selene.support.shared import browser
from selene import have
import os


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Daniel')
    browser.element('#lastName').type('Fazylov')
    browser.element('#userEmail').type('daniel@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select>[value="1900"]').click()
    browser.element('.react-datepicker__month-select>[value="11"]').click()
    browser.element('.react-datepicker__day--013').click()
    browser.element('#subjectsInput').type('comp').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('.form-control-file').set_value(
        os.path.dirname(os.path.abspath(__file__))+'/tmp/picture.png'
    )
    browser.element('#currentAddress').type('Test Address')
    browser.element('#react-select-3-input').type('e').press_enter()
    browser.element('#react-select-4-input').type('e').press_enter()
    browser.element('#submit').press_enter()
    browser.element('.table').should(have.text(
        'Daniel Fazylov' and
        'daniel@test.com' and
        'Male' and
        '0123456789' and
        '13 December,1900' and
        'Computer Science' and
        'Music' and
        'picture.png' and
        'Test Address' and
        'Uttar Pradesh Merrut'
    ))
