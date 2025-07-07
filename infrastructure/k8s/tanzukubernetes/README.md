# vsphere kubernetes deployments on vsan streteched cluster

Over the last few months, I've been involved in two separate projects to deploy Kubernetes clusters on a vSAN stretched cluster using vSphere Kubernetes Service (VKS). This blog entry aims to capture the highlights of these efforts for running Kubernetes workloads in this highly available environment.

## Key Considerations
When deploying Kubernetes on a vSAN stretched cluster, several key considerations must be taken into account:

1. **High Availability**: Ensure that the Kubernetes control plane and etcd are highly available across the stretched cluster.
2. **Networking**: Configure networking to support cross-site communication between Kubernetes nodes.
3. **Storage**: Leverage vSAN's capabilities to provide resilient storage for Kubernetes workloads.
4. **Disaster Recovery**: Implement disaster recovery strategies to protect against site failures.

## Deployment Steps
The deployment process involves several key steps:

1. **Prepare the vSAN Stretched Cluster**: Ensure that the vSAN stretched cluster is properly configured and that all necessary components are in place.

    vSAN stretched clusters are a powerful option for environments that require the highest levels of data resilience and VM uptime. This guide was developed to provide additional insight and information for the design, installation and configuration of vSAN stretched clusters. It will also cover operational procedures and explain how it handles failure scenarios unique to this topology.

    A VMware vSAN stretched cluster is a cluster configuration where the hosts that comprise a vSAN cluster reside in two geographic locations. The two sites typically have an equal number of hosts residing in each site, and are connected using a high bandwidth/low latency connection known as an inter-site link, or ISL. The third site, or tertiary site hosts a vSAN Witness Host that is connected to both data sites. This connectivity can be via low bandwidth/high latency links.

    ### references

    [vSAN Stretched Cluster Guide](https://core.vmware.com/resource/vsan-stretched-cluster-guide#introduction)


2. **Review the Pre-requisites**: Ensure that the vSphere environment meets the prerequisites for deploying VKS, including the necessary licenses and configurations.

    * [Infrastructure Review](./0.SetupVSanStretchedCluster/InfrastructureReview.md)

    * [HA/DRS](./1.ConfigurePreReqs/0.%20HA-DRS%28fully-automated%29.md)
    * [Storage Policy Configuration](./1.ConfigurePreReqs/1.%20StoragePolicy.md)
    * [Availability Zones](./1.ConfigurePreReqs/images/2.AvailabilityZones.md)

    An important aspect to understand before enabling workload management (aka creating a Supervisor Cluster) is the networking used in vks.

    There are 3 important portgroups to create

3. **Deploy vSphere Kubernetes Service (VKS)**: Use the vSphere Client to deploy VKS on the stretched cluster. This involves creating a Supervisor Cluster and configuring it to use the vSAN stretched cluster as the underlying storage.


4. **Configure Kubernetes Networking**: Set up networking to enable communication between Kubernetes nodes across sites.

    When using Avi Load Balancer, install Avi Kubernetes Operator and configure it to manage the load balancer for the Kubernetes control plane and workloads. This ensures that traffic is properly routed across the stretched cluster.

    When using HA proxy, configure the HAProxy Load Balancer to support service type LoadBalancer in Kubernetes. This involves:

    * Deploy the HAProxy Kubernetes Ingress Controller as a DaemonSet or Deployment
    * Configure a service of type LoadBalancer that points to the HAProxy pods
    * Create a ConfigMap with the HAProxy configuration for load balancing across sites
    * The HAProxy configuration should include proper timeouts and retries to accommodate potential latency between sites in the stretched cluster.


    Ensure proper health checks are configured to detect failures between sites

    Apply network policies to allow traffic between the HAProxy instances and Kubernetes services


5. **Deploy Workloads**: Deploy Kubernetes workloads and services, taking advantage of the stretched cluster's capabilities.

    CI/CD solutions that leverage gitOps principles can be used to automate the deployment of Kubernetes workloads. This includes using tools like ArgoCD or Flux to manage the deployment process and ensure that the desired state of the cluster is maintained.

6. **Troubleshooting deployment**: Monitor the deployment process and troubleshoot any issues that arise, ensuring that the Kubernetes control plane and workloads are functioning correctly.

    * [Troubleshooting References for Tanzu Kubernetes Service (TKG) on vSphere](./troubleshooting/troubleshooting-references.md)

    * If necessary to ssh to a cluster node, you can use the following reference:
    [SSH to cluster notes](./troubleshooting/sshToClusterNodes.md)


## Conclusion
Deploying Kubernetes on a vSAN stretched cluster using VKS provides a powerful solution for running highly available workloads. By following best practices and considering key factors, organizations can successfully leverage this architecture to meet their business needs.
