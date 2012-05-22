@echo off

if %python_path% == "" (
echo. Please set the Python path!
goto end
)

if "%1" == "" (
goto displayparams
)

if "%1" == "-help" (
goto helpcommands
)

set file=empty
set block=empty
set property=empty
set searchPath=empty
set resultPath=empty
set global_index=0

goto checkparams

:checkparams

set SWITCHPARSE=%1

if "%SWITCHPARSE%" == "" ( goto run )

for /F "tokens=1,2 delims=@ " %%a IN ("%SWITCHPARSE%") DO SET SWITCH=%%a&set VALUE=%%b

if "%SWITCH%" == "-file" (
set file=%VALUE%
SHIFT
goto checkparams
)

if "%SWITCH%" == "-block" (
set block=%VALUE%
SHIFT
goto checkparams
)

if "%SWITCH%" == "-property" (
set property=%VALUE%
SHIFT
goto checkparams
)

if "%SWITCH%" == "-searchPath" (
set searchPath=%VALUE%
SHIFT
goto checkparams
)
echo. %VALUE%
if "%SWITCH%" == "-resultPath" (
set resultPath=%VALUE%
SHIFT
goto checkparams
)


rem **************
rem This is where we run our python
rem **************

:run
if "%file%" == "empty" (
goto runconsole
) else (
goto runpython
)

:runconsole

if "%block%" == "empty" (
goto exit
)

echo. 
if not "%block%" == "empty" (

	if not "%property%" == "empty" (
		
		if "%global_index%" == "0" (
		
		)
	)
		if not "%searchPath%" == "empty" (
		
			if not "%resultPath%" == "empty" (
				python.exe explorer_console.py %block% %property% %searchPath% %resultPath%
				goto end
			) else (
				python.exe explorer_console.py %block% %property% %searchPath%
				goto end
			)
			
		) else (
			python.exe explorer_console.py %block% %property%
			goto end
		) 
		
	) else (
		python.exe explorer_console.py %block%
	)
goto end
)

set block=empty
set property=empty
set searchPath=empty
set resultPath=empty

goto end


:runpython

python.exe %file%
set file=empty
goto end


:displayparams
    echo.nif_explorer.bat 
    echo.   Flags: -file, -block, -property, -searchPath, -resultPath 
    echo.   Optional: None
    echo.   Types -help [parameter] for additional help.
    echo.
    goto end

:helpcommands

if "%2" == "-file" (
echo.
echo. -file is used to set the Nif Explorer to run a .py file created by the user.
echo. [Usage: -file@look_for_ninodes.py]
echo.
)

if "%2" == "-block" (
echo.
echo. -block is used to set the nif block type to search for in the nif files
echo. [Usage: -block@NiNode]
echo. [Required_Param: None]
echo.
)

if "%2" == "-property" (
echo.
echo. -property is used to search for a specific property of the '-block' type.
echo. [Usage: -property@num_children]
echo. [Required_Param: -block]
echo.
)

if "%2" == "-searchPath" (
echo.
echo. -searchPath is used to define the search path containing the nif files.
echo. [Usage: -property@num_children]
echo. [Required_Param: -block -property]
echo.
)

if "%2" == "-resultPath" (
echo.
echo. -resultPath is used to define the result path, if none is defined
echo. -a default result directory is created in the root folder.
echo. [Usage: -resultPath@results]
echo. [Usage: -resultPath@results/nifs] -folder 'resulst' must exsist to create nifs
echo. [Required_Param: -block -property -searchParh]
echo.
)



goto end

:exit
echo. No parameters parsed, type -help [arg] for a list of parameters.
goto end

:end