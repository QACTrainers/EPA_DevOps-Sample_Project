from service import Service
from repo import Repo

# Testing the change_record stock function which lowers a records stock by an order quantity
# def test_changeRecordStock(mocker):

#     # Arrange 
#     record_id = 0
#     order_id = 0
#     result = False
#     mocker.patch("self.repo.runQuery", return_value = )

#     # Act
#     result = changeRecordStock(record_id, order_id)

#     # Assert 
#     assert result == True

test_repo = Repo()
test_service = Service(test_repo)

def test_deleteAllRecords(mocker):

    # Arrange

    result = False
    mocker.patch("repo.Repo.runQuery", return_value="")
    # Act 

    result = test_service.deleteAllRecords()

    # Assert
    assert result == True
