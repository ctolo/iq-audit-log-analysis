#!/usr/bin/env python3

import json
import sys


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        raise Exception("Usage: " + argv[0] + " file")

    with open(argv[1], mode='r') as f:
        lines = f.readlines()

    print('Application Name,Stage,Scan ID,Time,Application Public ID,Application ID')
    for line in lines:
        record = json.loads(line.strip())
        if record['domain'] == 'governance.evaluation.application':
            data = record['data']
            print('%s,%s,%s,%s,%s,%s' % 
            (data['applicationName'], data['stageId'], data['scanId'], record['timestamp'], data['applicationPublicId'],data['applicationId']))

if __name__ == "__main__":
    sys.exit(main()) 
