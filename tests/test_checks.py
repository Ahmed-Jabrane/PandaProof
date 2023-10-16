import pandas as pd
from pandaproof.checks import DataQualityChecker

sample_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'San Francisco', 'Los Angeles']
})

test_schema = {
    'Name': {'type': object, 'required': True},
    'Age': {'type': int, 'required': True},
    'City': {'type': object, 'required': False}
}

def test_check_data_schema():
    checker = DataQualityChecker(sample_data)
    issues = checker.check_data_schema(test_schema)
    assert not issues

def test_check_unique_key():
    checker = DataQualityChecker(sample_data)
    key_columns = []
    issues = checker.check_unique_key(key_columns)
    assert not issues

