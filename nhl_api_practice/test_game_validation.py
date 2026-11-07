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
    
def test_bool_id():
    test_data = {
        "games": [
            {"id": True}
        ]
    }
    
    result = validate_games(test_data)
    
    assert len(result[4]) == 1
    assert len(result[2]) == 0
