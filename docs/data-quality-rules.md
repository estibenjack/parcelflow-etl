# ParcelFlow - Data Quality Rules

## Standardisation
- [x] Trim and normalise depot names, cities and statuses
- [ ] Handle missing or null values without crashing
- [ ] Validate origin depot against known depots

## Validation
- [x] Validate event timestamps
- [x] Reject invalid, zero, negative and non-finite weights
- [x] Validate event statuses
- [ ] Validate required IDs and shipment fields
- [ ] Check expected delivery date and date consistency

## Deduplication
- [x] Keep first occurrence of each event_id
- [ ] Handle missing or blank event_id
- [ ] Detect conflicting records sharing an event_id
- [ ] Test exact duplicates and preserved event order

## Pipeline integration
- [ ] Restructure records into three relational tables
- [ ] Quarantine rejected records with reasons
- [ ] Ensure repeated loads do not create duplicate database records