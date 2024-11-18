*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Confirmation Password  pekka123
    Submit Registration
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  p
    Set Password  pekka123
    Set Confirmation Password  pekka123
    Submit Registration
    Register Should Fail With Message  The username has to be at least three characters long

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  p
    Set Confirmation Password  p
    Submit Registration
    Register Should Fail With Message  The password has to be at least eight characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  pekka
    Set Password  pekkaabc
    Set Confirmation Password  pekkaabc
    Submit Registration
    Register Should Fail With Message  The password has to have at least one character that is not a letter

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  pekka123
    Set Confirmation Password  pekka1234
    Submit Registration
    Register Should Fail With Message  The given passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  pekka123
    Set Confirmation Password  pekka123
    Submit Registration
    Register Should Fail With Message  The username is already in use

Login After Successful Registration
    Set Username  pekka
    Set Password  pekka123
    Set Confirmation Password  pekka123
    Submit Registration
    Welcome Page Should Be Open
    Click Link  Continue to main page
    Main Page Should Be Open
    Click Button  Logout
    Login Page Should Be Open
    Set Username  pekka
    Set Password  pekka123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  p
    Set Password  pekka123
    Set Confirmation Password  pekka123
    Submit Registration
    Register Page Should Be Open
    Click Link  Login
    Login Page Should Be Open
    Set Username  p
    Set Password  pekka123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page