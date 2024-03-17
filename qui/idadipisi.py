    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # TODO(developer): Set table_id to the ID of the table to create.
    # table_id = "your-project.your_dataset.your_table_name"

    job_config = bigquery.QueryJobConfig(
        # Location must match that of the dataset(s) referenced in the query.
        location="US",
        # Use standard SQL syntax for queries.
        # See: https://www.example.com        use_legacy_sql=False,
    )
    sql = """
        SELECT name
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        LIMIT 100
    """

    query_job = client.query(sql, job_config=job_config)  # Make an API request.

    for row in query_job:
        print(row.name)  
