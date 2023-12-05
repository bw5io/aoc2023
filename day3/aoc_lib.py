def file_to_array(filename, return_int=False, return_matrix=False, allow_empty_line=True):
    output=[]
    openedfile=open(filename)
    flag=False
    while True:
        thisline = openedfile.readline().strip()
        if thisline=='':
            if allow_empty_line==True:
                if flag == True:
                    break
                else:
                    flag = True
            else:
                break
        if return_int==True and thisline.isnumeric():
            thisline=int(thisline)
            flag=False
        elif return_matrix==True:
            thisline=list(thisline)
        output.append(thisline)
    return output

def file_to_array_no_strip(filename, return_int=False):
    output=[]
    openedfile=open(filename)
    flag=False
    while True:
        thisline = openedfile.readline()
        if return_int==True and thisline.isnumeric():
            thisline=int(thisline)
            flag=False
        if thisline=='':
            if flag == True:
                break
            else:
                flag = True
        output.append(thisline)
    return output

def file_to_map(filename, sep, return_int=False):
    input_file=file_to_array(filename)
    output=[]
    for i in input_file:
        if i=="":
            break
        if sep=="":
            line=list(i)
        else:
            line=i.split(sep)
        if return_int==True:
            line=[int(element) for element in line]
        output.append(line)
    return output

def add_dict_map(obj, key, value):
    if key in obj:
        obj[key].append(value)
    else:
        obj[key]=[value]

def add_dict(obj, key, value):
    if key in obj:
        obj[key]+=value
    else:
        obj[key]=value