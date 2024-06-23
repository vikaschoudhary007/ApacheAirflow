### Introduction to Apache Airflow

#### Workflow management tool 

- Workflow is a series of tasks that needs to be executed in a specific order.
- Extract - Transform - Load == Workflow

#### In Airflow this workflow is called DAG(Directed Acyclic Graph)
- kind of like a blueprint of all the tasks and their execution order
- Directed -> task moves in one direction
- Acyclic -> No loops in tasks
- Graph -> Visual representation of tasks
- Collection of multiple tasks = DAG

#### Operator 

- Function provided by airflow to create and execute tasks
- Multiple operators available for different functionalities

#### Executors

- To run the entire DAG(in a flow task by task)

### The following example is a simple ETL pipeline 
* To extract data from twitter for any user 
* Transform it into a dataframe to store it as csv file and 
* Load the data finally to a S3 bucket for further analysis

#### Twitter APIS -- V1.0 doesn't work anymore
#### If you have access to v2.0 you will need the following mentioned API keys

- CONSUMER KEY 
- CONSUMER SECRET 
- ACCESS TOKEN 
- ACCESS TOKEN SECRET

#### In case you don't have access to Twitter API use `Nitter` to get user tweets

#### Airflow

- connect to EC2 instance and then create a conda virtual env in EC2 
- In order to connect to EC2 through ssh paste the `.pem` certificate in your `PWD`
- pip3 install "apache-airflow==2.7.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-no-providers-3.11.txt"
- airflow db init
-  airflow users create --username admin --password admin@123 --firstname Jon --lastname Doe --role Admin --email admin@domain.com
- airflow webserver -D
- airflow scheduler -D
- Add new inbound rule under security group in EC2 instance (Custom TCP, 8080, Anywhere IPv4)
- Launch the public IP in browser with 8080 port - Airflow UI(use the above created credentials)
- Copy code to airflow and then run the DAG