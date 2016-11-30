import os
import pytest
import json


@pytest.fixture(scope='session')
def stump_json():
    # Who cares about RAM anyway?
    data = {}
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'json')
    for f in os.listdir(data_path):
        with open(os.path.join(data_path, f), 'rt') as fh:
            data[f] = json.load(fh)

    return data
