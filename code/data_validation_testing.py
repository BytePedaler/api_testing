# The games key exists, contains a list, and has two elements.
data_a = {
    "games": [
        {"id": 101},
        {"id": 102}
    ]
}

# The games key exists, but there are no games.
data_b = {
    "games": []
}

# The dictionary exists, but the games key is missing.
data_c = {
    "date": "2024-01-15"
}

data_d = {
    "games": "No games available"
}

data_e = {
    "games": None
}

data_f = {
    "games": ["hello", "world"]
}

data_g = {
    "games": [
        {"id": 101},
        "hello",
        {"team": "SEA"},
        {"id": 104},
        {"id": "105"}
    ]
}

data_h = {
    "games": [
        {"id": 101},
        {"id": True},
        {"id": 0},
        {"id": -10},
        {"id": 102},
        {"id": None}
    ]
}

data_i = {
    "games": [
        {"id": 101},
        {"id": 101},
        {"id": 102}
    ]
}


def print_results(validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids):
    print('Begin intake report: ')
    print(f'    Found {len(valid_records_raw)} valid game ids.')
    print(f'    Found {len(duplicate_valid_records)} duplicated valid game ids.')
    print(f'    Found {len(invalid_records)} invalid records.')
    print(f'    Found {len(invalid_game_ids)} invalid game ids.')
    print(f'    Ingestion Status: {validation_status}')
    print('-----------------------')


def validate_games(data_dict):
    valid_records_raw = []
    valid_records_unique = []
    duplicate_valid_records = []
    invalid_records = []
    invalid_game_ids = []
    validation_status = 'unable_to_assign'
    
    def valid_records_append(record):
        valid_records_raw.append(record)
        if record not in valid_records_unique:
            valid_records_unique.append(record)
        else:
            duplicate_valid_records.append(record)
    
    def invalid_records_append(record):
        invalid_records.append(record)
        
    def invalid_game_ids_append(record):
        invalid_game_ids.append(record)


    if "games" not in data_dict:
        validation_status = 'response_error'
        return validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids
        
    if not isinstance(data_dict["games"], list):
        validation_status = 'response_error'
        return validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids
        
    num_games = len(data_dict["games"])
    
    if len(data_dict["games"]) == 0:
        validation_status = 'empty'
        return validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids
    
    for game in data_dict["games"]:
        if not isinstance(game, dict):
            invalid_records_append(game)
        elif not "id" in game:
            invalid_records_append(game)
        elif type(game["id"]) != int:
            invalid_records_append(game["id"])
            invalid_game_ids_append(game["id"])
        elif game["id"] <= 0:
            invalid_records_append(game["id"])
            invalid_game_ids_append(game["id"])
        else: 
            valid_records_append(game["id"])
    
    if len(valid_records_raw) <= 0:
        validation_status = 'record_failure'
        return validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids
    else: 
        if len(valid_records_raw) == num_games:
            validation_status = 'success'
            return validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids
        else:
            validation_status = 'partial_failure'
            return validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids


def validation_helper(data_set):
    validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids = validate_games(data_set)
    print_results(validation_status, valid_records_raw, duplicate_valid_records, invalid_records, invalid_game_ids)


def main():
    validation_helper(data_a)
    validation_helper(data_b)
    validation_helper(data_c)
    validation_helper(data_d)
    validation_helper(data_e)
    validation_helper(data_f)
    validation_helper(data_g)
    validation_helper(data_h)
    validation_helper(data_h)


if __name__ == "__main__":
    main()
