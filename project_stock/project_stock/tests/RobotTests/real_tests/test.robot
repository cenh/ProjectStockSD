*** Settings ***
Library           Selenium2Library
Library           Collections

*** Test Cases ***
Get All Links
    [Tags]    Links
    Open Browser    http://projectstock.karen.gg/    firefox
    Maximize Browser Window
    Comment    Count Number Of Links on the Page
    ${AllLinksCount}=    Get Matching Xpath Count    //a
    Comment    Log links count
    Log    ${AllLinksCount}
    Comment    Create a list to store link texts
    @{LinkItems}    Create List
    Comment    Loop through all links and store links value that has length more than 1 character
    : FOR    ${INDEX}    IN RANGE    1    7
    \    ${linklength}    Get Length    ${lintext}
    \    Run Keyword If    ${linklength}>1    Append To List    ${LinkItems}    ${lintext}
    ${LinkSize}=    Get Length    ${LinkItems}
    Log    ${LinkSize}
    Comment    Print all links
    : FOR    ${ELEMENT}    IN    @{LinkItems}
    \    Log    ${ELEMENT}
    Close Browser
