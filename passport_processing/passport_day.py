import re
# https://adventofcode.com/2020/day/4
# https://adventofcode.com/2020/day/4#part2

# check every requirement field as valid, treat cid field as optional
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def dicts_within_list(inp):
    # eyr:2029 iyr:2013 
    passports = []                  # a list for mutiple dict
    passport = {}                   # a dict
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    for line in inp:
        # important because it check the line for \n first for every new line
        if line != "\n": 
            #print('his is an in statement:', line)          # his is an in statement: ecl:blu byr:1939
            # orgininally, everyline has \n. This is how to handle/format them out first before putting into a dict.
            line = line.rstrip().split(" ")                 # remove \n with .rstrip. .split for space and replacing it with , ''     [] are placed upon because thats how split work       
            #print(line)                                    # ['eyr:2029', 'iyr:2013']                                                    before split ---> eyr:2029 iyr:2013     
                                                                                # for every element In the line, doing this because is in a list and not 1 string only.          
            line = [in_parenthesis.split(":") for in_parenthesis in line]       # separate to make keys and values where : are and replacing it with , '' and [] worked around it because is each element ---> anything inside parenthesis'' count as element
                                                                                # The [] is to contain lists within a list in one line.          
            #print(line)                                     # [['eyr', '2029'], ['iyr', '2013']]                                                         nomral split without list ---> ['eyr', '2029'], ['iyr', '2013']

            # making an acutal dict
            for field in line:                               # for every element in each list (each list count as element too)   
                passport[field[0]] = field[1]                # put each list as a dict using indexes [0] as key, [1] as value with : .Basically replacing , with : .That way dict can understand and be use. Since it is each element it will know its index 
            #print(passport)                                 # {'eyr': '2029', 'iyr': '2013'} --->  {'eyr': '2029', 'iyr': '2013', 'hcl': '#ceb3a1', 'byr': '1939', 'ecl': 'blu', 'hgt': '163cm', 'pid': '660456119'}
        else:                                                # this is to handle the line with \n, without else statatement it will give index error because it's an empty space when there is only field [0] and [1] which dont exist
            #print('this is else statement:',line)           # this is else statement:   
            passports.append(passport)                       # Separate each dict by adding the previous created dict into a list
            passport = {}                                    # reset the dict after adding it to the list, so it can in add a new one without the previous ones which interfere the key/value. Organize the dictionary, so it is the correct order list the file
            #print(passports)                                
        #print(passports)
    passports.append(passport)                              # add the last dict since there won't be new line
    #print('this is a dict: ', passport)                     
    print('this is a dict within a List: ', passports)
    return passports


def check_passport(passports):
    s1 = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    s2 = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])

    test_num = 0
    total = 0
    total_invalid = 0

    for field in passports:
        test_num += 1

    for field in passports:
        if s1.issubset(field) or s2.issubset(field):
            #print('Valid')
            total += 1
        else:
            #print('Invalid')
            total_invalid += 1

def check_field():
    pass


def test_field():
    byr = 'byr'
    pass


if __name__ == "__main__":
    with open('input.txt') as inp:
        passports = dicts_within_list(inp)
    check_passport(passports)