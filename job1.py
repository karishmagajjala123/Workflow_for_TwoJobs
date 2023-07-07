import boto3
import io
import pandas as pd
import sys
from awsglue.utils import getResolvedOptions

file_name = 'out1/customers1.csv'

client = boto3.client('s3')
s3 = boto3.resource('s3')

obj = client.get_object(Bucket='workflow', Key='in/customers.csv')

df = pd.read_csv(obj['Body'])

jsonBuffer = io.StringIO()

df.head(10).to_json(jsonBuffer,orient='records');

s3.Bucket('workflow').put_object(Key=file_name, Body = jsonBuffer.getvalue())

glue_client = boto3.client("glue")
args = getResolvedOptions(sys.argv, ['WORKFLOW_NAME', 'WORKFLOW_RUN_ID'])
workflow_name = args['WORKFLOW_NAME']
workflow_run_id = args['WORKFLOW_RUN_ID']
workflow_params = glue_client.get_workflow_run_properties(Name=workflow_name, RunId=workflow_run_id)["RunProperties"]
                                           
workflow_params['file_name'] = file_name
glue_client.put_workflow_run_properties(Name=workflow_name, RunId=workflow_run_id, RunProperties=workflow_params)