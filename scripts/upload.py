import logging
from .functions import import_files
from .export import upload_data


def upload_all(run_params, start):
    logging.info("start met uploaden van datasets")

    data = import_files(run_params, "transactions")
    upload_data(run_params.jaar, data, start, run_params)

    sv = import_files(run_params, "summary")
    upload_data("sv_" + run_params.jaar, sv, start, run_params)