def standardise_record(record):

    cleaned_rec = record.copy()

    cleaned_rec['origin_depot'] = cleaned_rec['origin_depot'].strip().title()
    cleaned_rec['destination_city'] = cleaned_rec['destination_city'].strip().title()
    cleaned_rec['event_status'] = cleaned_rec['event_status'].strip().upper()

    return cleaned_rec


sample = {
    "origin_depot": " bELFAST ",
    "destination_city": " manchester ",
    "event_status": "in_transit"
}

result = standardise_record(sample)

print(result)