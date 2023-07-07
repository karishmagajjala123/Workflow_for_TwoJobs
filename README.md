# Workflow_for_TwoJobs
Created two Glue Jobs job1 and job2. The first job will read IMDB-Movie-Data.csv file from the workflowbucket07072023 bucket and write it to movie1.csv to the out1 folder. The first job will write the file name movie1.csv to the workflow property as the state. 
The second job will fetch the file name from the workflow property and then will read movie1.csv file from out1 folder in the workflowbucket07072023 bucket and write movie2.csv to the out2 folder. The jobs will not perform any transformations.
A Glue Workflow which will orchestrate both jobs and the workflow will use workflow properties to share state between the jobs.
