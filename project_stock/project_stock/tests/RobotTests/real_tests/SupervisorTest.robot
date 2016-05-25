*** Settings ***
Documentation     A test suite with a single test for a working link.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Clickable link
    Open Browser To Supervisor Page
    Click Element           xpath=(//html/body/center/table/tbody/tr/td[contains(text(), "Torben")])
    [Teardown]    Close Browser
