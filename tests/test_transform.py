from src.transform import deduplicate_events, standardise_record, validate_record


def test_standardise_record():
    sample = {
        "shipment_id": "PF-BEL-00001",
        "origin_depot": " bELFAst   ",
        "destination_city": "   manchester",
        "event_status": "in_transit"
    }

    result = standardise_record(sample)

    assert result["shipment_id"] == "PF-BEL-00001"
    assert result["origin_depot"] == "Belfast"
    assert sample["origin_depot"] == " bELFAst   "
    assert result["destination_city"] == "Manchester"
    assert result["event_status"] == "IN_TRANSIT"


def test_validate_record_valid_timestamp():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "2.50",
        "event_status": "IN_TRANSIT"
    }

    assert validate_record(record) is True


def test_validate_record_invalid_timestamp():
    record = {"event_timestamp": "not-a-date"}

    assert validate_record(record) is False


def test_validate_record_empty_timestamp():
    record = {"event_timestamp": ""}

    assert validate_record(record) is False


def test_validate_record_none_timestamp():
    record = {"event_timestamp": None}

    assert validate_record(record) is False


def test_validate_record_missing_key_timestamp():
    record = {"destination_location": "manchester"}

    assert validate_record(record) is False


def test_validate_record_negative_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "-2.50",
        "event_status": "IN_TRANSIT"
    }

    assert validate_record(record) is False


def test_validate_record_empty_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": ""
    }

    assert validate_record(record) is False


def test_validate_record_missing_weight_key():
    record = {
        "event_timestamp": "2026-10-13 03:41:00"
    }

    assert validate_record(record) is False


def test_validate_record_zero_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "0"
    }

    assert validate_record(record) is False


def test_validate_record_non_numeric_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "seven"
    }

    assert validate_record(record) is False


def test_validate_record_none_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": None
    }

    assert validate_record(record) is False


def test_validate_record_NaN_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "NaN"
    }

    assert validate_record(record) is False


def test_validate_record_infinity_weight():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "Infinity"
    }

    assert validate_record(record) is False


def test_validate_record_valid_status():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "2.50",
        "event_status": "IN_TRANSIT"
    }

    assert validate_record(record) is True


def test_validate_record_unknown_status():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "2.50",
        "event_status": "UNKNOWN_STATUS"
    }

    assert validate_record(record) is False


def test_validate_record_empty_status():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "2.50",
        "event_status": ""
    }

    assert validate_record(record) is False


def test_validate_record_none_status():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "2.50",
        "event_status": None
    }

    assert validate_record(record) is False


def test_validate_record_missing_status_key():
    record = {
        "event_timestamp": "2026-10-13 03:41:00",
        "parcel_weight_kg": "2.50"
    }

    assert validate_record(record) is False


def test_deduplicate_events():
    records = [
        {"event_id": "EV001", "shipment_id": "PF001"},
        {"event_id": "EV002", "shipment_id": "PF001"},
        {"event_id": "EV001", "shipment_id": "PF001"},
        {"event_id": "EV003", "shipment_id": "PF002"}
    ]

    unique_records, conflicting_records = deduplicate_events(records)

    assert len(unique_records) == 3
    assert len(conflicting_records) == 0
    assert unique_records[0]["event_id"] == "EV001"
    assert unique_records[1]["event_id"] == "EV002"
    assert unique_records[2]["event_id"] == "EV003"


def test_deduplicate_events_excludes_missing_event_ids():
    records = [
        {"event_id": "EV001", "shipment_id": "PF001"},
        {"event_id": "", "shipment_id": "PF002"},
        {"shipment_id": "PF003"}
    ]

    unique_records, conflicting_records = deduplicate_events(records)

    assert len(unique_records) == 1
    assert unique_records[0]["event_id"] == "EV001"
    assert conflicting_records == []


def test_deduplicate_events_excludes_whitespace_only_event_ids():
    records = [
        {"event_id": "EV001", "shipment_id": "PF001"},
        {"event_id": "   ", "shipment_id": "PF004"}
    ]

    unique_records, conflicting_records = deduplicate_events(records)

    assert len(unique_records) == 1
    assert unique_records[0]["event_id"] == "EV001"
    assert conflicting_records == []


def test_deduplicate_events_handles_event_id_whitespace():
    records = [
        {"event_id": "  EV001 ", "shipment_id": "PF001"},
        {"event_id": "EV001", "shipment_id": "PF001"}
    ]

    unique_records, conflicting_records = deduplicate_events(records)

    assert len(unique_records) == 1
    assert unique_records[0]["event_id"] == "  EV001 "
    assert conflicting_records == []


def test_deduplicate_events_detects_conflicting_records():
    records = [
        {"event_id": "  EV001 ", "event_status": "DISPATCHED"},
        {"event_id": "EV001", "event_status": "IN_TRANSIT"}
    ]

    unique_records, conflicting_records = deduplicate_events(records)

    assert len(unique_records) == 1
    assert len(conflicting_records) == 1
    assert unique_records[0]["event_status"] == "DISPATCHED"
    assert conflicting_records[0]["event_status"] == "IN_TRANSIT"

