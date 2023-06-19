# Imports
import os
import json
import sys
import validators
# Imports END

# ENV Variables
try:
    server = str(os.environ['SMB_SERVER'])
    share = str(os.environ['SMB_SHARE'])
    user = str(os.environ['SMB_USER'])
    password = str(os.environ['SMB_PASSWORD'])
    mountPath = str(os.environ['SMB_MOUNT_PATH'])
except:
    print("Missing some SMB_* env variables")
    print("SMB_SERVER, SMB_SHARE, SMB_USER, SMB_PASSWORD, SMB_MOUNT_PATH")
    sys.exit(1)
# ENV Variables END

# Logic
# Create mount path if it doesn't exist
#if not os.path.exists(mountPath):
#    os.makedirs(mountPath)
# Create string for umount
umountString = 'umount ' + mountPath
# Create string for mount
smbMountString = 'mount -t cifs -o username=' + user + ',password=' + password + ' //' + server + '/' + share + ' ' + mountPath
print('Running command: {}'.format(smbMountString))
# Check if smb command is successful
os.system(umountString)
os.system(smbMountString)
if os.path.ismount(mountPath):
    print('Successfully mounted {} to {}'.format(share, mountPath))
else:
    print('Failed to mount {} to {}'.format(share, mountPath))
    sys.exit(1)
# Logic END
