import os

os.system("pyinstaller --onefile --icon=icon.ico server.py")

pa = f"{os.getcwd()}\dist\server.exe"
path = pa.replace('\\', '\\\\')

text = f'''Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\Localhost File Sharing]
@="&Open Localhost"
"Icon"="{path}"

[HKEY_CLASSES_ROOT\Directory\Background\shell\Localhost File Sharing\command]
@="{path}"
'''

with open("temporary.reg", "w") as tf:
          tf.write(text)

os.system("temporary.reg")
os.remove("temporary.reg")
