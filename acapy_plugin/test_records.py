from .records import *

from unittest import mock, TestCase


class TestRecordsAdd(TestCase):
    payload = """[
        {
            "data1": "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/basicmessage/1.0/message",
            "data2": [],
        }
    ]"""

    def test_init(self):
        recordsAdd = RecordsAdd(payload=self.payload)
        assert recordsAdd.payload == self.payload
        assert recordsAdd.record_id == None

    def test_type(self):
        recordsAdd = RecordsAdd(payload=self.payload)
        assert recordsAdd._type == RECORDS_ADD

    @mock.patch(f"{RECORDS}.RecordsAddSchema.load")
    def test_deserialize(self, mock_records_add_schema_load):
        obj = {"obj": "obj"}

        recordsAdd = RecordsAdd.deserialize(obj)
        mock_records_add_schema_load.assert_called_once_with(obj)

        assert recordsAdd is mock_records_add_schema_load.return_value

    @mock.patch(f"{RECORDS}.RecordsAddSchema.dump")
    def test_serialize(self, mock_records_add_schema_dump):
        recordsAdd = RecordsAdd(payload=self.payload)

        recordsAdd_dict = recordsAdd.serialize()
        mock_records_add_schema_dump.assert_called_once_with(recordsAdd)

        assert recordsAdd_dict is mock_records_add_schema_dump.return_value


class TestRecordsAddSchema(TestCase):

    recordsAdd = RecordsAdd(payload="a")

    def test_make_model(self):
        data = self.recordsAdd.serialize()
        model_instance = RecordsAdd.deserialize(data)
        assert isinstance(model_instance, RecordsAdd)


class TestRecordsGet(TestCase):
    record_id = "1234"

    def test_init(self):
        recordsGet = RecordsGet(record_id=self.record_id)
        assert recordsGet.record_id == self.record_id

    def test_type(self):
        recordsGet = RecordsGet(record_id=self.record_id)
        assert recordsGet._type == RECORDS_GET

    @mock.patch(f"{RECORDS}.RecordsGetSchema.load")
    def test_deserialize(self, mock_records_get_schema_load):
        obj = {"obj": "obj"}

        recordsGet = RecordsGet.deserialize(obj)
        mock_records_get_schema_load.assert_called_once_with(obj)

        assert recordsGet is mock_records_get_schema_load.return_value

    @mock.patch(f"{RECORDS}.RecordsGetSchema.dump")
    def test_serialize(self, mock_records_get_schema_dump):
        recordsGet = RecordsGet(record_id=self.record_id)

        recordsGet_dict = recordsGet.serialize()
        mock_records_get_schema_dump.assert_called_once_with(recordsGet)

        assert recordsGet_dict is mock_records_get_schema_dump.return_value


class TestRecordsGetSchema(TestCase):
    recordsGet = RecordsGet(record_id="123566")

    def test_make_model(self):
        data = self.recordsGet.serialize()
        model_instance = RecordsGet.deserialize(data)
        assert isinstance(model_instance, RecordsGet)