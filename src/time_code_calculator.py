from re import split

def add_time_codes(input_list):
    """
    takes a list of time codes in a hh:mm:ss format 
    (can leave out hours and minutes but must end in seconds)

    returns their sum as a time code
    """
    total_time = 0
    for item in input_list: # turning time codes into seconds & adding them up
        separated_nums = split(r"\:", item)

        seconds = int(separated_nums[-1])
        if len(separated_nums) >= 2:
            minutes = int(separated_nums[-2]) * 60
        else: minutes = 0
        if len(separated_nums) == 3:
            hours = int(separated_nums[-3]) * 60 * 60
        else: hours = 0

        num = seconds + minutes + hours
        total_time += num

    second_remainder = None
    minute_remainder = None
    total_hours = None
    if total_time < 60: # if only seconds
        second_remainder = total_time
    else: # making minutes
        second_remainder = total_time % 60
        total_minutes = int((total_time - second_remainder) / 60)
        if second_remainder == 0:
            second_remainder = "00"

        if total_minutes < 60:
            minute_remainder = total_minutes
        else: # making hours
            minute_remainder = total_minutes % 60
            total_hours = int((total_minutes - minute_remainder) / 60)
            if minute_remainder == 0:
                minute_remainder = "00"

    final_string = ""
    if total_hours:
        final_string += f"{total_hours}:"
    if minute_remainder:
        final_string += f"{minute_remainder}:"
    final_string += f"{second_remainder}"

    return final_string