import csv

import xmltodict

from constant import INITIAL_DATA_XMLS_LESSON_16, INITIAL_DATA_CSVS_LESSON_16, PROCESSED_DATA_CSVS_LESSON_16
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

with open(INITIAL_DATA_XMLS_LESSON_16 / 'groups.xml', mode='r') as file:
    # logger.info(f"Path to XMLs: {INITIAL_DATA_XMLS_LESSON_16}")
    data_xml = file.read()
    data_xml_parse = xmltodict.parse(data_xml)
    incoming_values = []
    for group in data_xml_parse['groups']['group']:
        timing = group.get('timingExbytes')
        if timing and 'incoming' in timing:
            incoming_values.append(timing['incoming'])

    logger.info(f"timingExbytes/incoming: {incoming_values}")


def csv_unduplicates(filename = 'r-m-c.csv'):
    unduplicates_csv = []
    with open(INITIAL_DATA_CSVS_LESSON_16 / filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row not in unduplicates_csv:
                unduplicates_csv.append(row)

    headers = unduplicates_csv[0]
    payload = unduplicates_csv[1:]
    with open(PROCESSED_DATA_CSVS_LESSON_16 / filename, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in payload:
            writer.writerow(row)

csv_unduplicates()
csv_unduplicates('random-michaels.csv')
