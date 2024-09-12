"""
Desc: service for working with patients data
"""

import datetime
import asyncio

from database.documents import PatientDoc
from shared.constants import WEEKDAYS


async def add_patient(
    name: str,
    dob: datetime.date,
) -> dict:
    """
    Adds new patient to database.

    ...

    Parameters
    ----------
    name : str
        Full name of new patient
    dob : date
        Date of birth for the new patient

    Returns
    -------
    Patient
    """
    today = datetime.date.today()
    obj = PatientDoc(
        name=name,
        dob=dob,
        weekday=WEEKDAYS[today.weekday()],
    )
    await obj.save()
    return obj


async def get_patients_for_today() -> list[dict]:
    """
    Fetch patients for a given date.

    ...

    Parameters
    ----------
    date : date
        Date when patients came in

    Returns
    -------
    Patients List
    """
    return await PatientDoc.find_many(
        {
            "weekday": WEEKDAYS[datetime.date.today().weekday()],
        }
    ).to_list()


async def get_patients_per_weekday() -> dict[str, int]:
    """
    Fetch patients for a given date.

    ...

    Returns
    -------
    Map
    """
    users_per_weekdays = (await asyncio.gather(
        *[PatientDoc.find_many({"weekday": w}).count() for w in WEEKDAYS]
    ))
    return dict(zip(WEEKDAYS, users_per_weekdays))
