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


def print_results(valid_records, duplicate_valid_records, invalid_records, duplicate_invalid_records):
    print('Begin intake report: ')
    print(f'    Found {len(valid_records)} valid game ids.')
    print(f'    Skipped {len(duplicate_valid_records)} duplicated valid game ids.')
    print(f'    Found {len(invalid_records)} invalid game ids.')
    print(f'    Skipped {len(duplicate_invalid_records)} duplicated invalid game ids.')
    print('-----------------------')


def validate_games(data_dict):
    valid_records = []
    duplicate_valid_records = []
    invalid_records = []
    duplicate_invalid_records = []
    
    def valid_records_append(record):
        if record not in valid_records:
            valid_records.append(record)
        else:
            duplicate_valid_records.append(record)
            
    def invalid_records_append(record):
        if record not in invalid_records:
            invalid_records.append(record)
        else:
            duplicate_invalid_records.append(record)

    if "games" in data_dict:
        if isinstance(data_dict["games"], list):
            if len(data_dict["games"]) != 0: # Checks if not an empty list
                # define a valid game record as a dictionary containing an id key whose value is a positive integer
                # dictionary in a list in a dictionary
                for game in data_dict["games"]:
                    if isinstance(game, dict):
                        if "id" in game: 
                            if type(game["id"]) == int:
                                if game["id"] > 0:
                                    valid_records_append(game["id"])
                                else: # Negative id number
                                    invalid_records_append(game["id"])
                            else: # Non-int id number
                                invalid_records_append(game)
                        else: # Key isn't "id"
                            invalid_records_append(game)
                    else: # game isn't a dict
                        invalid_records_append(game)
            else:
                print(f'Advisory: {data_dict["games"]} is empty.')
        else:
            print(f'Error: Invalid type - {type(data_dict["games"])}')
    else:
        print('Games key is missing.')
        
    return valid_records, duplicate_valid_records, invalid_records, duplicate_invalid_records


def validation_helper(data_set):
    valid_records, duplicate_valid_records, invalid_records, duplicate_invalid_records = validate_games(data_set)
    print_results(valid_records, duplicate_valid_records, invalid_records, duplicate_invalid_records)


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
