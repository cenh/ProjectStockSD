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
${CORRECT URL}       http://projectstock.karen.gg/projects/13
${SUPERVISOR URL}    http://projectstock.karen.gg/supervisors/
${CORRECT SUPERVISOR}     http://projectstock.karen.gg/supervisors/2
${DIKU URL}          http://diku.dk/ansatte?pure=da/persons/162114

*** Keywords ***
Open Browser To Overview Page
    Open Browser    ${OVERVIEW URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Project Page Should Be Open


Open Browser To Supervisor Page
    Open Browser    ${SUPERVISOR URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Go To Diku Page
    Go To   ${DIKU URL}
    Set Selenium Speed    ${DELAY}


Project Page Should Be Open
    Title Should Be    Projects

Go To Project Page
    Go To    ${OVERVIEW URL}
    Project Page Should Be Open

Click A Link
    Click Element         xpath=//html/body/center/table[1]/tbody/tr[3]/td[1]



Chosen Project Should Be Open
    Location Should Be    ${CORRECT URL}
    Title Should Be    Beer brewing
