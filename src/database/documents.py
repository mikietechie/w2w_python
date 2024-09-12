"""
Desc: Database ORM Models
"""

from __future__ import annotations

import datetime

from beanie import Document


class PatientDoc(Document):
    """
    Patient data model.
    """

    name: str
    dob: datetime.date
    weekday: str

    def __str__(self):
        return str(self.name)


DOCUMENT_MODELS = [
    PatientDoc,
]
