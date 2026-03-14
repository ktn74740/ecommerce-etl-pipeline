from pathlib import Path



def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent

def get_data_dir() -> Path :
    data_dir = get_project_root()/"data"
    data_dir.mkdir(exist_ok=True)
    return data_dir

def get_output_path(filename: str) -> Path:
    return get_data_dir()/filename

