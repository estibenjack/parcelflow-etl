from datetime import datetime
from decimal import Decimal, InvalidOperation


VALID_STATUSES = {
    "DISPATCHED",
    "IN_TRANSIT",
    "OUT_FOR_DELIVERY",
    "DELIVERED"
}

def standardise_record(record):

    cleaned_rec = record.copy()

    cleaned_rec['origin_depot'] = cleaned_rec['origin_depot'].strip().title()
    cleaned_rec['destination_city'] = cleaned_rec['destination_city'].strip().title()
    cleaned_rec['event_status'] = cleaned_rec['event_status'].strip().upper()

    return cleaned_rec


def validate_record(record):
    try:
        datetime.strptime(record["event_timestamp"], "%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError, KeyError):
        return False

    try:
        weight = Decimal(record["parcel_weight_kg"])
        if not weight.is_finite() or weight <= 0:
            return False
    except (InvalidOperation, TypeError, KeyError):
        return False

    if record.get("event_status") not in VALID_STATUSES:
        return False
    
    return True


def deduplicate_events(records):
    seen_event_ids = set()
    unique_records = []

    for record in records:
        event_id = record.get("event_id")
        
        if not event_id:
            continue

        event_id = event_id.strip()

        if not event_id:
            continue

        if event_id not in seen_event_ids:
            seen_event_ids.add(event_id)
            unique_records.append(record)

    return unique_records