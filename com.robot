*** Settings ***
Library     sample.py
Library     sample1.py
Library     Collections
*** Keywords ***
hello1
    [Arguments]  ${var2}
    ${output1}=  ram1  a2
    [Return]    ${output1}
# hello
#     [Arguments]  ${var}
#     ${output}=  test1  a
#     [Return]    ${output}
*** Test Cases ***
# test1
#     ${output}=  hello  a
#     log to console  ${output}

test2
    ${output1}=  hello1  a2
    Should be equal  ${output1}  ${0}


