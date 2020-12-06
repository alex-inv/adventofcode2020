import re

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
        passport[key] = attr[attr.find(":") + 1:]

passports.append(passport.copy())

counter = 0


def valid_byr(psp):
    byr = int(psp.get('byr'))
    print('byr = ' + str(byr))
    if 1920 <= byr <= 2002:
        print('byr valid')
        return True
    else:
        print('byr invalid')
        return False


def valid_iyr(psp):
    iyr = int(psp.get('iyr'))
    print('iyr = ' + str(iyr))
    if 2010 <= iyr <= 2020:
        print('iyr valid')
        return True
    else:
        print('iyr invalid')
        return False


def valid_eyr(psp):
    eyr = int(psp.get('eyr'))
    print('eyr = ' + str(eyr))
    if 2020 <= eyr <= 2030:
        print('eyr valid')
        return True
    else:
        print('eyr invalid')
        return False


def valid_hgt(psp):
    hgt = psp.get('hgt')
    print('hgt = ' + hgt)
    if hgt[-2:] == 'cm':
        if 150 <= int(hgt[:-2]) <= 193:
            print('hgt valid')
            return True
        else:
            print('hgt invalid')
            return False
    elif hgt[-2:] == 'in':
        if 59 <= int(hgt[:-2]) <= 76:
            print('hgt valid')
            return True
        else:
            print('hgt invalid')
            return False


def valid_hcl(psp):
    hcl = psp.get('hcl')
    print('hcl = ' + hcl)
    if bool(re.match(r"^#[a-f0-9]{6}$", hcl)):
        print('hcl valid')
        return True
    else:
        print('hcl invalid')
        return False


def valid_ecl(psp):
    ecl = psp.get('ecl')
    print('ecl = ' + ecl)
    if bool(re.match(r"^(amb|blu|brn|gry|grn|hzl|oth)$", ecl)):
        print('ecl valid')
        return True
    else:
        print('ecl invalid')
        return False


def valid_pid(psp):
    pid = psp.get('pid')
    print('pid = ' + pid)
    if bool(re.match(r"^\d{9}$", pid)):
        print('pid valid')
        return True
    else:
        print('pid invalid')
        return False


for psp in passports:
    if ('byr' in psp and valid_byr(psp)
            and 'iyr' in psp and valid_iyr(psp)
            and 'eyr' in psp and valid_eyr(psp)
            and 'hgt' in psp and valid_hgt(psp)
            and 'hcl' in psp and valid_hcl(psp)
            and 'ecl' in psp and valid_ecl(psp)
            and 'pid' in psp and valid_pid(psp)
    ):
        counter += 1

print(counter)
