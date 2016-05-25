*** Settings ***
Documentation     A test suite with a single test for a working link.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Clickable link
    Open Browser To Overview Page
    ${TableLinks}=      Get Matching Xpath Count     //html/body/center/table/tbody/tr/td
    : FOR     ${INDEX}     IN RANGE     1    ${TableLinks}
    \     Click Element       xpath=(//html/body/center/table/tbody/tr/td)[${INDEX}]
    \     Go To Project Page
    [Teardown]    Close Browser
