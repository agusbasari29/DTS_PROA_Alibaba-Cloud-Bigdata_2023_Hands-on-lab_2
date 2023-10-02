# DTS_PROA_Alibaba-Cloud-Bigdata_2023_Hands-on-lab_2

Use DataService Studio of DataWorks to Publish APIs
1. Introduction
1.1 Knowledge points
This lab uses DataService Studio of Alibaba Cloud DataWorks. It demonstrates how to publish APIs by using DataService Studio of DataWorks. The DataService Studio of DataWorks aims at building a centralized data service bus to help enterprises manage all internal and external APIs. You can quickly create APIs in DataService Studio based on data tables or register existing APIs for centralized management and publishing.

1.2 Lab Steps
Prepare an RDS environment.
Create a DataWorks environment.
Use DataService Studio to create APIs.

1.3 Cloud resources required
ECS
RDS
Dataworks
Api Gateway

1.4 Prerequisites
If you're using your own Alibaba Cloud account instead of the account provided by this lab to operate the lab, please note that you'll need to choose the same Ubuntu 16.04 operating system for your ECS in order to run the lab smoothly.
Before starting the lab, please confirm that the previous lab has been closed normally and exited.




- Start
- open alibaba console with ram user

- Prepare the RDS environment:
    Menu -> Product And Services -> Search(RDS) -> ApsaraDB for RDS.
    Select US (Silicon Valley) Regional -> Instance -> Exact Server was Running properly and then click manage.
    Click Configure Whitelist to configure a whitelist.
    Modify whitelist to "0.0.0.0/0"
    Create Administrator account:
        Account -> Create Account:
            Database account    : labex
            * Privileged Account
            Password            : Aliyun-test
            Confirm Password    : Aliyun-test
            OK
    
    Apply for a public endpoint:
        Database Connection -> Apply for Public Endpoint -> prompt(just OK)
    
    Check on Basic Information

- Import Data
    * Search for Elastic Compute Service
    Go to Instance... -> Silicon Valley Regional -> See IP Public to remote via ssh

    ssh root@21.2.2.1

    apt update && apt -y install git mysql-client

    git clone https://github.com/datacharmer/test_db.git

    cd test_db

    mysql -ulabex -pAliyun-test -hYOUR-RDS-PRVIATE-ADDRESS < employees.sql


    Database Connection -> Internal Endpoint.


- Create a Dataworks Environment:
    Product adn services -> Dataworks
    * Select Regional US (Silicon Valey)

    Workspace->Create workspace
    * Workspace name    : labex0412
    * Mode              : Standard mode
    NEXT

    Check on MaxCompute
    NEXT

    MaxCompute:
    * Instance Display name : labex0614
    Create Workspace

- Add a MySQL data source:
    In Workspace -> Data Integration (on Action Tab)

    Data Source
    Add data source -> select MySQL:
    * Data Source Type  : Connection string mode
    * Data Source Name  : my_mysql
    * Environment       : *Development     *Production
    * JDBC URL          : jdbc:mysql://YOUR-RDS-PUBLIC-ADDRESS:3306/employees
    * User name         : labex
    * Password          : Aliyun-test
    ----------------
    | Data Service |
    ----------------
    Test Connectivity -> Complete


- Use DataService Studio to create APIs
    Product and Services -> search(api) -> choice API Gateway
    Select Regional (US (Silicon Valley))
    API Groups -> Create Group:
    * Group name    : apiGroup1
    * Description   : test
    Confirm -> prompt(Confirm)

    Go to DataSevice Studio on DataWorks/Workspace

    Create Business Process:
    * Business name : labex
    * API Group     : apiGroup1
    OK

- Create an API in wizard mode
    API->New API->Generate API
    * API mode      : wizard mode
    * API Name      : query1
    * API Path      : /query1
    * Description   : test
    Determine


    111035

    Test



- Create an API in script mode
    API->New API->Generate API
    * API mode      : script mode
    * API Name      : query2
    * API Path      : /query2
    * Description   : test2
    Determine


    select d.emp_no, e.first_name, e.last_name, d.from_date, d.to_date from dept_manager d, employees e where d.dept_no = (select dept_no from departments where dept_name = '${dept_name}') and e.emp_no = d.emp_no

    Test


Publish All Queries



- Call API

        import sys
        import urllib.request
        import ssl

        host = 'https://47bcbb0d03324951af88848d803a8a72-us-west-1.alicloudapi.com'
        path = '/query2'
        method = 'GET'
        appcode = 'bb9717fa2b604e51ae039d792c57f9c7'
        querys = 'dept_name=Marketing'
        bodys = {}
        url = host + path + '?' + querys

        request = urllib.request.Request(url)
        request.add_header('Authorization', 'APPCODE ' + appcode)

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        response = urllib.request.urlopen(request, context=ctx)
        content = response.read()
        if (content):
            print(content)

    python3 call.py
