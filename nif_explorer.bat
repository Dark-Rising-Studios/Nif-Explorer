@echo off

if %python_path% == "" (
echo. Please set the Python path!
goto end
)

if "%1" == "" (
echo. No parameters passed!
SHIFT
goto end
)

goto runpython


:runpython

echo. 
python.exe %1
echo. 

:end