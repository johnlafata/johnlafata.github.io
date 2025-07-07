# Infrastructure Review

Running Kubernetes on a vSAN stretched cluster using vSphere Kubernetes Service (VKS) provides a robust solution for high availability and disaster recovery. This guide outlines the requirements and considerations for deploying Kubernetes clusters in such an environment.

[Requirements for Running vSphere Supervisor on vSAN Stretched Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/running-vsphere-supervisor-on-vsan-stretched-cluster/overview-of-running-vsphere-iaas-control-plane-on-vsan-stretched-cluster/requirements-for-running-vsphere-iaas-control-plane-on-vsan-stretched-cluster-deployments.html)

A crucial aspect of deploying Kubernetes on a vSAN stretched cluster is ensuring that the vSphere Supervisor Cluster is properly configured. This includes meeting the networking prerequisites for running vSphere Supervisor on a vSAN stretched cluster, which are outlined in the VMware documentation and referenced below for AVI Load Balancer Deployment and HA Proxy Load Balancer Deployment on VDS Networking.

[Requirements for Cluster Supervisor Deployment with Avi Load Balancer and VDS Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/vsphere-supervisor-concepts-and-planning/requirements-for-enabling-a-single-cluster-supervisor/requirements-for-cluster-supervisor-deployment-with-nsx-advanced-load-balancer-and-vds-networking.html)

[Requirements for Cluster Supervisor Deployment with HA proxy Load Balancer and VDS Networking](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/vsphere-supervisor-concepts-and-planning/requirements-for-enabling-a-single-cluster-supervisor/requirements-for-cluster-supervisor-deployment-with-vds-networking-and-haproxy-load-balancer.html)

