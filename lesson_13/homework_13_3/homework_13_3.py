import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

tree = ET.parse('groups.xml')
root = tree.getroot()

for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        incoming = timing_exbytes.find('incoming')
        if incoming is not None:
            logger.info(f"Group: {group.find('name').text}, incoming: {incoming.text}")
        else:
            logger.info(f"Group: {group.find('name').text}, incoming: Не знайдено")
