import re


def is_valid_license_plate_old_format(plate: str) -> bool:
    """
    Checks whether a string matches the old format of Brazilian license plate.
    """
<<<<<<< HEAD
    pattern = re.compile(r"^[aA-zZ]{3}[0-9]{3}$")
=======
    pattern = re.compile(r"^[aA-zZ]{3}[0-9]{4}$")
>>>>>>> 174
    return (
        isinstance(plate, str) and re.match(pattern, plate.strip()) is not None
    )
