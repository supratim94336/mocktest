from src.db_connector import Engine


def test_engine_load_data(mocker):
    mocker.patch("src.db_connector.DBConnector.__init__", return_value=None)
    mocker.patch("src.db_connector.DBConnector.get", return_value='xyz')
    output = Engine().load_data()
    assert output == 'xyzxxx'
