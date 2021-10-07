import pandas as pd
from os import remove, listdir
import const
import json


def excel_to_json(filepath: str):
    """Takes excel (.xlsx) file and convert it into .json

    Parameters:
        filepath: full path off excel file
        email_column: title of e-mails column from .csv
        msg_column: title of messages column from .csv

    Returns:
        JSON"""

    excel_data = pd.read_excel(filepath)
    json_data = excel_data.to_json()
    json_final = json.loads(json_data)
    # remove(filepath)

    return json_final


def allowed_file(filename: str) -> bool:
    """Checks if file with allowed extension

    Parameters:

    filename: path of file

    coder_type: 'decoder' or 'encoder' """

    return '.' in filename and filename.rsplit('.', 1)[1].lower() in const.allow_extensions


def clean_uploads(upload_folder) -> None:
    """Clears UPLOAD_FOLDER before uploading new file"""
    filearr = listdir(upload_folder)
    for file in filearr:
        filepath = f'{upload_folder}/{file}'
        remove(filepath)


def get_filepath(upload_folder: str) -> str:
    """Gets filepath - UPLOAD_FOLDER/<file>"""
    filepath = f'{upload_folder}/{listdir(upload_folder)[0]}'

    return filepath
