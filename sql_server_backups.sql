DECLARE @MyFileName varchar(1000)
SELECT @MyFileName = (SELECT "C:\Program Files\Microsoft SQL Server\MSSQL12.GIS_EDITING\MSSQL\Backup\TESTING_" + convert(varchar(500),GetDate(),112) + ".bak") 
BACKUP DATABASE [TESTING] TO DISK=@MyFileName
GO
DECLARE @MyFileName varchar(1000)
SELECT @MyFileName = (SELECT "C:\Program Files\Microsoft SQL Server\MSSQL12.GIS_EDITING\MSSQL\Backup\PRODUCTION_" + convert(varchar(500),GetDate(),112) + ".bak") 
BACKUP DATABASE [PRODUCTION] TO DISK=@MyFileName
GO
DECLARE @MyFileName varchar(1000)
SELECT @MyFileName = (SELECT "C:\Program Files\Microsoft SQL Server\MSSQL12.GIS_EDITING\MSSQL\Backup\NG_911_TESTING_" + convert(varchar(500),GetDate(),112) + ".bak") 
BACKUP DATABASE [NG_911_TESTING] TO DISK=@MyFileName
GO