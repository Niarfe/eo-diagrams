sequenceDiagram
    User-->>+pulumiapi: create tenant abc12cde
    pulumiapi-->>-User: http/2 200
    pulumiapi-->>aws_s3: create bucket s3://evi-abc12de-unst-or-data-ingest/
    User-->>aws_s3: add subfolders dms-cdc/study/
    User-->>aws_s3: upload parquet file to s3://evi-abc12de-unst-or-data-ingest/dms-cdc/study/
    Ingest-->>+aws_s3: taf gile for load to snowflake
    Ingest-->>sf_sga45941: file loaded into snowflake
    User-->>sf_sga45941: use role abc12cde_ingester
    User-->>sf_sga45941: Look in table ABC12CDE_RAW.STUDY.STUDY, there should be data 

