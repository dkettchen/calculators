from src.time_code_calculator import add_time_codes

def test_does_not_mutate_input():
    input_list = ["1", "1"]
    add_time_codes(input_list)
    assert input_list == ["1", "1"]

def test_returns_string():
    input_list = ["1", "1"]
    result = add_time_codes(input_list)
    assert type(result) == str

def test_returns_0_for_empty_list():
    input_list = []
    result = add_time_codes(input_list)
    assert result == "0"

def test_returns_single_char_string_for_less_than_10_seconds():
    input_list = ["1", "1"]
    result = add_time_codes(input_list)
    assert len(result) == 1

def test_returns_double_char_string_for_less_than_1_min():
    input_list = ["10", "15"]
    result = add_time_codes(input_list)
    assert len(result) == 2

def test_returns_string_containing_colon_for_more_than_59_seconds():
    input_list = ["25", "40"]
    result = add_time_codes(input_list)
    assert ":" in result

def test_returns_result_in_hh_mm_ss_format():
    input_list = ["2:32:01", "9:52:20"]
    result = add_time_codes(input_list)
    assert type(int(result[:2])) == int
    assert type(int(result[3:5])) == int
    assert type(int(result[-2:])) == int
    assert result[2] == ":"
    assert result[5] == ":"

def test_returns_correctly_summed_seconds_for_less_than_1_min():
    input_list = ["10", "15"]
    result = add_time_codes(input_list)
    assert result == "25"

def test_returns_correctly_summed_time_for_full_minutes():
    input_list = ["10", "50"]
    result = add_time_codes(input_list)
    assert result == "1:00"

def test_processes_input_with_more_than_1_min_time_codes():
    input_list = ["1:10", "2:50"]
    result = add_time_codes(input_list)
    assert result == "4:00"

def test_returns_correctly_summed_time_for_full_hours():
    input_list = ["45:00", "15:00"]
    result = add_time_codes(input_list)
    assert result == "1:00:00"

def test_returns_correctly_summed_time_for_results_that_contain_multiple_sizes():
    input_list = ["32:01", "52:20"]
    result = add_time_codes(input_list)
    assert result == "1:24:21"

def test_processes_input_with_more_than_1_hour_time_codes():
    input_list = ["2:32:01", "9:52:20"]
    result = add_time_codes(input_list)
    assert result == "12:24:21"

def test_returns_correctly_summed_result_for_more_than_2_items_in_list():
    input_list = ["10", "20:12", "50:10:05", "16:24"]
    result = add_time_codes(input_list)
    assert result == "50:46:51"
