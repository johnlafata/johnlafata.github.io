# Running Prometheus on AWS Fargate. 

Prometheus can monitor pods running on Fargate, and you can use it to gain visibility into your containerized workloads. [1, 2, 3, 4]  
How to set up Prometheus on AWS Fargate [2, 5]  
1. Create a Prometheus-enabled AWS Fargate task 
2. Configure Node Groups 
3. Install AWS EBS CSI driver 
4. Install Prometheus 
5. Install Grafana 

Prometheus on AWS Fargate with Amazon Managed Service [6]  
• You can use Amazon Managed Service for Prometheus to collect metrics for your Amazon EKS cluster [6]  
• You can use the service's metrics path and port to allow the Prometheus collector to discover the service [7]  

Using Prometheus with Grafana [8]  
• You can use Grafana to visualize the metrics stored in Prometheus in dashboards 

Monitoring with Prometheus [9]  
• You can use Prometheus to monitor issues and alerts such as tasks in crash loops, unprogrammed failures, and CPU throttling 
• You can customize the configuration to include or drop metrics 


Generative AI is experimental.

[1] https://aws.amazon.com/blogs/containers/monitoring-amazon-eks-on-aws-fargate-using-prometheus-and-grafana/[2] https://aws.amazon.com/blogs/mt/monitor-and-scale-your-amazon-ecs-on-aws-fargate-application-using-prometheus-metrics/[3] https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-onboard-ingest-metrics-existing-Prometheus-fargate.html[4] https://www.youtube.com/watch?v=Wk0h3aGtlUo[5] https://dev.to/aws-builders/setup-prometheus-and-grafana-with-existing-eks-fargate-cluster-monitoring-39he[6] https://www.youtube.com/watch?v=1_SAP7QkRlU[7] https://medium.com/cloud-native-daily/configuring-fargate-custom-application-metrics-in-cloudwatch-using-prometheus-6340530a701b[8] https://www.datadoghq.com/blog/tools-for-collecting-aws-fargate-metrics/[9] https://sysdig.com/blog/monitor-aws-fargate-prometheus/
Not all images can be exported from Search.
