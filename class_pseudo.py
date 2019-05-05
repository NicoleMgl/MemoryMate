from datetime import date
from typing import List


class Contact:
    """A page that allows you to add an instance of a User's contacts.
    Will also display all instances of the contact."""

    def new_contact(self):
        """Add a contact to the User."""
        name_field = str(input())
        bday_field = input()
        age_field = int(input())
        relate_field = input()
        likes_field = str(input())

        People(name_field, bday_field, age_field, relate_field,
               likes_field)


class User:
    """A person on the Memory Mate app."""
    birthday: date  # MM-DD
    name: str
    # nicknames: Optional[List]
    age: int

    def __init__(self, name, birthday, age):
        self.name = name
        self.birthday = birthday
        self.age = age


class People(User):
    """ A contact of the User. """
    relationship: str
    likes: str

    def __init__(self, name, birthday, age, relate, likes):
        User.__init__(self, name, birthday, age)
        self.relationship = relate
        self.likes = likes


class JournalPage:
    """A page with a new entry and the past entries. """
    # self.past_entries: [NewJournal]

    def __init__(self):
        self.past_entries = List[NewJournal]

class NewJournal:
    """A new entry in the journal. """
    self.date: date
    self.text: str

    def __init__(self, datetime, text):

        self.date = datetime.date
        self.text = text
        JournalPage.past_entries.append(self)


class SettingsPage:
    """A screen with four settings.
    Volume: adjusts volume in app.
    Language: changes language.
    Notifications: creates alerts.
    Controls: Allows moderator zone."""

    def __init__(self, ):

class VolumePage(SettingsPage):
    """A page that allows you to change the volume."""
    pass

class LanguagePage(SettingsPage):
    """A page that allows you to change the language."""
    pass

class NotifPage(SettingsPage):
    """A page that allows you to create reminders."""

class ViewNotif(NotifPage):
    """ A page that lists all notifications. """

class AddNotif(NotifPage):
    """A page that creates a new instance of a notification. """
    day = datetime  # I think this is referencing the current day, loser :)
    time = day.time
    content = input("What is happening on that day?")

class ControlPage(SettingsPage):
    """A page that allows you to go into moderator mode. """
