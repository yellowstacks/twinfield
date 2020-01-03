import logging
from datetime import datetime

import requests

from scripts import functions, soap_bodies


def read_offices(param):
    url = 'https://{}.twinfield.com/webservices/processxml.asmx?wsdl'.format(param.cluster)
    body = soap_bodies.soap_offices(param.session_id)
    response = requests.post(url=url, headers=param.header, data=body)

    data = functions.parse_session_response(response, param)
    data.to_excel('offices.xlsx', index = False)

    return data


def read_030_1(param, jaar, periode):
    start = datetime.now()

    logging.info('start request {} periode van {} t/m {}'.format(jaar, periode['from'], periode['to']))

    url = 'https://{}.twinfield.com/webservices/processxml.asmx?wsdl'.format(param.cluster)
    body = soap_bodies.soap_030_1(param.session_id, jaar, periode)
    response = requests.post(url=url, headers=param.header, data=body)

    data = functions.parse_response(response, param)

    logging.info('{} records in {}'.format(len(data), datetime.now() - start))

    return data


def read_metadata(module, param):
    metadata = functions.get_metadata(module=module, param=param)
    fieldmapping = metadata['label'].to_dict()

    return fieldmapping


def read_164(param):
    start = datetime.now()

    logging.info('start request credit management')

    url = 'https://.twinfield.com/webservices/processxml.asmx?wsdl'.format(param.cluster)
    body = soap_bodies.soap_164(param.session_id)
    response = requests.post(url=url, headers=param.header, data=body)

    data = functions.parse_response(response, param)

    logging.info('{} records in {}'.format(len(data), datetime.now() - start))

    return data
