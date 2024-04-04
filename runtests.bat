@echo off
rem Activate the virtual environment (if you are using one)
call venv\Scripts\activate

rem Run Behave tests with specified options
behave -f pretty -o test-results

rem Deactivate the virtual environment (if activated)
deactivate
