*** Settings ***
Library  commands.py
Library  OperatingSystem
Library  Collections
*** Test Cases ***
test2
    ${output}=  hello   a
    log to console  ${output}
*** Keywords ***
hello
    [Arguments]  ${var}
    ${output}=  test    a
    [Return]    ${output}