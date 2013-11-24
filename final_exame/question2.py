total_count = 0
count = 0

for a in range(3):
    for b in range(3):
        for c in range(3):
            total_count += 1
            if ( a == b and a == c ) or (a != b and a != c and b != c ):
                continue
            count += 1
print count
