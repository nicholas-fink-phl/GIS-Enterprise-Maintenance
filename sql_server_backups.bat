echo off
sqlcmd -S MACHINENAME\INSTANCE -i "~\backups.sql" >>~backups_log.txt 2>&1