import pytest
from redes_sociais import facebook, linkedin, github, instagram
from sessoes import PersonalSection, AlbumSection, PublicationSection, UploadSection


class TestFactoryFacebook():
    def test_instanciar_objeto_ok(self):
        objeto = facebook()
        assert isinstance(objeto, facebook)

    def test_nome_objeto_ok(self):
        objeto = facebook()
        assert type(objeto).__name__ == "facebook"

    def test_sessoes_objeto_ok(self):
        objeto = facebook()
        assert str(objeto.getSections()) == "[Dados Pessoais, Sessão para fotos]"


class TestFactoryLinkedin():
    def test_instanciar_objeto_ok(self):
        objeto = linkedin()
        assert isinstance(objeto, linkedin)

    def test_nome_objeto_ok(self):
        objeto = linkedin()
        assert type(objeto).__name__ == "linkedin"

    def test_sessoes_objeto_ok(self):
        objeto = linkedin()
        assert str(objeto.getSections()) == "[Dados Pessoais, Sessão publicações]"


class TestFactoryGithub():
    def test_instanciar_objeto_ok(self):
        objeto = github()
        assert isinstance(objeto, github)

    def test_nome_objeto_ok(self):
        objeto = github()
        assert type(objeto).__name__ == "github"

    def test_sessoes_objeto_ok(self):
        objeto = github()
        assert str(objeto.getSections()) == "[Dados Pessoais, Sessão para Upload]"


class TestFactoryInstagram():
    def test_instanciar_objeto_ok(self):
        objeto = instagram()
        assert isinstance(objeto, instagram)

    def test_nome_objeto_ok(self):
        objeto = instagram()
        assert type(objeto).__name__ == "instagram"

    def test_sessoes_objeto_ok(self):
        objeto = instagram()
        assert str(objeto.getSections()) == "[Dados Pessoais, Sessão para fotos]"


def TestFactorySessoes():
    def test_instanciar_PersonalSection(self):
        objeto = PersonalSection()
        assert isinstance(objeto, PersonalSection)

    def test_sobre_PersonalSection(self):
        objeto = PersonalSection()
        assert objeto.sobre() == "Sessao para dados pessoais"

    def test_instanciar_AlbumSection(self):
        objeto = AlbumSection()
        assert isinstance(objeto, AlbumSection)

    def test_sobre_AlbumSection(self):
        objeto = AlbumSection()
        assert objeto.sobre() == "Sessao para fotos"

    def test_instanciar_PublicationSection(self):
        objeto = PublicationSection()
        assert isinstance(objeto, PublicationSection)

    def test_sobre_PublicationSection(self):
        objeto = PublicationSection()
        assert objeto.sobre() == "Sessao para publicações(posts)"

    def test_instanciar_UploadSection(self):
        objeto = UploadSection()
        assert isinstance(objeto, UploadSection)

    def test_sobre_UploadSection(self):
        objeto = UploadSection()
        assert objeto.sobre() == "Sessao para Upload"



