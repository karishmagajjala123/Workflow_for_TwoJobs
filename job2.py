import boto3
import io
import pandas as pd
import sys
from awsglue.utils import getResolvedOptions

glue_client = boto3.client("glue")
args = getResolvedOptions(sys.argv, ['WORKFLOW_NAME', 'WORKFLOW_RUN_ID'])
workflow_name = args['WORKFLOW_NAME']
workflow_run_id = args['WORKFLOW_RUN_ID']
workflow_params = glue_client.get_workflow_run_properties(Name=workflow_name, RunId=workflow_run_id)["RunProperties"]

file_name = workflow_params['file_name'] 

client = boto3.client('s3')
s3 = boto3.resource('s3')

obj = client.get_object(Bucket='workflow', Key=file_name)

df = pd.read_csv(obj['Body'])

jsonBuffer = io.StringIO()

df.head(10).to_json(jsonBuffer,orient='records');

s3.Bucket('workflow').put_object(Key='out2/customers2.csv', Body = jsonBuffer.getvalue())