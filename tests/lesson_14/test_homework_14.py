from lessons.lesson_14.homework_14 import log_event
import pytest
import logging

@pytest.mark.parametrize("name, status, log_level", [
    ("Sasha", "success", "INFO"),
    ("Masha", "expired", "WARNING"),
    ("Dasha", "failed", "ERROR"),
])

def test_log_event_success(caplog, name, status, log_level):
    caplog.set_level(logging.INFO, logger="log_event")

    log_event(name, status)

    assert len(caplog.records) > 0
    record = caplog.records[0]
    assert record.levelname == log_level, "Incorrect log level"
    assert name in record.message, "Incorrect name in log message"
    assert status in record.message, "Incorrect status in log message"

