def truncate(cases):
    for case in cases:
        limit, string = case

        if limit == 0:
            print();
            continue;
            
        # (last_byte & 0xC0) == 0x80 means byte starts with 10 (part of a multi-byte character)
        while limit > 0 and limit < len(string) and (string[limit] & 0xC0) == 0x80:
            limit -= 1
        string = string[:limit]

        print(string.decode('utf-8'))
    
if __name__ == "__main__":
    cases = []
    with open("/Users/ab/Desktop/projects/CS-primer/ComputerSystems/Bits-and-bytes/UTF-8-truncate/cases", "rb") as file:
        for line in file:
            line = line.rstrip(b'\n')
            limit = line[0]
            string = line[1:]
            cases.append((limit, string))

    truncate(cases)
    print('ok')