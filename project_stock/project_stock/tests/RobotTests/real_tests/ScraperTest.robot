*** Settings ***
Documentation     A test suite with a single test for comparing scraper results.
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
IsEqual
  Open Browser To Supervisor Page
  ${string1}    Get Text    xpath=(//html/body/center/table/tbody/tr[25]/td[3])

  Go To Diku Page
  ${string2}    Get Text      xpath=(//*[@id="content"]/div[3]/div[3]/div/div/ul[1]/li/div[2]/ul[1]/li/a/span)

  Should Be Equal     ${string1}      ${string2}
  [Teardown]    Close Browser
