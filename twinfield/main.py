import logging

import azure.functions as func

from .pull_data import import_all
from .upload import upload_all
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.serverless import serverless_function
from .functions import RunParameters

sentry_sdk.init(
    "https://03f0371227ad473a89d7358c89c2e6c5@o472336.ingest.sentry.io/5515670",
    traces_sample_rate=1.0,
)

load_dotenv()


@serverless_function
def run(run_params):
    if run_params.refresh:
        import_all(run_params)

    if run_params.upload:
        upload_all(run_params)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    options = {
        "100": "openstaande_debiteuren",
        "200": "openstaande_crediteuren",
        "030_1": "mutaties",
        "040_1": "consolidatie",
    }

    module = req.params.get("module")
    jaar = req.params.get("jaar")

    if not jaar:
        jaar = "2020"
    else:
        jaar = req_body.get("jaar")

    if not module:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            module = req_body.get("module")

    if module:

        run_params = RunParameters(
            jaar=jaar, refresh=True, upload=True, modules=["040_1"], offices=[], rerun=False
        )
        run(run_params)

        return func.HttpResponse(
            f"Script {module} van Twinfield is afgerond. Zie teams voor het resultaat"
        )
    else:
        return func.HttpResponse(
            f"Script is niet opgegeven of niet bekend geef met parameter 'script' "
            f"aan welk module je wil draaien, te kiezen uit {', '.join(options.keys())}.",
            status_code=200,
        )
