from service import Service
from repo import Repo

def setup_module(module):
    print("Hello World")

test_repo = Repo("test-db")
test_service = Service(test_repo)

test_repo.createTable()


def test_deleteAllRecords(mocker):

    # Arrange

    result = False
    mocker.patch("repo.Repo.runQuery", return_value="")
    # Act 

    result = test_service.deleteAllRecords()

    # Assert
    assert result == True

def test_getAllRecords(mocker):



    # mocker.patch("repo.Repo.runQuery", return_value = "Hello")
    mocker.patch("service.Service.fetchall", return_value = "Hello")

    result = test_service.getAllRecords()
    

    assert result == "Hello"

