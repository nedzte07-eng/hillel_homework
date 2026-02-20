import csv
import os
import logging

import xmltodict
import json

from constant import INITIAL_DATA_XMLS_LESSON_16, INITIAL_DATA_CSVS_LESSON_16, INITIAL_DATA_JSONS_LESSON_16, \
    PROCESSED_DATA_CSVS_LESSON_16, PROCESSED_DATA_JSONS_LESSON_16

with open(INITIAL_DATA_XMLS_LESSON_16 / 'groups.xml', mode='r') as file:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    # logger.info(f"Path to XMLs: {INITIAL_DATA_XMLS_LESSON_16}")
    data_xml = file.read()
    data_xml_parse = xmltodict.parse(data_xml)
    incoming_values = []
    for group in data_xml_parse['groups']['group']:
        timing = group.get('timingExbytes')
        if timing and 'incoming' in timing:
            incoming_values.append(timing['incoming'])

    logger.info(f"timingExbytes/incoming: {incoming_values}")


def csv_unduplicates(filename='r-m-c.csv'):
    unduplicates_csv = []
    with open(INITIAL_DATA_CSVS_LESSON_16 / filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row not in unduplicates_csv:
                unduplicates_csv.append(row)

    headers = unduplicates_csv[0]
    payload = unduplicates_csv[1:]
    with open(PROCESSED_DATA_CSVS_LESSON_16 / f'nedzelnytskyi_{filename}', mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in payload:
            writer.writerow(row)


csv_unduplicates()
csv_unduplicates('random-michaels.csv')


def is_valid_json(file_json: str) -> bool:
    logging.basicConfig(
        filename=PROCESSED_DATA_JSONS_LESSON_16 / "json_nedzelnytskyi.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    try:
        with open(INITIAL_DATA_JSONS_LESSON_16 / file_json, "r", encoding="utf-8") as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print("Failure:", e)
        logging.error("Failure in file %s: %s", file_json, e)
        return False


for pass_to_file, _, files in os.walk(INITIAL_DATA_JSONS_LESSON_16):
    if '.venv' in pass_to_file:
        continue

    for file in files:
        if file.endswith('.json'):
            json_name = file
            print(json_name)
            print(is_valid_json(json_name))
