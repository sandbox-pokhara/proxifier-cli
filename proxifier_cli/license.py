import winreg as wrg


def install_license(license_key, owner):
    key = wrg.CreateKey(wrg.HKEY_CURRENT_USER, r"SOFTWARE\\Initex\\Proxifier\\License")
    wrg.SetValueEx(key, "Key", 0, wrg.REG_SZ, license_key)
    wrg.SetValueEx(key, "Owner", 0, wrg.REG_SZ, owner)
    if key:
        wrg.CloseKey(key)
