import os

ODBC_DRIVER = os.getenv("ODBC_DRIVER", "{ODBC Driver 17 for SQL Server}")
SERVER      = os.getenv("SQLSERVER", "")   # SERVER
DATABASE    = os.getenv("SQLDB", "Tesis")
USER        = os.getenv("SQLUSER", "")
PASSWORD    = os.getenv("SQLPWD", "")

connection_string = (
    f"DRIVER={ODBC_DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USER};"
    f"PWD={PASSWORD};"
    "TrustServerCertificate=yes;"
)
