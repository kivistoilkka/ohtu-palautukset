*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Click Link  Register new user
    Set Username  stanley
    Set Password  stanley123
    Set Password_confirmation  stanley123
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Click Link  Register new user
    Set Username  st
    Set Password  stanley123
    Set Password_confirmation  stanley123
    Submit Register
    Register Should Fail With Message  Too short username, use at least 3 characters

Register With Valid Username And Too Short Password
    Click Link  Register new user
    Set Username  stanley
    Set Password  stanle1
    Set Password_confirmation  stanle1
    Submit Register
    Register Should Fail With Message  Too short password, use at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Click Link  Register new user
    Set Username  stanley
    Set Password  stanley123
    Set Password_confirmation  stanley456
    Submit Register
    Register Should Fail With Message  Passwords do not match


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Register
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}
