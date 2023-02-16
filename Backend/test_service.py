import pytest
from unittest.mock import MagicMock

from service import Service


@pytest.fixture
def mock_repo():
    return MagicMock()

test_new_data = {
        'title': 'Title 1',
        'artist': 'Artist 1',
        'genre': 'Genre 1',
        'runtime': 10,
        'total_stock': 10,
        'cost': 9.99,
    }


def test_get_all_records(mock_repo):
    mock_repo.runQuery.return_value.fetchall.return_value = [
        (1, 'Title 1', 'Artist 1', 'Genre 1', 10, 9.99),
        (2, 'Title 2', 'Artist 2', 'Genre 2', 20, 19.99),
    ]
    service = Service(mock_repo)

    actual = service.getAllRecords()

    expected = [
        {
            'id': 1,
            'title': 'Title 1',
            'artist': 'Artist 1',
            'genre': 'Genre 1',
            'runtime': 10,
            'total_stock': 10,
            'cost': 9.99,
        },
        {
            'id': 2,
            'title': 'Title 2',
            'artist': 'Artist 2',
            'genre': 'Genre 2',
            'runtime': 20,
            'total_stock': 20,
            'cost': 19.99,
        },
    ]
    assert actual == expected
    mock_repo.runQuery.assert_called_once_with("SELECT * FROM records")


def test_get_record_id(mock_repo):
    mock_repo.runQuery.return_value.fetchall.return_value = [(1, 'Title 1', 'Artist 1', 'Genre 1', 10, 9.99)]
    service = Service(mock_repo)

    actual = service.getRecordId(1)

    expected = {
        'id': 1,
        'title': 'Title 1',
        'artist': 'Artist 1',
        'genre': 'Genre 1',
        'runtime': 10,
        'total_stock': 10,
        'cost': 9.99,
    }
    assert actual == expected
    mock_repo.runQuery.assert_called_once_with("SELECT * FROM records WHERE record_id = 1")


def test_create_record(mock_repo):

    service = Service(mock_repo)

    actual = service.createRecord(test_new_data)

    expected = mock_repo.runQuery.return_value
    assert actual == expected
    mock_repo.runQuery.assert_called_once_with(
        "INSERT INTO records (title, artist, genre, runtime, total_stock, cost) VALUES ('Title 1', 'Artist 1', 'Genre 1', 10, 10, 9.99);"
    )


def test_update_record(mock_repo):

    service = Service(mock_repo)

    actual = service.updateRecord(1, test_new_data)

    expected = mock_repo.runQuery.return_value
    assert actual == True
    mock_repo.runQuery.assert_called_once_with(
        "UPDATE records SET title = 'Title 1', artist = 'Artist 1', genre = 'Genre 1', runtime = '10', total_stock = '10', cost = '9.99' WHERE record_id = 1"
    )

def test_delete_record(mock_repo):

    service = Service(mock_repo)

    actual = service.deleteRecord(1)

    expected = True

    assert actual == expected
    mock_repo.runQuery.assert_called_once_with(
        "DELETE from records WHERE record_id = 1"
    )

def test_delete_all(mock_repo):

    test_service = Service(mock_repo)

    actual = test_service.deleteAllRecords()

    expected = True

    assert actual == expected
    mock_repo.runQuery.assert_called_once_with(
        "DELETE from records WHERE record_id > 1"
    )

def test_get_record_search(mock_repo):
    mock_repo.runQuery.return_value.fetchall.return_value = [(1, 'Title 1', 'Artist 1', 'test_genre', 10, 9.99)]

    service = Service(mock_repo)

    actual = service.getRecordSearch("test_genre")

    expected = {
        'id': 1,
        'title': 'Title 1',
        'artist': 'Artist 1',
        'genre': 'test_genre',
        'runtime': 10,
        'total_stock': 10,
        'cost': 9.99,
    }

    assert actual == expected
    mock_repo.runQuery.assert_called_once_with("SELECT * FROM records WHERE (title LIKE '%test_genre%') OR (artist LIKE '%test_genre%') OR (genre LIKE '%test_genre%');")
