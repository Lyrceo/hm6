result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a < b")
        if b == 0:
            raise ZeroDivisionError("b is 0")
        if b > 100:
            raise IndexError("b > 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"An unexpected error occurred while processing data[{key}]: {e}")

print(result)
