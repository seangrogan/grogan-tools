def auto_mkdir(path):
    """
    Auto-make-directory.  This code block automatically makes folders
    :param path: File with path
    :return: true if successful
    """
    import os, pathlib
    directory, file = os.path.split(path)
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
    return True
