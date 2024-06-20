import pathlib


def resolve_file_in_files_dir(filename: str) -> str:
    return str(pathlib.Path(__file__).parent.joinpath('files').joinpath(filename))
