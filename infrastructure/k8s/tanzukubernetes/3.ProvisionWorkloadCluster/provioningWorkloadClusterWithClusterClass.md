# Provisioning Workload Cluster with Cluster Class

[provisioning Workload Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/using-tkg-service-with-vsphere-supervisor/provisioning-tkg-service-clusters/workflow-for-provisioning-tkg-clusters-using-kubectl.html)

Cluster Class is a new feature in vSphere with Tanzu that allows you to define a set of reusable configurations for Kubernetes clusters. This feature simplifies the process of creating and managing clusters by providing a template-like structure that can be customized and reused.

[example Cluster Class yaml](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/using-tkg-service-with-vsphere-supervisor/provisioning-tkg-service-clusters/using-the-cluster-v1beta1-api/v1beta1-example-custom-cluster-based-on-the-default-clusterclass.html)

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  name: cluster-custom
  namespace: tkg-cluster-ns
spec:
  clusterNetwork:
    services:
      cidrBlocks: ["10.196.0.0/12"]
    pods:
      cidrBlocks: ["192.168.0.0/16"]
    serviceDomain: "cluster.local"
  topology:
    class: tanzukubernetescluster
    version: v1.30.1---vmware.1-fips-tkg.5
    controlPlane:
      replicas: 3
    workers:
      machineDeployments:
        - class: node-pool
          name: node-pool-1
          replicas: 3
          variables:
            overrides:
            - name: vmClass
              value: guaranteed-xlarge
    variables:
      - name: vmClass
        value: guaranteed-medium
      - name: storageClass
        value: tkg-storage-profile
      - name: defaultStorageClass
        value: tkg-storage-profile
      - name: nodePoolVolumes
        value:
          - name: containerd
            capacity:
              storage: 50Gi
            mountPath: /var/lib/containerd
            storageClass: tkg-storage-profile
          - name: kubelet
            capacity:
              storage: 50Gi
            mountPath: /var/lib/kubelet
            storageClass: tkg-storage-profile
```
[example Cluster Class yaml with annotated explanations](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/using-tkg-service-with-vsphere-supervisor/provisioning-tkg-service-clusters/using-the-cluster-v1beta1-api/v1beta1-example-default-cluster.html#GUID-607BA980-E3E3-4167-ABC8-B9FCDCF44746-en) 

[definitions of kubernetesClusterClass (the default cluster class)](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-supervisor/8-0/using-tkg-service-with-vsphere-supervisor/provisioning-tkg-service-clusters/using-the-cluster-v1beta1-api/cluster-v1beta1-api.html#GUID-69E52B31-6DEC-412D-B60E-FE733156F708-en)