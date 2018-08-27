# cleans up metadata in an enterprise gdb
import os
import sys
import shutil
import arcpy
from datetime import datetime

start = datetime.now()

if arcpy.GetLogHistory():
    arcpy.SetLogHistory(False)

install_dir = arcpy.GetInstallInfo()['InstallDir']

ss1 = 'Metadata\\Stylesheets\\gpTools\\remove geoprocessing history.xslt'
ss2 = 'Metadata\\Stylesheets\\gpTools\\remove local storage info.xslt'
ss3 = 'Metadata\\Stylesheets\\gpTools\\remove empty elements.xslt'

sspath1 = install_dir + ss1
sspath2 = install_dir + ss2
sspath3 = install_dir + ss3

outXML = 'c:\\XML_out'
if os.path.exists(outXML):
    shutil.rmtree(outXML)
os.mkdir(outXML)

sde = 'Database Connections\GIS_gis_sde.sde'
conn = arcpy.ArcSDESQLExecute(sde)
sql = '''select owner, table_name from layers order by owner, table_name'''
query = conn.execute(sql)

for x in query:
    fc = str(x[0])+'.'+str(x[1])
    print(fc)
    acct = x[0]
    conn_file = 'Database Connections' + os.sep + 'GIS_' + str(acct) + '.sde'
    print(conn_file)
    try:
        nameXml1 = outXML + os.sep + x[1] + '1.xml'
        nameXml2 = outXML + os.sep + x[1] + '2.xml'
        nameXml3 = outXML + os.sep + x[1] + '3.xml'
        arcpy.XSLTransform_conversion(conn_file + os.sep + x[1], sspath1, nameXml1, '')
        arcpy.MetadataImporter_conversion(nameXml1, conn_file + os.sep + x[1])
        arcpy.XSLTransform_conversion(conn_file + os.sep + x[1], sspath2, nameXml2, '')
        arcpy.MetadataImporter_conversion(nameXml2, conn_file + os.sep + x[1])
        arcpy.XSLTransform_conversion(conn_file + os.sep + x[1], sspath3, nameXml3, '')
        arcpy.MetadataImporter_conversion(nameXml3, conn_file + os.sep + x[1])
        print('complete')
    except:
        print('something broke...')
        continue

shutil.rmtree(outXML)

total = datetime.now() - start

print('Completed in ' + str(total) + ' minutes.')
