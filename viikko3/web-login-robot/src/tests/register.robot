*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Click Link  Register new user
    Register with  gordon123  gordon123  gordon123
    Register Should Succeed

Register With Too Short Username And Valid Password
    Click Link  Register new user
    Register with  st  stanley123  stanley123
    Register Should Fail With Message  Too short username, use at least 3 characters

Register With Valid Username And Too Short Password
    Click Link  Register new user
    Register with  stanley  stanle1  stanle1
    Register Should Fail With Message  Too short password, use at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Click Link  Register new user
    Register with  stanley  stanley123  stanley456
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Click Link  Register new user
    Register with  barney  barney123  barney123
    Register Should Succeed
    Go To Main Page
    Click Link  Login
    Login With  barney  barney123
    Login Should Succeed

Login After Failed Registration
    Click Link  Register new user
    Register with  stanley  st  st
    Register Should Fail With Message  Too short password, use at least 8 characters
    Go To Main Page
    Click Link  Login
    Login With  stanley  st
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register with
    Register Page Should Be Open
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password_confirmation  ${password_confirmation}
    Submit Register

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

Reset Application And Go To Main Page
    Reset Application
    Go To Main Page
