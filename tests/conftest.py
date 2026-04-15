import copy

import pytest
from starlette.testclient import TestClient

from src.app import app, activities

# Capture original seed data once at module import time
_original_activities = copy.deepcopy(activities)


@pytest.fixture
def client():
    # Reset in-memory state to original seed data before each test
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
    return TestClient(app)
