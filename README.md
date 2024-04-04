# demo_test_project
This is a practice coding test.

## Step1: Project setup
#### 1.	New directory creation  
mkdir demo_test_project<br>
cd demo_test_project<br>
OR<br>
Clone repository<br>
git clone <repository-url>

#### 2.	Initializing new git repo
git init

#### 3.	Virtual environment setup
python -m venv venv<br>
venv\Scripts\activate

#### 4.	Package installation (behave, selenium, behave-x)
pip install behave selenium behavex

## Step2: Write Feature File
Here we will create a ‘.feature’ file (eg. Login.feature) containing gherkins scenarios described in the user story.<br>
I’ve created login.feature file in features folder

## Step3: Step definitions implementation
Here we will implement step definitions for the steps mentioned in our feature file. These step definitions will contain the selenium automation code with behave.<br>
We will also store screenshots of particular steps in screenshots folder.<br>
I’ve created step_definitions.py file inside /features/Steps folder

## Step4: Write Automation Code
Here we will write the automation code using selenium to interact with the website elements and perform actions described in the scenario.<br>
I’ve created automation.py file inside main directory demo_test_project

## Step5: Create Batch File
Here we will create a batch file (e.g runtest.bat) to run our test.<br>
I’ve created batch file inside main directory too.

@echo off<br>
rem Activate the virtual environment (if you are using one)<br>
call venv\Scripts\activate<br>


rem Run Behave tests with specified options<br>
behave -f pretty -o test-results<br>


rem Deactivate the virtual environment (if activated)<br>
deactivate<br>

## Step6: Generate BehaveX Report
BehaveX generates reports automatically. By using behave -f Pretty -o test-results in the batch file, it will generate the BehaveX report.<br>
Report is getting generated inside our main directory.

## Step6: Run the code
*To run acceptance criteria behave test just double click the batch file* OR *In cmd after setting up virtual environment run the behave –f Pretty –o test-results command*<br>
Steps to setup virtual environment through CMD–<br>
1.	Go to directory
2.	Open cmd in that directory
3.	Activate virtual environment<br>
python –m venv venv<br>
venv\Scrips\activate
4.	Run the code<br>
behave –f Pretty –o test-results
5.	After successful test results deactivate the virtual environment<br>
deactivate

##### For more detail understanding you can refer to my documentation.docx file