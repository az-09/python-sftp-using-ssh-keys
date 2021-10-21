import os
from pathlib import Path
from typing import List

import pysftp
from dotenv import load_dotenv

load_dotenv()

def file_list() -> List[str]:
    return [str(path) for path in Path().glob('data/*.*')] # path for all files in data folder

def main():
    sftp_host = os.getenv("SFTP_IPADDRESS")
    sftp_userid = os.getenv("SFTP_USERID")
    sftp_private_key = os.getenv("SFTP_PRIVATE_KEY")
   
    try:
        with pysftp.Connection(host=sftp_host, username=sftp_userid, private_key=sftp_private_key, port=22) as sftp:
            with sftp.cd('sftp'): # target folder
                for file in file_list():
                    sftp.put(file)
                print('Files have been uploaded to sftp successfully.')
    except:
        print('Upload has failed.')

if __name__ == '__main__':
    main()
