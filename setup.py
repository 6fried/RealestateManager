from distutils import version
from cx_Freeze import setup, Executable

setup(
	name="Locatia",
	version="1.0",
	description="Gérez plus facilement votre agence immobilière",
	executables=[Executable("main.py", base = "Win32GUI")],
)