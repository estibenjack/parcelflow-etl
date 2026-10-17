from src.transform import standardise_record


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
    assert result["destination_city"] == "Manchester"
    assert result["event_status"] == "IN_TRANSIT"