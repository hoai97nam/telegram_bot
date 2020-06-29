@echo THIS IS TEST CASE FOR ADDING MEMBER BY DOUBLE CLICK ON A BATCH FILE
@echo PURPOSE: Adding member to Telegram group
@echo Author: Ng-H Nam
@echo Project: Telegram Bot
@echo Description: Automatically, run adding functions in each terminal
@echo ------------------------------------------------------------------     
echo           
                        
@echo Principle:
@echo 1. Name of element files must be the same format
@echo 2. Element files file must be in the same folder
@echo 3. Consider your resources when multiple adding functions conducted
echo

REM set /p var1="Enter number of add file: "
REM set /p var2="Insert py file that you want to use: "
@echo off
for /l %%x in (1,1,3) do (
    start cmd.exe /k python halo%%x.py nam%%x.csv
)
REM for /l %%x in (1,1,3) do (
REM     start cmd.exe /k python halo%%x.py
REM )
@echo ON


pause >nul
