-- sets SQL Server databases online if they've been knocked offline, runs from sql_server_set_online.bat
alter database testing set online
go
alter database production set online
go
alter database ng_911_testing set online
go
