# ParcelFlow - Data Quality Rules

## Standardisation
- [x] ~~Trim and normalise depot names, cities and statuses~~
- [ ] Handle missing or null values without crashing
- [ ] Validate origin depot against known depots

## Validation
- [x] ~~Validate event timestamps~~
- [x] ~~Reject invalid, zero, negative and non-finite weights~~
- [x] ~~Validate event statuses~~
- [ ] Validate required IDs and shipment fields
- [ ] Check expected delivery date and date consistency

## Deduplication
- [x] ~~Exclude records with missing, empty or whitespace-only event_id~~
- [x] ~~Normalise surrounding whitespace in event IDs for duplicate detection~~
- [x] ~~Detect conflicting records sharing an event_id~~
- [x] ~~Presxerve conflicting records in a separate collection~~
- [x] ~~Test exact duplicates and preserved event order~~
- [ ] Quarantine both versions of conflicting events
- [ ] Preserve records rejected due to missing IDs with rejection reasons

## Pipeline integration
- [ ] Restructure records into three relational tables
- [ ] Quarantine rejected records with reasons
- [ ] Ensure repeated loads do not create duplicate database records