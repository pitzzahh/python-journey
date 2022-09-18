# put your python code here
first_hour = abs(int(input()))
first_minutes = abs(int(input()))
first_seconds = abs(int(input()))
second_hour = abs(int(input()))
second_minutes = abs(int(input()))
second_seconds = abs(int(input()))

seconds_in_hour = 3600
seconds_in_minutes = 60

first_moment_hour = first_hour * seconds_in_hour
first_moment_minutes = first_minutes * seconds_in_minutes

first_moment = first_moment_hour + first_moment_minutes + first_seconds

second_moment_hour = second_hour * seconds_in_hour
second_moment_minutes = second_minutes * seconds_in_minutes

second_moment = second_moment_hour + second_moment_minutes + second_seconds

print(second_moment - first_moment)
