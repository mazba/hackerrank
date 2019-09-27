def repeatedString(s, n):
    string_len = len(s)
    min_repeat = int(n/string_len)
    a_occurrence = s.count('a')
    num_of_repeat = a_occurrence*min_repeat
    end_gap = n-(string_len*min_repeat)
    if end_gap > 0:
        num_of_repeat += s[:end_gap].count('a')
    return num_of_repeat
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = 10
    s = "abc"
    result = repeatedString(s, n)
    print(result)