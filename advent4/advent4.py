file_name = "../input/input4.txt"
my_file = open(file_name)

passports = []
lines = list(map(lambda s: s.strip(), my_file.readlines()))

passport = {}
for line in lines:
    if line == "":
        passports.append(passport.copy())
        passport = {}
        continue

    for attr in line.split(" "):
        key = attr[:attr.find(":")]
        passport[key] = True

passports.append(passport.copy())

counter = 0
for psp in passports:
    if ('byr' in psp
            and 'iyr' in psp
            and 'eyr' in psp
            and 'hgt' in psp
            and 'hcl' in psp
            and 'ecl' in psp
            and 'pid' in psp
    ):
        counter += 1

print(counter)
