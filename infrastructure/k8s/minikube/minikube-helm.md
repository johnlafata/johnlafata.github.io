`brew install kubernetes-helm`

Response:
```
Updating Homebrew...
==> Auto-updated Homebrew!
Updated Homebrew from eac74ec6e to 3aa762428.
Updated 5 taps (cloudfoundry/tap, homebrew/core, homebrew/cask, pivotal/tap and warrensbox/tap).
==> New Formulae
awsume            grin              minikube          ngt               pylint            wal2json
comby             grin-wallet       mpi4py            oauth2l           tdkjs
dvc               javacc            mpv               onefetch          tektoncd-cli
gmt@5             jd                navi              pnpm              toast
govc              manticoresearch   nbdime            prestosql         ttyplot
==> Updated Formulae
azure-cli ✔                          fossil                               php
cloudfoundry/tap/bosh-cli ✔          frpc                                 php-code-sniffer
cloudfoundry/tap/cf-cli ✔            frps                                 php-cs-fixer
docker ✔                             frugal                               php@7.1
git ✔                                fstrm                                php@7.2
go ✔                                 futhark                              phpstan
gradle ✔                             fwup                                 phpunit
grafana ✔                            gatsby-cli                           picard-tools

...

firebase-cli                         packer                               youtube-dl
flake8                               paket                                yq
flintrock                            pango                                zabbix
flow                                 pdftk-java                           zbar
fluid-synth                          percona-server                       zita-convolver
flyway                               perltidy                             zola
fn                                   petsc                                zrepl
folly                                petsc-complex                        zsh-history-substring-search
fork-cleaner                         pgrouting                            zydis
==> Renamed Formulae
jupyter -> jupyterlab                                   presto -> prestodb
==> Deleted Formulae
aiccu                 bdsup2sub             dcal                  gmt@4                 gmtl
==> minikube has been moved to Homebrew.
To uninstall the cask run:
  brew cask uninstall --force minikube
==> Installing minikube...
==> Installing dependencies for minikube: kubernetes-cli
==> Installing minikube dependency: kubernetes-cli
==> Downloading https://homebrew.bintray.com/bottles/kubernetes-cli-1.16.2.mojave.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/12/12b5954c175d44077679d95d96497038f800dc2b9b836f1068d8446f453
######################################################################## 100.0%
==> Pouring kubernetes-cli-1.16.2.mojave.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/kubectl
Target /usr/local/bin/kubectl
already exists. You may want to remove it:
  rm '/usr/local/bin/kubectl'

To force the link and overwrite all conflicting files:
  brew link --overwrite kubernetes-cli

To list all files that would be deleted:
  brew link --overwrite --dry-run kubernetes-cli

Possible conflicting files are:
/usr/local/bin/kubectl -> /Applications/Docker.app/Contents/Resources/bin/kubectl
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/kubernetes-cli/1.16.2: 232 files, 52.3MB
==> Installing minikube
==> Downloading https://homebrew.bintray.com/bottles/minikube-1.5.2.mojave.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/4c/4cf3836df30546744ecaf0514c22b041142e49f29e4c7ae74eff4e49b9d
######################################################################## 100.0%
==> Pouring minikube-1.5.2.mojave.bottle.tar.gz
==> minikube cask is installed, skipping link.
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/minikube/1.5.2: 8 files, 51.5MB
==> `brew cleanup` has not been run in 30 days, running now...
Removing: /Users/jlafata/Library/Caches/Homebrew/bosh-cli--6.0.0... (37.8MB)
Removing: /Users/jlafata/Library/Caches/Homebrew/cf-cli--6.46.0.tgz... (8.0MB)
Removing: /Users/jlafata/Library/Caches/Homebrew/go--1.12.9.mojave.bottle.tar.gz... (159.4MB)
Removing: /usr/local/Cellar/kubernetes-cli/1.16.1... (232 files, 52.3MB)
Removing: /Users/jlafata/Library/Caches/Homebrew/kubernetes-cli--1.16.1.mojave.bottle.tar.gz... (14.4MB)
Removing: /Users/jlafata/Library/Caches/Homebrew/tfenv--1.0.1.tar.gz... (11.9KB)
Removing: /Users/jlafata/Library/Caches/Homebrew/bbl--v8.2.14... (109MB)
Removing: /Users/jlafata/Library/Caches/Homebrew/terraform--0.12.8.mojave.bottle.tar.gz... (15.1MB)
Removing: /Users/jlafata/Library/Logs/Homebrew/terraform... (64B)
Removing: /Users/jlafata/Library/Logs/Homebrew/go... (64B)
Removing: /Users/jlafata/Library/Logs/Homebrew/tfswitch... (119B)
Removing: /Users/jlafata/Library/Logs/Homebrew/cf-cli... (119B)
Removing: /Users/jlafata/Library/Logs/Homebrew/bbl... (116B)
Removing: /Users/jlafata/Library/Logs/Homebrew/bosh-cli... (121B)
Removing: /Users/jlafata/Library/Logs/Homebrew/tfenv... (101B)
==> Caveats
==> kubernetes-cli
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> minikube
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
Linking /usr/local/Cellar/minikube/1.5.2... 3 symlinks created

==> Downloading https://homebrew.bintray.com/bottles/kubernetes-helm-2.15.2.mojave.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/af/af96fbedc19ad56994180843cda30829ce14c83b556531b8089b9c57835
######################################################################## 100.0%
==> Pouring kubernetes-helm-2.15.2.mojave.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/kubernetes-helm/2.15.2: 51 files, 85.1MB

`$ helm`
The Kubernetes package manager

To begin working with Helm, run the 'helm init' command:

```

`$ helm init`


This will install Tiller to your running Kubernetes cluster.
It will also set up any necessary local configuration.

Common actions from this point include:

- helm search:    Search for charts
- helm fetch:     Download a chart to your local directory to view
- helm install:   Upload the chart to Kubernetes
- helm list:      List releases of charts

Environment:

- $HELM_HOME:           Set an alternative location for Helm files. By default, these are stored in ~/.helm
- $HELM_HOST:           Set an alternative Tiller host. The format is host:port
- $HELM_NO_PLUGINS:     Disable plugins. Set HELM_NO_PLUGINS=1 to disable plugins.
- $TILLER_NAMESPACE:    Set an alternative Tiller namespace (default "kube-system")
- $KUBECONFIG:          Set an alternative Kubernetes configuration file (default "~/.kube/config")
- $HELM_TLS_CA_CERT:    Path to TLS CA certificate used to verify the Helm client and Tiller server certificates (default "$HELM_HOME/ca.pem")
- $HELM_TLS_CERT:       Path to TLS client certificate file for authenticating to Tiller (default "$HELM_HOME/cert.pem")
- $HELM_TLS_KEY:        Path to TLS client key file for authenticating to Tiller (default "$HELM_HOME/key.pem")
- $HELM_TLS_ENABLE:     Enable TLS connection between Helm and Tiller (default "false")
- $HELM_TLS_VERIFY:     Enable TLS connection between Helm and Tiller and verify Tiller server certificate (default "false")
- $HELM_TLS_HOSTNAME:   The hostname or IP address used to verify the Tiller server certificate (default "127.0.0.1")
- $HELM_KEY_PASSPHRASE: Set HELM_KEY_PASSPHRASE to the passphrase of your PGP private key. If set, you will not be prompted for the passphrase while signing helm charts

Usage:
  helm [command]

Available Commands:
  completion  Generate autocompletions script for the specified shell (bash or zsh)
  create      Create a new chart with the given name
  delete      Given a release name, delete the release from Kubernetes
  dependency  Manage a chart's dependencies
  fetch       Download a chart from a repository and (optionally) unpack it in local directory
  get         Download a named release
  help        Help about any command
  history     Fetch release history
  home        Displays the location of HELM_HOME
  init        Initialize Helm on both client and server
  inspect     Inspect a chart
  install     Install a chart archive
  lint        Examines a chart for possible issues
  list        List releases
  package     Package a chart directory into a chart archive
  plugin      Add, list, or remove Helm plugins
  repo        Add, list, remove, update, and index chart repositories
  reset       Uninstalls Tiller from a cluster
  rollback    Rollback a release to a previous revision
  search      Search for a keyword in charts
  serve       Start a local http web server
  status      Displays the status of the named release
  template    Locally render templates
  test        Test a release
  upgrade     Upgrade a release
  verify      Verify that a chart at the given path has been signed and is valid
  version     Print the client/server version information

Flags:
      --debug                           Enable verbose output
  -h, --help                            help for helm
      --home string                     Location of your Helm config. Overrides $HELM_HOME (default "/Users/jlafata/.helm")
      --host string                     Address of Tiller. Overrides $HELM_HOST
      --kube-context string             Name of the kubeconfig context to use
      --kubeconfig string               Absolute path of the kubeconfig file to be used
      --tiller-connection-timeout int   The duration (in seconds) Helm will wait to establish a connection to Tiller (default 300)
      --tiller-namespace string         Namespace of Tiller (default "kube-system")

Use "helm [command] --help" for more information about a command.

```
  $ helm init  
```
```
Creating /Users/jlafata/.helm
Creating /Users/jlafata/.helm/repository
Creating /Users/jlafata/.helm/repository/cache
Creating /Users/jlafata/.helm/repository/local
Creating /Users/jlafata/.helm/plugins
Creating /Users/jlafata/.helm/starters
Creating /Users/jlafata/.helm/cache/archive
Creating /Users/jlafata/.helm/repository/repositories.yaml
Adding stable repo with URL: https://kubernetes-charts.storage.googleapis.com
Adding local repo with URL: http://127.0.0.1:8879/charts
$HELM_HOME has been configured at /Users/jlafata/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
```

```
jlafata$ helm repo add bitnami https://charts.bitnami.com/bitnami
```

```
"bitnami" has been added to your repositories
```

```
$ helm install bitnami/kafka
NAME:   youngling-snake
LAST DEPLOYED: Fri Nov 22 13:36:40 2019
NAMESPACE: default
STATUS: DEPLOYED

RESOURCES:
==> v1/Pod(related)
NAME                         READY  STATUS   RESTARTS  AGE
youngling-snake-kafka-0      0/1    Pending  0         1s
youngling-snake-zookeeper-0  0/1    Pending  0         1s

==> v1/Service
NAME                                TYPE       CLUSTER-IP      EXTERNAL-IP  PORT(S)                     AGE
youngling-snake-kafka               ClusterIP  10.105.114.247  <none>       9092/TCP                    1s
youngling-snake-kafka-headless      ClusterIP  None            <none>       9092/TCP                    1s
youngling-snake-zookeeper           ClusterIP  10.104.54.31    <none>       2181/TCP,2888/TCP,3888/TCP  1s
youngling-snake-zookeeper-headless  ClusterIP  None            <none>       2181/TCP,2888/TCP,3888/TCP  1s

==> v1/StatefulSet
NAME                       READY  AGE
youngling-snake-kafka      0/1    1s
youngling-snake-zookeeper  0/1    1s


NOTES:


** Please be patient while the chart is being deployed **

Kafka can be accessed via port 9092 on the following DNS name from within your cluster:

    youngling-snake-kafka.default.svc.cluster.local

To create a topic run the following command:

    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=youngling-snake,app.kubernetes.io/component=kafka" -o jsonpath="{.items[0].metadata.name}")
    kubectl --namespace default exec -it $POD_NAME -- kafka-topics.sh --create --zookeeper youngling-snake-zookeeper:2181 --replication-factor 1 --partitions 1 --topic test

To list all the topics run the following command:

    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=youngling-snake,app.kubernetes.io/component=kafka" -o jsonpath="{.items[0].metadata.name}")
    kubectl --namespace default exec -it $POD_NAME -- kafka-topics.sh --list --zookeeper youngling-snake-zookeeper:2181

To start a kafka producer run the following command:

    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=youngling-snake,app.kubernetes.io/component=kafka" -o jsonpath="{.items[0].metadata.name}")
    kubectl --namespace default exec -it $POD_NAME -- kafka-console-producer.sh --broker-list localhost:9092 --topic test

To start a kafka consumer run the following command:

    export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=kafka,app.kubernetes.io/instance=youngling-snake,app.kubernetes.io/component=kafka" -o jsonpath="{.items[0].metadata.name}")
    kubectl --namespace default exec -it $POD_NAME -- kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

To connect to your Kafka server from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/youngling-snake-kafka 9092:9092 &
    echo "Kafka Broker Endpoint: 127.0.0.1:9092"

    PRODUCER:
        kafka-console-producer.sh --broker-list 127.0.0.1:9092 --topic test
    CONSUMER:
        kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic test --from-beginning

```

# list and remove helm releases
```
$ helm list -aq
youngling-snake
$ helm delete youngling-snake
release "youngling-snake" deleted

```

```
$ kubectl get pods
        NAME                       READY   STATUS    RESTARTS   AGE
        errant-prawn-kafka-0       1/1     Running   1          4m20s
        errant-prawn-zookeeper-0   1/1     Running   0          4m20s

```
#get nodes
$ kubectl get nodes -o wide
NAME       STATUS   ROLES    AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE              KERNEL-VERSION   CONTAINER-RUNTIME
minikube   Ready    master   23h   v1.16.2   192.168.64.2   <none>        Buildroot 2019.02.6   4.19.76  

#ssh to minukubes
ssh docker@192.168.64.2
password: tcuser

#deploy cp-zookeeper

```
kubectl create configmap cp-zookeeper-config --from-env-file=configmap/cp-zookeeper-config.properties --dry-run -o yaml > cp-zookeeper-config.yaml

kubectl create -f cp-zookeeper-config.yaml

kubectl create -f cp-zookeeper.yaml

```

#deploy cp-kafka
```
kubectl create configmap cp-kafka-config --from-env-file=configmap/cp-kafka-config.properties --dry-run -o yaml > cp-kafka-config.yaml

kubectl create -f cp-kafka-config.yaml

kubectl create -f cp-kafka.yaml
```


#deployment confluence docker images to k8s
```
$ kubectl create deployment cp-schema-registry --image confluentinc/cp-schema-registry  --dry-run -o yaml > cp-schema-registry.yaml
```
# to verify
kubectl get pods
kubectl logs <pod-name>


#verification resulting in identifying that the following environment variables are needed.

#create config map
```
kubectl create configmap cp-schema-registry-config --from-env-file=configmap/cp-schema-registry-config.properties --dry-run -o yaml > cp-schema-registry-config.yaml

$ kubectl create -f cp-schema-registry-config.yaml
```
#verify config masp
```
kubectl get configmap cp-schema-registry-config -o yaml
```

```
$ kubectl create deployment cp-kafka-connect --image confluentinc/cp-kafka-connect  --dry-run -o yaml > cp-kafka-connect.yaml
```

#create config map
```
kubectl create configmap cp-kafka-connect-config --from-env-file=configmap/cp-kafka-connect-config.properties --dry-run -o yaml > cp-kafka-connect-config.yaml

# modify deployment yaml to refer to config map
```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: cp-schema-registry
  name: cp-schema-registry
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cp-schema-registry
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: cp-schema-registry
    spec:
      containers:
      - image: confluentinc/cp-schema-registry
        name: cp-schema-registry
        envFrom:
        - configMapRef:
            name: cp-schema-registry-config        
        resources: {}
status: {}
```
# redeploy
$ kubectl delete -f cp-schema-registry.yaml
$ kubectl create -f cp-schema-registry.yaml

#kafka connect deployment
$ kubectl create -f cp-kafka-connect-config.yaml
```
#verify config masp
```
kubectl get configmap cp-kafka-connect-config -o yaml
```



#edit cp-kafka-connect.yaml and add CONNECT_BOOTSTRAP_SERVERS to environment

#original deployment file
```apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: cp-kafka-connect
  name: cp-kafka-connect
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cp-kafka-connect
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: cp-kafka-connect
    spec:
      containers:
      - image: confluentinc/cp-kafka-connect
        name: cp-kafka-connect
        envFrom:
        - configMapRef:
            name: cp-kafka-connect-config        
        resources: {}
status: {}
```

#after adding environment variable
```
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: cp-kafka-connect
  name: cp-kafka-connect
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cp-kafka-connect
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: cp-kafka-connect
    spec:
      containers:
      - image: confluentinc/cp-kafka-connect
        name: cp-kafka-connect
        resources: {}
status: {}
```
