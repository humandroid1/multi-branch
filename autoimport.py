import sys
import os
import datetime
import pip
import pkg_resources
built_in_mod = sys.modules
print(built_in_mod.keys())
print("***************")
pkgs = []
pkgs1=[]
installed = [pkg.key for pkg in pkg_resources.working_set]
print(installed)
print("****************")
for a,b,c in os.walk('/home/ec2-user/vish):
    for files in c:
        with open(files) as f:
            for lines in f:
                if "import" in lines and "#" not in lines:
                    tmp = lines.split("import")
                    if tmp[-1].strip() not in built_in_mod and (tmp[-1].strip()).lower() not in installed:
                        pkgs.append((tmp[-1].strip()))
if len(pkgs) is not 0:
    print(pkgs)
    pip.main(['install'] + pkgs)
    print("******************")
else:
    print("All the Packages are installed...You are Good to go...")

