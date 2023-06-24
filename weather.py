import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date_object = datetime.fromisoformat(iso_string)
    formatted_date = date_object.strftime("%A %d %B %Y")
    return formatted_date


def convert_f_to_c(temp_in_farenheit):
    temp_in_celsius = (float (temp_in_farenheit) - 32) * 5 / 9
    return round(temp_in_celsius, 1)


def calculate_mean(weather_data):
    total = 0
    for temp in weather_data:
        total = total + float(temp)
    number_of_items = len(weather_data)
    mean_value = total / number_of_items
    return mean_value


def load_data_from_csv(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        big_list = []
        for row in reader:
            if row:
                str1 = str(row[0])
                int1 = int(row[1])
                int2 = int(row[2])
                small_list = [str1, int1, int2]
                big_list.append(small_list)
        return big_list


def find_min(weather_data):
    if not weather_data:
        return ()
    
    new_list=[]
    for number in weather_data:
        new_list.append(float(number))
    min_value = min(new_list)
    min_index = new_list.index(min_value)
    
    print(new_list)
    min_index_list=[]
    index_counter=0
    for number in new_list:
        if min_value == number:
            min_index_list.append(index_counter)
        index_counter += 1
    print(min_index_list)
    return min_value, min_index_list[-1]


def find_max(weather_data):
    if not weather_data:
        return ()
    # Check if the list is empty
    if not weather_data:
        return ()
    # Convert the elements in the list to floats
    new_list = []
    for number in weather_data:
        new_list.append(float(number))
    # Find the maximum value and its index
    max_value = max(new_list)
    # Build a list of all indices with the maximum value
    max_index_list = []
    index_counter = 0
    for number in new_list:
        if max_value == number:
            max_index_list.append(index_counter)
        index_counter += 1
    # Return the maximum value and the last index in the list
    return max_value, max_index_list[-1]


def generate_summary(weather_data):
    if not weather_data:
        return "No weather data available."
# create empty lists
    temp_min_list = []
    temp_max_list = []
    date_list = []
# Iterate over each line in weather_data and extract the relevant data
    for line in weather_data:
        date_list.append(line[0])  # Store the date in the date_list
        temp_min_list.append(line[1])  # Store the minimum temperature in the temp_min_list
        temp_max_list.append(line[2])  # Store the maximum temperature in the temp_max_list
# Find the minimum and maximum temperatures and their corresponding positions in the lists
    min_value_f = find_min(temp_min_list)[0]  # Find the minimum value in temp_min_list in Fahrenheit
    min_value_c = convert_f_to_c(min_value_f)  # Convert the minimum value to Celsius
    min_data_position = find_min(temp_min_list)[1]  # Find the position of the minimum value in temp_min_list
    max_value_f = find_max(temp_max_list)[0]  # Find the maximum value in temp_max_list in Fahrenheit
    max_value_c = convert_f_to_c(max_value_f)  # Convert the maximum value to Celsius
    max_data_position = find_max(temp_max_list)[1]  # Find the position of the maximum value in temp_max_list
# Calculate the average low and high temperatures in Fahrenheit and convert them to Celsius
    average_low_f = calculate_mean(temp_min_list)  # Calculate the average of temp_min_list in Fahrenheit
    average_low_c = convert_f_to_c(average_low_f)  # Convert the average low temperature to Celsius
    average_high_f = calculate_mean(temp_max_list)  # Calculate the average of temp_max_list in Fahrenheit
    average_high_c = convert_f_to_c(average_high_f)  # Convert the average high temperature to Celsius
# Construct the summary string in the desired format using the calculated values
    return (
    f"{len(weather_data)} Day Overview\n"
    f"  The lowest temperature will be {format_temperature(min_value_c)}, and will occur on {convert_date(date_list[min_data_position])}.\n"
    f"  The highest temperature will be {format_temperature(max_value_c)}, and will occur on {convert_date(date_list[max_data_position])}.\n"
    f"  The average low this week is {format_temperature(average_low_c)}.\n"
    f"  The average high this week is {format_temperature(average_high_c)}.\n"
)

def generate_daily_summary(weather_data):
    if not weather_data:
        return "No weather data available."
# Initialize an empty string to store the summary
    summary = ""
# Iterate over each entry in weather_data
    for entry in weather_data:
        max_temp = convert_f_to_c(round(entry[2], 1))  # Convert and round the maximum temperature to Celsius
        min_temp = convert_f_to_c(round(entry[1], 1))  # Convert and round the minimum temperature to Celsius
        
# Adding data to the summary
        summary += f"---- {convert_date(entry[0])} ----\n"  # Add the formatted date to the summary
        summary += f"  Minimum Temperature: {min_temp}°C\n"  # Add the minimum temperature to the summary
        summary += f"  Maximum Temperature: {max_temp}°C\n\n"  # Add the maximum temperature to the summary
    return summary  # Return the final summary string"