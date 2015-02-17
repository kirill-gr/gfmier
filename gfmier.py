import re

def parse_file(f):
    spaces = re.compile(r'\s+')
    def nospaces(line):
        return spaces.sub(' ', line)

    concat_count = 0
    break_count = 0
    parsed = []

    line_continued = ''
    for line in f:
        line_strip = line.strip()
        new_line = ''
        if line_strip:
            if line_strip[-1] == '|':
                if line_continued:
                    line = nospaces(line_continued + line) + '\r\n'
                    concat_count += 1
                    line_continued = ''
            elif line_continued or line_strip[0] == '|':
                line_continued += line + '<br>'
                break_count += 1
        if not line_continued:
            parsed.append(line)
    return parsed, concat_count, break_count

def main():
    import sys
    try:
        with open(sys.argv[1], encoding='utf_8') as f:
            parsed, concat_count, break_count = parse_file(f)            
    except FileNotFoundError as e:
        print('File "%s" not found' % e.filename)
        quit()
    if break_count > 0:
        with open(sys.argv[1], mode='w', encoding='utf_8') as f:
                for line in parsed:
                    f.write(line)
        print('%d <br> added to %d rows' % (break_count, concat_count))
    else:
        print('Nothing to replace')
                
if __name__ == '__main__':
    main()
