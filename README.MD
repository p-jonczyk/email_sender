## INSTALLATION

**pip install -r *requirements.txt***
<br />

## ABOUT

Program *(bulk e-mail sender)* allows user to upload excel file *(.xlsx)* which contains columns *'email' and 'message'* and send them via gmail account.
<br />

*My second project with use of Flask, HTML and CSS*
<br />

## KEY INFO

**Detailed informations are presented on HOW TO site**
<br />

- Turn off google's *2-Step Verification* and *Less secure apps & your Google Account* (therefore better not to use your private account)
<br />

- make sure your excel file contains *'email' and 'message'* columns
<br />

- amount of mails per day is set by Google - 500 *(https://support.google.com/a/answer/166852?hl=en#zippy=)*
<br />

## HOW TO
1. Download project / clone git. 
2. Open *cmd/powershell* with project's directory.
3. Make sure you made **INSTALLATION** step.
4. Command: *flask run* 
5. Open shown address. **REMEMBER TO CHECK 'HOW TO...' SITE (/how_to)**
6. Play around
<br />

## TESTS

To run tests install **pip install -r requirements_test.txt**
<br />

1. Open terminal in main directory and type *'flask run'* 
2. Type *'cd test'* to change directory
3. Type *'pytest .*' to run all 12 tests or *'pytest **modul_name.py**'* to run specific module tests
4. To see each test in real time add *'--demo'* at the end of mentioned commends


Tests are performed with selenium-base *(https://pypi.org/project/seleniumbase/)*.
<br />

## TEST SCENARIO 

### 1. UPLOAD FILE 
**Scope**: Test upload file mechanism.  
**Action**: User uploads file and submit it.  
**Test Notes and Preconditions**: Open main page.
**Verification Steps**: There occurred redirection or not, depends on valid or invalid upload.
| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 1.1 | No file choosen  | 1. Click *SUBMIT* button | No redirection occurred and message appears|
| 1.2 | Invalide file extension choosen  | 1. Uploads invalide file format <br /> 2. Click *SUBMIT* button | No redirection occurred and message appears |
| 1.3 | Valid file extension choosen  | 1. Uploads valide file format <br /> 2. Click *SUBMIT* button | Redirection occurred and credential form is shown |
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |

### 2. DATA VERIFICATION
**Scope**: Verify uploaded data.  
**Action**: Uploaded file.  
**Test Notes and Preconditions**: Displays *possible errors* and *data table*.  
**Verification Steps**: Checks if any *possible errors* and *data table* are shown.
| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 2.1 | Valid data file uploaded | None | *POSSIBLE ERRORS* field is empty and data are shown in table below| <br />
| 2.2 | Invalid data file uploaded | None | *POSSIBLE ERRORS* field is filled with invalid data and all data are shown in table below|
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |

### 3. SEND RESPONSE 
**Scope**: Test send mechanism.  
**Action**: User enter credentials and click *SENT MAIL* button.  
**Test Notes and Preconditions**: File is uploaded and credential form is shown.  
**Verification Steps**: There occurred redirection or not, depends on valid or invalid credentials. In addition, redirection may show *fail* or *success* message.
| #                   | Action           | Test case procedure | Expected result |
| ------------- | ------------- |  ------------- |  ------------- | 
| 3.1 | All form fields are empty  |1. User doesn't enter any credentials <br /> 2. Click *SEND MAILS* button | No redirection occurred and message appears| <br />
| 3.2 | Password is left empty  |1. User doesn't enter password <br /> 2. Click *SEND MAILS* button | No redirection occurred and message appears| <br />
| 3.3 | Gmail address is left empty  |1. User doesn't enter gmail address <br /> 2. Click *SEND MAILS* button | No redirection occurred and message appears| <br />
| 3.4 | Invalid gmail address  |1. User enters invalid gmail address <br /> 2. Click *SEND MAILS* button | Redirection occurred and message **fail** appears| <br />
| 3.5 | Invalid password  |1. User enters invalid password <br /> 2. Click *SEND MAILS* button | Redirection occurred and message **fail** appears| <br />
| 3.6 | Valid credentials and data set |1. User uploads valid data set <br /> 2. User enters valid credentials <br /> 3. Click *SEND MAILS* button | Redirection occurred and message **success** appears| <br />
| 3.7 | Valid credentials and invalid data set |1. User uploads invalid data set <br /> 2. User enters valid credentials <br /> 3. Click *SEND MAILS* button | Redirection occurred and message **fail** appears| <br />
| <img width=100/> | <img width=200/> |  <img width=500/> |  <img width=200/> |