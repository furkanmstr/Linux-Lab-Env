import os
import pwd
import grp

from .output import check_result


def check_file(path: str) -> bool:
    result = os.path.isfile(path)
    return check_result(f"File exists: {path}",result)
    

def check_directory(path: str) -> bool:
    result = os.path.isdir(path)
    return check_result(f"Directory exists: {path}",result)


def check_user(username: str) -> bool:
    try:
        pwd.getpwnam(username)
        result  = True
    except KeyError:
        result  = False

    return check_result(f"User '{username}' exists", retult)


def check_group(groupname: str) -> bool: 
    try:
        grp.getgrnam(groupname)
        result  = True
    except KeyError:
        result  = False

    return check_result(f"Group '{groupname}' exists", result)

def check_group_membership(username: str, groupname: str) -> bool:
    try:
        user    = pwd.getpwnam(username)
        group   = grp.getgrnam(groupname)
        
        result  = (username in group.gr_mem
        or user.pw_gid == group.gr_gid)

    except KeyError:
        result  = False

    return check_result(f"'{username}' is member of '{groupname}'",
        result
    )

def check_exact_permission(path: str, expected: str) -> bool:
    try:
        actual  = oct(os.stat(path).st_mode & 0o777)[2:]
        result  = actual == expected

    except FileNotFoundError:
        result  = False

    return check_result(f"Permissions on {path} : {expected}",result)

def check_owner(path: str, expected: str) -> bool:
    try:
        file_stat   = os.stat(path)
        owner       = pwd.getpwuid(file_stat.st_uid).pw_name

        result      = owner == expected
    
    except (FileNotFoundError, KeyError):
        result      = False

    return check_result(f"Owner of {path}: {expected}",result)

def check_file_content(path: str, expected: str) -> bool:
    try: 
        content = open(path).read()
        result  = expected in content

    except (FileNotFoundError, PermissionError):
        result  = False

    return check_result(f"Content of {path} contains '{expected}'",result)
