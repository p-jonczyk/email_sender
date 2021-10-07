"""Operation on emails and its content """
import re
import const


def get_email_msg(json_sting: str) -> list:
    """Create list of tuples (email, message)

    Parameters:
    json_string: contain 'email' and 'message'

    Returns: list of tuples (email, msg)"""

    record_count = len(json_sting['message'].values())
    email_msg_pairs = []
    for i in range(record_count):
        email_msg_pairs.append(
            (json_sting['email'][str(i)], json_sting['message'][str(i)]))

    return email_msg_pairs


def check_email(email_msg_pairs: list) -> list:
    """Checks if email contains ['@' , '.'] or doesn't contain white spaces.

    Parameters:
    email_msg_pairs: list of tuples (email, message) 

    Returns: 
    list of tuples (index, invalide email)"""

    invalide_emails = []
    for num, data_tuple in enumerate(email_msg_pairs):
        if data_tuple[0] is None:
            invalide_emails.append((num, const.no_email))

        elif not re.fullmatch("[^@]+@[^@]+\.[^@]+[^\s]", str(data_tuple[0])):
            invalide_emails.append(
                (num, f'{data_tuple[0]}  (check email address)'))

        elif data_tuple[1] is None:
            invalide_emails.append((num, const.no_msg))

    return invalide_emails
