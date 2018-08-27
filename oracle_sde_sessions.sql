SELECT DISTINCT a.owner AS table_owner,
  a.table_name,
  b.LOCK_TIME,
  c.owner                             AS connection_owner,
  regexp_substr(c.nodename, '^[^:]+') AS machine,
  CASE
    WHEN c.nodename LIKE '%:%'
    THEN regexp_substr(c.nodename, '[^:]+$')
    ELSE NULL
  END AS version,
  d.program,
  upper(d.osuser) AS AD_USER
FROM table_registry a
RIGHT JOIN table_locks b
ON a.REGISTRATION_ID = b.REGISTRATION_ID
RIGHT JOIN process_information c
ON b.sde_id = c.sde_id
RIGHT JOIN v$session d
ON c.SERVER_ID                            = regexp_substr(d.process, '^[^:]+')
WHERE regexp_substr(c.nodename, '^[^:]+') = d.TERMINAL
ORDER BY a.owner,
  a.table_name;