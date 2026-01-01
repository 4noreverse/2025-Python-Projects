filename = input('File name: ').strip()
exten = filename.split('.')[-1]
if exten == 'gif':
    print('image/gif')
elif exten == 'jpg':
    print('image/jpeg')
elif exten == 'jpeg':
    print('image/jpeg')
elif exten == 'png':
    print('image/png')
elif exten.casefold() == 'pdf'.casefold():
    print('application/pdf')
elif exten == 'txt':
    print('text/plain')
elif exten == 'zip':
    print('application/zip')
else:
    print('application/octet-stream')
