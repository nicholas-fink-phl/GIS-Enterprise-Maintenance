REM Sets SQL Server instances online in the event that McAfee knocks them offline.
echo off
sqlcmd -S MACHINENAME\INSTANCE -i ~\set_online.sql
