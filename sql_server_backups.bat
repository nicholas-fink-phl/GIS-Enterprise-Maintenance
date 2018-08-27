REM Batch file to run the SQL to create backups as a scheduled task with SQL Server Express.
echo off
sqlcmd -S MACHINENAME\INSTANCE -i "~\backups.sql" >>~backups_log.txt 2>&1
