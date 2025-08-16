from selene import browser, have


def test_table_texts_selene():
    browser.open(
        'https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html'
    )

    browser.element('#customers').all('tr').should(
        have.exact_texts(
            'Company Contact Country',
            'Google Maria Anders Germany',
            'Meta Francisco Chang Mexico',
            'Microsoft Roland Mendel Austria',
            'Island Trading Helen Bennett UK',
            'Adobe Yoshi Tannamuri Canada',
            'Amazon Giovanni Rovelli Italy',
        )
    )