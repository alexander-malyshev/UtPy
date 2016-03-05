from cx_Freeze import setup, Executable


setup(
    name = "UtPy",
    version = "0.01",
    description = "Useful scripts which are written in python language",
    executables = [Executable("DeltaPrepare.py"), Executable("CodeCount.py"), Executable("TwoWaySync.py")]
)