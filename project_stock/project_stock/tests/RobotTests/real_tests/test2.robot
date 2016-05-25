*** Settings ***
Documentation     A test suite with a single test for a working link.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Click A Link
    Choen Project Should Be Open
    [Teardown]    Close Browser
