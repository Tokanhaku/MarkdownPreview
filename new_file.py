import os
import subprocess as sp
from urllib.parse import quote

def process_path(file_path):
    '''
    input: string: file path
    output: 3 strings: tilda path, full path, encoded url path
    '''
    homepath = os.path.expanduser("~")
    if file_path[0] == "~":
        tilda_path = file_path
        full_path  = homepath + file_path[1:]
    elif file_path[:len(homepath)] == homepath:
        tilda_path = "~"+ file_path[len(homepath):]
        full_path  = file_path
    else:
        tilda_path = file_path
        full_path  = file_path
    encoded_url_path = "file://" + quote(full_path)
    return tilda_path, full_path, encoded_url_path

def lb_notification(title, file_path):
    my_env = os.environ.copy()
    my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]
    tilda_path, full_path, encoded_url_path = process_path(file_path)    
    my_command = ["osascript", "new_file_lb_notification.scpt", \
                    title, tilda_path, encoded_url_path]
    sp.check_output(my_command, env=my_env)
