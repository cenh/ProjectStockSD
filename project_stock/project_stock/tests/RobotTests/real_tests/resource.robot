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
${OVERVIEW URL}      http://projectstock.karen.gg/projects/
${CORRECT URL}    http://projectstock.karen.gg/projects/13

*** Keywords ***
Open Browser To Project Page
    Open Browser    ${OVERVIEW URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Project Page Should Be Open

Project Page Should Be Open
    Title Should Be    Projects

Go To Project Page
    Go To    ${OVERVIEW URL}
    Project Page Should Be Open

Click A Link
    Click Link            Beer brewing
    Click Link            Link=${http://projectstock.karen.gg/projects/13}
    Click Link            xpath=//a[@href=http://projectstock.karen.gg/projects/13']
    Click Element         xpath=//a[@href='/projects/13']



Chosen Project Should Be Open
    Location Should Be    ${CORRECT URL}
    Title Should Be    Beer brewing

