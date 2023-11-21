def table(base, start, end, inc):
    for i in range(start, end + 1, inc):
        print(f"{base} * {i} = {base * i}")

base_value = 5
start_value = 1
end_value = 10
increment_value = 2

print(f"Displaying the multiplication table for {base_value} from {start_value} to {end_value}, with an increment of {increment_value}:")
table(base_value, start_value, end_value, increment_value)