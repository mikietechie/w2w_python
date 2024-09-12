"""
Desc: Patients Bot routes
"""
import datetime

from aiogram import (
    types,
    filters,
    Router,
)
from aiogram_forms import dispatcher
from aiogram_forms.forms import (
    Form,
    fields,
    FormsManager,
)

from services.patients import (
    add_patient,
    get_patients_for_today,
    get_patients_per_weekday,
)
from shared.logger import logger
from shared.constants import UNDERLINE
from telegram.validators.patients import age_validator

router = Router(name=__name__)

ADD_CMD = types.BotCommand(
    command="add_patient",
    description="Add Patient",
)
TODAY_CMD = types.BotCommand(
    command="today",
    description="Today's Patients",
)
PERDAY_CMD = types.BotCommand(
    command="perday",
    description="Perday Patients",
)
COMMANDS = [
    ADD_CMD,
    TODAY_CMD,
    PERDAY_CMD,
]

PATIENT_FORM = "patient-form"


@dispatcher.register(PATIENT_FORM)
class PatientForm(Form):
    """
    Add patient form
    """

    name = fields.TextField(
        "Name i.e John Doe",
        min_length=2,
        validators=[],
    )
    dob = fields.TextField(
        "DOB i.e 28.02.1977",
        min_length=2,
        validators=[age_validator],
    )
    confirm = fields.TextField(
        "Type 'yes' if the data is correct",
        min_length=2,
        validators=[],
    )

    @classmethod
    async def callback(
        cls,
        message: types.Message,
        forms: FormsManager,
        **data,
    ) -> None:
        """
        Handle add patient on submit
        """
        data = await forms.get_data(PATIENT_FORM)
        if data.get("confirm") != "yes":
            return await message.answer(
                text="You cancelled.\n\n/add_patient",
                reply_markup=types.ReplyKeyboardRemove(),
            )
        doc = await add_patient(
            name=data.get("name"),
            dob=datetime.datetime.strptime(data.get("dob"), "%d.%m.%Y").date(),
        )
        await doc.save()
        await message.answer(
            text=f"{doc} been saved!\n\n/add_patient",
            reply_markup=types.ReplyKeyboardRemove(),
        )


@router.message(filters.Command(commands=[ADD_CMD.command]))
async def add_patient_handler(
    message: types.Message,
    forms: FormsManager,
) -> None:
    """
    Handles add patient cmd.
    """
    logger.info("Add patient %s", message)
    await forms.show(PATIENT_FORM)


@router.message(filters.Command(commands=[TODAY_CMD.command]))
async def todays_patients_handler(
    message: types.Message,
) -> None:
    """Read todays patients"""
    logger.info("Todays patients %s", message)
    docs = await get_patients_for_today()
    text = f"{len(docs)} documents found\n\n" + f"\n{UNDERLINE}\n".join(
        [(f"{doc.name}\n{doc.dob}\n") for doc in docs]
    )

    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(filters.Command(commands=[PERDAY_CMD.command]))
async def patients_per_day_handler(
    message: types.Message,
) -> None:
    """Read patients day"""
    logger.info("Read Stats %s", message)
    data = await get_patients_per_weekday()
    text = f"\n{UNDERLINE}\n".join(
        [f"{weekday:10}: {number}" for (weekday, number) in data.items()]
    )

    await message.answer(
        text=text,
        reply_markup=types.ReplyKeyboardRemove(),
    )
