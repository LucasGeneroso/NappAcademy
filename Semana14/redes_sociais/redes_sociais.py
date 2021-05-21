from abc import ABC, abstractmethod
from sessoes import PersonalSection, AlbumSection, PublicationSection, UploadSection


class Profile(ABC):
    def __init__(self):
        self._sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self._sections

    def addSections(self, section):
        self._sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


class github(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(UploadSection())


class instagram(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())
