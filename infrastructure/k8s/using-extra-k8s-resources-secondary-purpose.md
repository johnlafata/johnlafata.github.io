# Extra Kubernetes Resources for Secondary Purposes
This document outlines how to use additional Kubernetes resources for secondary purposes, such as using backup capacity for workloads that are not critical - such as testing, development, short-term analysis, etc.
This can help in optimizing resource usage and cost management.
## Using Backup Capacity for Non-Critical Workloads
When you have backup capacity in your Kubernetes cluster, you can utilize it for workloads that are not critical. This can be done by:

# Setting the Priority of a Kubernetes Deployment

Kubernetes allows you to control the priority of pods using PriorityClass resources. By setting priority, you can influence how the scheduler makes decisions about which pods to evict during resource constraints.

## Steps to Set Priority

1. Create a PriorityClass resource:
    ```yaml
    apiVersion: scheduling.k8s.io/v1
    kind: PriorityClass
    metadata:
      name: high-priority
    value: 1000000
    globalDefault: false
    description: "This priority class should be used for critical service pods only."
    ```

2. Reference the PriorityClass in your Deployment spec:
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-deployment
    spec:
      template:
         spec:
            priorityClassName: high-priority
            containers:
            - name: app
              # container details
    ```

## Important Notes
- Higher priority value means higher priority (range: -2147483648 to 1000000000)
- System critical pods use reserved priority values above 1000000000
- If `globalDefault` is set to true, pods without priorityClassName will use this class
- Priority affects scheduling decisions and pod preemption during resource constraints