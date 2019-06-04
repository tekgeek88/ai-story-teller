def get_file_contents(*args: str) -> str:
    """Reads all of the files from the given list and combines them into one large string
        representing the concatenation of the files.

    Args:
        args: (list) Takes a list of files to be read

    Returns
        :returns a string of the concatenated files in order from first to list

    """

    filecontent = list()
    for file in args:
        with open(file, 'r') as filehandle:
            filecontent.append(filehandle.read().replace('\n', ' '))
    if len(filecontent) > 1:
        return ' '.join(filecontent)
    else:
        return ''.join(filecontent)


