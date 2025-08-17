ёimport os

import pytest
import selene
from selene import browser, have, be, command, query, by

def test_add_todos_and_complete_one():

    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('test123@gmail.com')
    browser.element('[for="gender-radio-1"].custom-control-label').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="1996"]').click()

    browser.element('.react-datepicker__day--023').click()

    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for ="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('../selene-in-action/cat_hungry.png'))
    browser.element('#currentAddress').type('123 Main St')

    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()

    browser.element('#submit').click()

    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'John Doe',
        'test123@gmail.com',
        'Male',
        '1234567890',
        '23 June,1996',
        'Math',
        'Reading',
        'cat_hungry.png',
        '123 Main St',
        'NCR Delhi'
    ))

