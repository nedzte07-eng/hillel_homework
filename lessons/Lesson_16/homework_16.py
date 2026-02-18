import xmltodict

from constant import INITIAL_DATA_XMLS_LESSON_16
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

with open(INITIAL_DATA_XMLS_LESSON_16/'groups.xml', mode='r') as file:
    logger.info(f"Path to XMLs: {INITIAL_DATA_XMLS_LESSON_16}")
    data_xml = file.read()
    data_xml_parse = xmltodict.parse(data_xml)
    print(data_xml_parse)
    incoming_values = []
    for group in data_xml_parse['groups']['group']:
        timing = group.get('timingExbytes')
        if timing and 'incoming' in timing:
            incoming_values.append(timing['incoming'])

    logger.info(f"timingExbytes/incoming: {incoming_values}")

# print(data_xml)
# print(data_xml_parse)