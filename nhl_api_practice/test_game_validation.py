from validation.data_validation_testing import validate_games

def test_empty_games():
    test_data = {
        "games": []
    }

    result = validate_games(test_data)

    assert result[0] == "empty"
    
def test_success():
    test_data = {
        "games": [
            {"id": 101},
            {"id": 102}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result[0] == "success"
    
def test_duplicate_games():
    data_i = {
        "games": [
            {"id": 101},
            {"id": 101},
            {"id": 102}
        ]
    }
    
    result = validate_games(data_i)
    
    assert result[0] == "duplicate_records"
    assert len(result[3]) == 1
    
def test_mixed_validity():
    data_j = {
        "games": [
            {"id": 101},
            {"id": 101},
            "hello"
        ]
    }
    
    result = validate_games(data_j)
    
    assert result[0] == "partial_failure"
    assert len(result[1]) == 2
    assert len(result[3]) == 1
    assert len(result[4]) == 1
    
    
def test_bool_id():
    test_data = {
        "games": [
            {"id": True}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result[0] == "record_failure"
    assert result[4] == [True]
    assert len(result[2]) == 0
    

def test_zero_id():
    test_data = {
        "games": [
            {"id": 0}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result[0] == "record_failure"
    assert len(result[4]) == 1
    assert len(result[5]) == 1

    
def test_missing_games_key():
    test_data = {
        "gaames": [
            {"id": 101}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result[0] == "response_error"

def test_duplicated_success_call():
    test_data = {
        "games": [
            {"id": 101},
            {"id": 102}
        ]
    }
    
    result = validate_games(test_data)
    result = validate_games(test_data)
    
    assert result[0] == "success"
    assert len(result[2]) == 2
    assert len(result[3]) == 0