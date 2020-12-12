import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)


def main():
    access_token = 'Pl3cE6QGLAcAAAAAAAAAAc9oODCYrgwkhwI1ziFX90SsqaLX0U3r_up_4D8JfEJb'
    transferdata = TransferData(access_token)

    file_from = input("Enter the file path to transfer")
    file_to = input("Enter the full path to upload to the dropbox")

    transferdata.upload_file(file_from,file_to)
    print("File has been moved")
main()    
