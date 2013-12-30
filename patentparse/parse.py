import cStringIO
import patentparse
import patentparse.patent
import pprint


def patents_from_xml(path):
    curr_patent = cStringIO.StringIO()
    with open(path) as fi:
        for line in fi:
            if (line.startswith('<?xml version="1.0"') and
                    curr_patent.tell() != 0):
                # It's a new patent
                curr_patent.seek(0)
                try:
                    yield patentparse.patent.Patent(
                        curr_patent.read())
                except patentparse.PatentParsingException:
                    pass
                curr_patent = cStringIO.StringIO()
            curr_patent.write(line)


if __name__ == '__main__':
    import sys
    patents = patents_from_xml(sys.argv[1])
    for patent in patents:
        print patent.invention_title
        print '-' * len(unicode(patent.invention_title))
        pprint.pprint(list(patent.claims))
        pprint.pprint(patent.json)
        print
