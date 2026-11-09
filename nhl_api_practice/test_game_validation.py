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
    assert result["duplicate_valid_records"] == [101]


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
    assert result["valid_records_raw"] == [101, 101]
    assert result["duplicate_valid_records"] == [101]
    assert result["invalid_records"] == ["hello"]


def test_bool_id():
    test_data = {
        "games": [
            {"id": True}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result["status"] == "record_failure"
    assert result["invalid_records"] == [True]
    assert result["valid_records_unique"] == []


def test_zero_id():
    test_data = {
        "games": [
            {"id": 0}
        ]
    }
    
    result = validate_games(test_data)
    
    assert result["status"] == "record_failure"
    assert result["invalid_records"] == [0]
    assert result["invalid_game_ids"] == [0]


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
    
    first_result = validate_games(test_data)
    secont_result = validate_games(test_data)
    
    assert first_result["status"] == "success"
    assert secont_result["status"] == "success"
    assert first_result["valid_records_unique"] == [101, 102]
    assert secont_result["valid_records_unique"] == [101, 102]
    assert first_result["duplicate_valid_records"] == []
    assert secont_result["duplicate_valid_records"] == []


def test_mixed_validity_two():
    data_j = {
        "games": [
            {"id": 101},
            {"id": 101},
            {"id": "hello"}
        ]
    }
    
    result = validate_games(data_j)
    
    assert result["status"] == "partial_failure"
    assert result["valid_records_raw"] == [101, 101]
    assert result["duplicate_valid_records"] == [101]
    assert result["invalid_records"] == ["hello"]