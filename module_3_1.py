calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search)

info1 = string_info("Capybara")
info2 = string_info("Armageddon")
contains1 = is_contains("Urban", ["ban", "BaNaNa", "urban", "Orange"])
contains2 = is_contains("cycle", ["Apple", "Banana", "Orange"])

print(f"{info1}")
print(f"{info2}")
print(f"{contains1}")
print(f"{contains2}")
print(f"{calls}")
