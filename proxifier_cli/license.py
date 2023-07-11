import winreg as wrg


def install_license(key, owner):
    location = wrg.HKEY_CURRENT_USER
    soft = wrg.OpenKeyEx(location, r"SOFTWARE\\")
    key = wrg.CreateKey(soft, "Initex\\Proxifier\\License")
    wrg.SetValueEx(key, "Key", 0, wrg.REG_SZ, key)
    wrg.SetValueEx(key, "Owner", 0, wrg.REG_SZ, owner)
    if key:
        wrg.CloseKey(key)
