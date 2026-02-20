# 401
def square_generator(n):
    for i in range(1,n + 1):
        yield i * i

n = int(input())
for value in square_generator(n):
    print(value)



# 402
def a(n):
    for i in range(n+1):
        if i%2==0:
            yield i

n=int(input())
print(",".join(map(str, a(n))))



# 403
def a(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

n=int(input())
for x in a(n):
    print(x)



# 404
def a(n,m):
    for i in range(n,m+1):
        yield i * i

n,m=map(int,input().split())
for x in a(n,m):
    print(x)



# 405
def a(n):
    for i in range(n,-1,-1):
        yield i

n=int(input())
for x in a(n):
    print(x)



# 406
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    n = int(input().strip())
    fib_sequence = list(fibonacci_generator(n))
    print(",".join(map(str, fib_sequence)))



# 407
class Reverse:
    def __init__(self, s):
        self.s = s
        self.i = len(s)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i == 0:
            raise StopIteration
        self.i -= 1
        return self.s[self.i]

print(''.join(Reverse(input())))



# 408
def a(n):
    for i in range(2,n+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            yield i


n=int(input())
print(*a(n))



# 409
def a(n):
    for i in range(0,n+1):
        yield 2**i

n=int(input())
print(*a(n))



# 410
def a(n, k):
    for _ in range(k):
        for item in n:
            yield item

n = input().split()
k = int(input())

print(*a(n, k))



# 411
import json

def apply_patch(source, patch):
    if not isinstance(source, dict) or not isinstance(patch, dict):
        # If either is not a dict, replace source with patch (but if patch is None, we handle above)
        return patch

    result = source.copy()

    for key, value in patch.items():
        if value is None:
            # Remove key if patch value is null
            result.pop(key, None)
        elif key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # Recursively patch nested objects
            result[key] = apply_patch(result[key], value)
        else:
            # Otherwise replace with patch value
            result[key] = value

    return result

def main():
    source = json.loads(input().strip())
    patch = json.loads(input().strip())

    patched = apply_patch(source, patch)

    # Sort keys lexicographically and output compact JSON
    print(json.dumps(patched, separators=(',', ':'), sort_keys=True))

if __name__ == "__main__":
    main()



# 412
import json

def deep_diff(obj1, obj2, path=""):
    differences = []

    # Get all unique keys from both objects
    keys = set(obj1.keys()) if isinstance(obj1, dict) else set()
    if isinstance(obj2, dict):
        keys.update(obj2.keys())

    for key in sorted(keys):  # sort for consistent order within recursion
        current_path = f"{path}.{key}" if path else key
        v1 = obj1.get(key, "<missing>") if isinstance(obj1, dict) else "<missing>"
        v2 = obj2.get(key, "<missing>") if isinstance(obj2, dict) else "<missing>"

        if v1 == "<missing>" and v2 == "<missing>":
            continue

        if isinstance(v1, dict) and isinstance(v2, dict):
            # Recursively compare nested objects
            differences.extend(deep_diff(v1, v2, current_path))
        elif v1 != v2:
            # Format values as compact JSON literals
            if v1 != "<missing>":
                v1 = json.dumps(v1, separators=(',', ':'))
            if v2 != "<missing>":
                v2 = json.dumps(v2, separators=(',', ':'))
            differences.append(f"{current_path} : {v1} -> {v2}")

    return differences


def main():
    obj1 = json.loads(input().strip())
    obj2 = json.loads(input().strip())

    diffs = deep_diff(obj1, obj2)

    if diffs:
        # Already sorted by path due to sorted keys + recursion
        for diff in diffs:
            print(diff)
    else:
        print("No differences")


if __name__ == "__main__":
    main()



# 413
import json
import re

def resolve_query(data, query):
    # Split query by dots and brackets
    # Example: "user.friends[0].name" -> ["user", "friends", "0", "name"]
    parts = re.split(r'[.\[\]]+', query)
    # Remove any empty strings from split (e.g., trailing bracket)
    parts = [p for p in parts if p]

    current = data
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.isdigit():
            idx = int(part)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                return "NOT_FOUND"
        else:
            return "NOT_FOUND"

    # Return compact JSON serialization
    return json.dumps(current, separators=(',', ':'))


def main():
    data = json.loads(input().strip())
    n = int(input().strip())

    for _ in range(n):
        query = input().strip()
        result = resolve_query(data, query)
        print(result)


if __name__ == "__main__":
    main()



# 414
from datetime import datetime, timedelta
import re

def parse_moment(moment_str):
    # Example: "2025-01-01 UTC+03:00"
    match = re.match(r'(\d{4}-\d{2}-\d{2}) UTC([+-])(\d{2}):(\d{2})', moment_str)
    if not match:
        raise ValueError("Invalid format")

    date_part, sign, hh, mm = match.groups()
    date = datetime.strptime(date_part, "%Y-%m-%d")

    offset_hours = int(hh) + int(mm) / 60
    if sign == '-':
        offset_hours = -offset_hours

    # Convert local midnight to UTC: subtract the offset
    # If offset is +03:00, local midnight = 03:00 UTC the previous day? Wait:
    # Local time = UTC + offset. So UTC = Local - offset.
    # Local midnight (00:00) in UTC = 00:00 - offset.
    utc_midnight = date - timedelta(hours=offset_hours)

    return utc_midnight

def main():
    moment1_str = input().strip()
    moment2_str = input().strip()

    utc1 = parse_moment(moment1_str)
    utc2 = parse_moment(moment2_str)

    diff = abs((utc2 - utc1).total_seconds()) / (24 * 3600)
    print(int(diff))

if __name__ == "__main__":
    main()



# 415
from datetime import datetime, timedelta
import re
import math

def parse_moment(moment_str):
    """Parse 'YYYY-MM-DD UTC±HH:MM' into a UTC datetime (midnight)."""
    match = re.match(r'(\d{4}-\d{2}-\d{2}) UTC([+-])(\d{2}):(\d{2})', moment_str)
    if not match:
        raise ValueError("Invalid format")
    date_part, sign, hh, mm = match.groups()
    date = datetime.strptime(date_part, "%Y-%m-%d")
    offset_hours = int(hh) + int(mm) / 60
    if sign == '-':
        offset_hours = -offset_hours
    # Local midnight in UTC = local - offset
    return date - timedelta(hours=offset_hours), offset_hours

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_local_midnight(year, month, day, tz_offset):
    """Get UTC time of local midnight in given time zone for a specific date."""
    try:
        if month == 2 and day == 29 and not is_leap(year):
            local_date = datetime(year, 2, 28)
        else:
            local_date = datetime(year, month, day)
    except ValueError:
        local_date = datetime(year, month, day)
    return local_date - timedelta(hours=tz_offset)

def main():
    birth_str = input().strip()
    current_str = input().strip()
    
    # Parse both moments to UTC and get offsets
    birth_utc, birth_offset = parse_moment(birth_str)
    current_utc, current_offset = parse_moment(current_str)
    
    # Get birth month/day from original birth local time
    birth_local = birth_utc + timedelta(hours=birth_offset)
    birth_month = birth_local.month
    birth_day = birth_local.day
    
    # Current year's birthday candidate
    current_year = (current_utc + timedelta(hours=current_offset)).year
    
    # Try birthday in current year
    candidate_utc = get_local_midnight(current_year, birth_month, birth_day, birth_offset)
    
    # If candidate is before current moment, try next year
    if candidate_utc < current_utc:
        candidate_utc = get_local_midnight(current_year + 1, birth_month, birth_day, birth_offset)
    
    # Calculate days until birthday (ceiling)
    delta = candidate_utc - current_utc
    days = math.ceil(delta.total_seconds() / 86400)
    
    print(days)

if __name__ == "__main__":
    main()



# 416
from datetime import datetime, timedelta
import re

def parse_timestamp(ts_str):
    """Parse 'YYYY-MM-DD HH:MM:SS UTC±HH:MM' into a UTC datetime."""
    # Example: "2026-01-01 10:00:00 UTC+03:00"
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC([+-])(\d{2}):(\d{2})', ts_str)
    if not match:
        raise ValueError("Invalid format")
    
    datetime_part, sign, hh, mm = match.groups()
    dt = datetime.strptime(datetime_part, "%Y-%m-%d %H:%M:%S")
    
    offset_hours = int(hh) + int(mm) / 60
    if sign == '-':
        offset_hours = -offset_hours
    
    # Convert to UTC: UTC = local - offset
    return dt - timedelta(hours=offset_hours)

def main():
    start_str = input().strip()
    end_str = input().strip()
    
    start_utc = parse_timestamp(start_str)
    end_utc = parse_timestamp(end_str)
    
    duration = int((end_utc - start_utc).total_seconds())
    print(duration)

if __name__ == "__main__":
    main()



# 417
import math

def segment_in_circle_length(R, x1, y1, x2, y2):
    # Vector from P1 to P2
    dx = x2 - x1
    dy = y2 - y1
    seg_len_sq = dx*dx + dy*dy
    seg_len = math.sqrt(seg_len_sq)
    
    # Distances squared from origin
    d1_sq = x1*x1 + y1*y1
    d2_sq = x2*x2 + y2*y2
    
    # Both endpoints inside circle
    if d1_sq <= R*R and d2_sq <= R*R:
        return seg_len
    
    # Solve quadratic a t^2 + b t + c = 0 for t in [0,1]
    a = seg_len_sq
    b = 2 * (x1*dx + y1*dy)
    c = d1_sq - R*R
    
    # If segment is a point
    if a == 0:
        return 0.0 if d1_sq > R*R else 0.0  # point outside -> 0, inside -> 0 length
    
    disc = b*b - 4*a*c
    if disc < 0:
        return 0.0  # no intersection
    
    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)
    
    # Sort t values
    t_enter = min(t1, t2)
    t_exit = max(t1, t2)
    
    # Clip to [0,1]
    t_enter = max(0.0, t_enter)
    t_exit = min(1.0, t_exit)
    
    if t_exit <= t_enter:
        return 0.0
    
    return seg_len * (t_exit - t_enter)

def main():
    R = float(input().strip())
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    
    length = segment_in_circle_length(R, x1, y1, x2, y2)
    print(f"{length:.10f}")

if __name__ == "__main__":
    main()



# 418
def main():
    xa, ya = map(float, input().split())
    xb, yb = map(float, input().split())
    
    t = ya / (ya + yb)
    xr = xa + t * (xb - xa)
    yr = 0.0
    
    print(f"{xr:.10f} {yr:.10f}")

if __name__ == "__main__":
    main()



# 419
import math

def solve():
    try:
        r = float(input().strip())
        x1, y1 = map(float, input().split())
        x2, y2 = map(float, input().split())
        
        # Basic distances
        dist_sq = (x2 - x1)**2 + (y2 - y1)**2
        dist_ab = math.sqrt(dist_sq)
        
        # Check if direct path is possible
        # Distance from origin to line AB
        cross_product = abs(x1 * y2 - y1 * x2)
        h = cross_product / dist_ab
        
        # Check if origin projection is within segment AB using dot products
        dot1 = (x2 - x1) * (-x1) + (y2 - y1) * (-y1)
        dot2 = (x1 - x2) * (-x2) + (y1 - y2) * (-y2)
        
        if h >= r or dot1 <= 0 or dot2 <= 0:
            print(f"{dist_ab:.10f}")
        else:
            # Path is blocked by the circle
            oa = math.sqrt(x1**2 + y1**2)
            ob = math.sqrt(x2**2 + y2**2)
            
            # Lengths of tangents
            s1 = math.sqrt(oa**2 - r**2)
            s2 = math.sqrt(ob**2 - r**2)
            
            # Angles
            gamma = math.acos(max(-1, min(1, (x1*x2 + y1*y2) / (oa*ob))))
            alpha = math.acos(r / oa)
            beta = math.acos(r / ob)
            
            theta = gamma - alpha - beta
            arc_len = r * theta
            
            print(f"{(s1 + s2 + arc_len):.10f}")
            
    except (EOFError, ValueError):
        pass

solve()



# 420
def main():
    t = int(input().strip())
    g = 0  # global
    n = 0  # nonlocal (in outer)
    # inner's local variable is created per command but doesn't persist

    for _ in range(t):
        scope, val = input().split()
        val = int(val)

        if scope == "global":
            g += val
        elif scope == "nonlocal":
            n += val
        elif scope == "local":
            # does nothing to g or n
            pass

    print(g, n)

if __name__ == "__main__":
    main()



# 421
import importlib

def classify(module_path, attr):
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        return "MODULE_NOT_FOUND"

    if not hasattr(module, attr):
        return "ATTRIBUTE_NOT_FOUND"

    obj = getattr(module, attr)
    if callable(obj):
        return "CALLABLE"
    else:
        return "VALUE"

def main():
    n = int(input().strip())
    for _ in range(n):
        mod_path, attr = input().split()
        print(classify(mod_path, attr))

if __name__ == "__main__":
    main()

