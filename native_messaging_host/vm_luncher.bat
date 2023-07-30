@echo off

set "ssh_key=path/to/your_ssh_key.ppk"
set "ip_address=%~1"

if "%ip_address%"=="" (
    echo Error: IP address not provided.
    exit /b 1
)

start "" "putty.exe" -ssh -i "%ssh_key%" ubuntu@%ip_address%
