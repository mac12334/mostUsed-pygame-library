def get_lines(directory: str) -> list[str]:
    with open(directory, "r") as file:
        lines = file.readlines()
    
    for x in range(len(lines)):
        lines[x] = lines[x].strip("\n")
    return lines

def correct_type(val: str):
    match val:
        case "True":
            return True
        case "False":
            return False
        case "None":
            return None
    
    if val.count(",") > 0:
        lst = []
        values = val.split(",")
        if values[-1] == '':
            values.pop()
        for v in values:
            lst.append(correct_type(v))
        return lst
    
    if val.isdigit():
        return int(val)
    try:
        return float(val)
    except ValueError:
        return val
    
def make_dict(line: str, key_val_sep: str, sep: str) -> dict[str, any]:
    pairs = line.split(sep)
    d = {}
    for pair in pairs:
        split = pair.split(key_val_sep)
        d[split[0]] = correct_type(split[1])
    return d

def get_data(file_name: str, key_val_sep: str, sep: str) -> list[dict[str, any]]:
    """get_data

    allows you to convert a text file to a list containing multiple dictionaries
    this can be very useful for game data that needs to be packaged easily into a human readable format

    syntax for data
    int_key=1 str_key=hello-world bool_key=True none_key=None list_key=1,True,hello,None
    level_num=2 display_text=this-is-a-nice-level easy_enabled=False image=None enemies=1,

    print(get_data(file, "=", " "))

    #output [{"int_key"=1, "str_key"="hello-world", "bool_key"=True, "none_key"=None, "list_key"=[1, True, "hello", None]},

    #{"level_num"=2, "display_text"="this-is-a-nice-level", "easy_enabled"=False, "image"=None, "enemies"=[1]}]
    ## Warning - you can only use 1D arrays for this function at this time

    Args:
        file_name - the path to the text file you want to read.
        key_val_sep - this character is used to seperate the keys to their values.
        sep - this character seperates one key value pair to the next.
    
    Returns:
        A list containing dictionaries used for containing data on any application
    """
    lines = get_lines(file_name)
    data = []
    for line in lines:
        data.append(make_dict(line, key_val_sep, sep))
    return data

def make_line(d: dict[str, any], key_val_sep: str, sep: str) -> str:
    """
    Warning this function is only used for another function this is not made for general purpose use
    """
    res = ""
    for key in d:
        if type(d[key]) != list:
            res += key + key_val_sep + str(d[key]) + sep
        else:
            res += key + key_val_sep + convert_list_to_string(d[key]) + sep
    return res[:-1]

def convert_list_to_string(lst: list) -> str:
    """
    Warning this function is used only for another function
    and 1d lists are only supported
    """
    if len(lst) == 1:
        return str(lst[0]) + ","
    else:
        string = ""
        for val in lst:
            string += str(val) + ","
        return string[:-1]

def write_data(file_name: str, data: list[dict[str, any]], key_val_sep: str, sep: str) -> None:
    w = ""
    for x in data:
        w += make_line(x, key_val_sep, sep) + "\n"
    
    w = w[:-1]
    with open(file_name, "w") as file:
        file.write(w)