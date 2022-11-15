*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  stanley  sekret42
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  sekret42
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  st  sekret42
    Output Should Contain  Too short username, use at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  stanley  sekret4
    Output Should Contain  Too short password, use at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  stanley  Salasana
    Output Should Contain  Password has to include other characters in addition to letters

Register With Username With Upper Case Characters And Valid Password
    Input Credentials  Stanley  sekret42
    Output Should Contain  Username can only have lower case letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123