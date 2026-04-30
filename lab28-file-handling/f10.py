# using pathlib

from pathlib import Path

current_path = Path("C:\AT\at_2025\py\lab28-file_handling")

# To check that whether this file exist or not
print(" is file exist : ",current_path.exists())
print(f"is current file is a dir or files : {current_path.is_file()}")
print(f"is current file is a dir or files : {current_path.is_dir()}")
