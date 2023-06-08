$USER = Get-LocalUser -Name $env:USERNAME
$BASE_PATH = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Creative\"
$EXTENDED_PATH = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Creative\".Insert($BASE_PATH.Length, $USER.SID.ToString())
$ASSET_PATH_LIST = Get-ChildItem -Path $EXTENDED_PATH -Recurse | Get-ItemPropertyValue -PSProperty 'landscapeImage'
$DEST = New-Item -Path $ENV:TEMP -Name (New-Guid) -ItemType Directory -Force
foreach ($asset_path in $ASSET_PATH_LIST) {
    Copy-Item -Path $asset_path -Destination $DEST.FullName
}
Get-ChildItem -Path $DEST.FullName | Rename-Item -NewName { $_.BaseName + '.jpg' }
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name 'WallPaper' -Type String -Value '<Image Path>'
