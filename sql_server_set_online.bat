REM Sets SQL Server Instances online in the event that McAfee knocks them offline.
echo off
sqlcmd -S MACHINENAME\INSTANCE -i ~\set_online.sql
