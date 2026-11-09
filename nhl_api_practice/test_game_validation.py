from validation.data_validation_testing import validate_games

def test_empty_games():
    test_data = {
        "games": []
    }

    result = validate_games(test_data)

    assert result["status"] == "empty"
    
def test_success():
    test_data = {
        "games": [
            {"id": 101},
            {"id": 102}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result["status"] == "success"
    
def test_duplicate_games():
    data_i = {
        "games": [
            {"id": 101},
            {"id": 101},
            {"id": 102}
        ]
    }
    
    result = validate_games(data_i)
    
    assert result["status"] == "duplicate_records"
    assert len(result["duplicate_valid_records"]) == 1
    
def test_mixed_validity():
    data_j = {
        "games": [
            {"id": 101},
            {"id": 101},
            "hello"
        ]
    }
    
    result = validate_games(data_j)
    
    assert result["status"] == "partial_failure"
    assert len(result["valid_records_raw"]) == 2
    assert len(result["duplicate_valid_records"]) == 1
    assert len(result["invalid_records"]) == 1
    
    
def test_bool_id():
    test_data = {
        "games": [
            {"id": True}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result["status"] == "record_failure"
    assert result["invalid_records"] == [True]
    assert len(result["valid_records_unique"]) == 0
    

def test_zero_id():
    test_data = {
        "games": [
            {"id": 0}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result["status"] == "record_failure"
    assert len(result["invalid_records"]) == 1
    assert len(result["invalid_game_ids"]) == 1

    
def test_missing_games_key():
    test_data = {
        "gaames": [
            {"id": 101}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result["status"] == "response_error"


def test_repeated_calls_are_independent():
    test_data = {
        "games": [
            {"id": 101},
            {"id": 102}
        ]
    }
    
    result = validate_games(test_data)
    resultt = validate_games(test_data)
    
    assert result["status"] == "success"
    assert len(result["valid_records_unique"]) == 2
    assert len(resultt["valid_records_unique"]) == 2
    assert len(result["duplicate_valid_records"]) == 0
    assert len(resultt["duplicate_valid_records"]) == 0