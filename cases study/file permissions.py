read=9
write=3
execute=1
permissions=read|write
print("permission value:",permissions)
if permissions & write:
    print("permission is set")
else:
    print("permission is not set")
    
output:
    permission value: 11
permission is set
