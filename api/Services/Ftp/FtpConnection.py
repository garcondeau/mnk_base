import ftplib
import os.path


class FtpConnection:
    def __init__(self, host, username, password):
        self.host = host
        print(f'Connecting to {host}')
        self.ftp = ftplib.FTP(host)
        self.ftp.login(username, password)

    def upload_file(self, local_file, remote_folder, remote_sub_folder):
        name, extension = os.path.splitext(local_file)
        self.ftp.cwd(remote_folder)
        if remote_sub_folder not in self.ftp.nlst():
            self.ftp.mkd(remote_sub_folder)
        with open(local_file, 'rb') as f:
            self.ftp.storbinary(f'STOR /{remote_folder}/{remote_sub_folder}/export{extension}', f)
        self.ftp.quit()
        print(f'File Uploaded to ftp://{self.host}/{remote_folder}/{remote_sub_folder}/export{extension} ...')

    def download_file(self, remote_file, local_file):
        print('Downloading file from : {}\n'.format(local_file))
        with open(local_file, "wb") as f:
            self.ftp.retrbinary("RETR " + remote_file, f.write)
        self.ftp.quit()
        print(f'\nFile downloaded ftp://{self.host}/{remote_file} ... to {local_file}\n')
