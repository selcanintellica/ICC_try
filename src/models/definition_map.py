from typing import Dict, Any

TEMPLATES: Dict[str, Dict[str, Any]] = {
    "SENDEMAIL": {
        "template_id": "110673709194435",
        "definitions": {
            "customer_id": "110673709476681",
            "sql_or_attachment_query": "110673709444744",
            "to": "110673709461441",
            "cc": "110673709490605",
            "subject": "110673709380478",
            "body": "110673709424784",
            "is_html": "1600766934",
        },
        "props_name": "SENDEMAIL",
    },
    "READSQL": {
        "template_id": "2223045341865624",
        "definitions": {
            "customer_id": "2223045341969932",
            "sql": "2223045341935949",
            "columns_json": "2223045341958051",
            "paginate": "28405919373737",        # "true"/"false"
            "limit": "28405919100373",
            "output_name": "28405919737373",
            "output_path": "28405919059373",
            "overwrite": "28405919526172",
            "opt_a": "284961720523",
            "opt_b": "284961720524",
            "return_json": "284961720525",
            "return_csv": "284961720526",
        },
        "props_name": "readsql",
    },
    "WRITEDATA": {
        "template_id": "28405918884279",
        "definitions": {

            "job_context": "28405919074002",     # value, jobName, folder
            "columns_schema_json": "28405919027068",
            "job_id": "28405918976213",
            "customer_id": "28405919100547",
            "database": "28405919042037",
            "table": "28405919059935",
            "write_mode": "28405919008625",
            "use_temp": "28405919087238",
            "create_if_missing": "28405919100737",
            "partitioned": "28405919839465",
            "batch_size": "28405919193743",
            "note": "28405919284178",
            "tags": "28405919372169",
        },
        "props_name": "writedata",
    },
}


DEFAULT_PRIORITY = "Normal"
DEFAULT_ACTIVE = "true"
DEFAULT_SKIP = "false"
DEFAULT_FOLDER = "3023602439587835"
DEFAULT_RIGHTS_OWNER = "184431757886694"
