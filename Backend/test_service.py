from service import *

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

def test_deleteAllRecords(mocker):

    # Arrange

    result = False
    # Act 
    result = test_deleteAllRecords()

    # Assert
    assert result == True
