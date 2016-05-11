*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.
Library           Selenium2Library

*** Variables ***
${SERVER}         http://128.199.39.136/
${BROWSER}        Firefox
${DELAY}          0
${VALID USER}     test
${VALID PASSWORD}    acceptance
${LOGIN URL}      http://128.199.39.136/admin/login/?next=/admin/
${WELCOME URL}    http://128.199.39.136/
${ERROR URL}      http://128.199.39.136/admin/login/?next=/admin/

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Login Page Should Be Open

Login Page Should Be Open
    Title Should Be    Log in | Django site admin

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    id_username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    id_password   ${password}

Submit Credentials
    Click Button    submit;

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Welcome Page
