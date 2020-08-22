# Kubernetes Failure Stories

A compiled list of links to public failure stories related to Kubernetes.
Most recent publications on top.

* [The case of the missing packet: An EKS migration tale - MindTickle - blog post 2020](https://yashmehrotra.com/post/2020-03-16-case-of-missing-packet/)
    * involved: EKS, AWS CNI Plugin,
    * impact: Frequent connection failures when talking to services outside the cluster
* [Kubernetes Networking Problems Due to the Conntrack - loveholidays - blog post 2020](https://deploy.live/blog/kubernetes-networking-problems-due-to-the-conntrack/)
    * involved: GKE, conntrack, HAProxy
    * impact: high error rate on network-heavy services
* [DNS issues in Kubernetes. Public postmortem #1 - Preply - blog post 2020](https://medium.com/preply-engineering/dns-postmortem-e169efd45afd)
    * involved: conntrack, DNS, CoreDNS-autoscaler
    * impact: partial production outage
* [CPU limits and aggressive throttling in Kubernetes - Omio - blog post 2020](https://medium.com/omio-engineering/cpu-limits-and-aggressive-throttling-in-kubernetes-c5b20bd8a718)
    * involved: GKE, CPU Limit, CPU throttling
    * impact: high latency, errors
* [When GKE ran out of IP addresses - loveholidays - blog post 2020](https://deploy.live/blog/when-gke-ran-out-of-ip-addresses/)
    * involved: GKE, cluster autoscaler, HPA, Alias IP VPC (VPC Native)
    * impact: stuck deployment, blocked autoscaling of both pods and nodes
* [How we failed to integrate Istio into our platform - Exponea - blog post 2019](https://medium.com/@jakubkulich/sailing-with-the-istio-through-the-shallow-water-8ae81668381e)
    * involved: Istio, GKE, proxy injection
    * impact: stopped Istio rollout, developers' time spent
* [Kubernetes made my latency 10x higher - Adevinta - blog post 2019](https://srvaroa.github.io/kubernetes/migration/latency/dns/java/aws/microservices/2019/10/22/kubernetes-added-a-0-to-my-latency.html)
    * involved: KIAM, DNS, AWS IAM, latency
    * impact: service showing up to x10 higher latencies compared to a deployment in EC2
* [A Kubernetes failure story (dex) - anonymous Fullstaq client - Dutch kubernetes meetup slides 2019-06](https://pieterlange.github.io/failure-stories/2019-06.dex.html)
    * involved: etcd, apiserver, dex, custom resources
    * impact: broken control plane on production with no access to o11y due to broken authentication system, no actual business impact
* [A Kubernetes crime story - Prezi - blog post 2019](https://engineering.prezi.com/https-engineering-prezi-com-a-kubernetes-crime-story-2e8d75a77630)
    * involved: AWS EKS, SNAT, conntrack, Amazon VPC CNI plugin
    * impact: delay of 1-3 seconds for outgoing TCP connections
* [Postmortem: New K8s workers unable to join cluster - FREE NOW - postmortem 2019](https://github.com/freenowtech/postmortems/blob/master/2019-09-19%20-%20New%20K8s%20workers%20unable%20to%20join%20cluster.pdf)
    * involved: AWS spot instances, kops, CentOS, container-selinux
    * impact: insufficient cluster capacity in testing environments, failed deployments in production and staging environments
* [How a simple admission webhook lead to a cluster outage - Jetstack - blog post 2019](https://blog.jetstack.io/blog/gke-webhook-outage)
    * involved: ValidatingWebhookConfiguration, GKE node auto-repair
    * impact: prolonged downtime of non-prod environment, nodes lost, failed master upgrade
* [Post Mortem: Kubernetes Node OOM - Blue Matador - blog post 2019](https://www.bluematador.com/blog/post-mortem-kubernetes-node-oom)
    * involved: AWS, SystemOOM, EBS, fluentd-sumologic, no resource requests/limits
    * impact: unknown, Pods killed
* [Kubernetes’ dirty endpoint secret and Ingress - Ravelin - blog post 2019](https://philpearl.github.io/post/k8s_ingress/)
    * involved: GKE, Ingress, replication controller, SIGTERM, "graceful shutdown"
    * impact: occasional 502 errors
* [How a Production Outage Was Caused Using Kubernetes Pod Priorities - Grafana Labs 2019](https://grafana.com/blog/2019/07/24/how-a-production-outage-was-caused-using-kubernetes-pod-priorities/)
    * involved: Pod priorities
    * impact: cascading Pod evictions
* [Moving to Kubernetes: the Bad and the Ugly - Xing - ContainerDays EU 2019](https://www.youtube.com/watch?v=MoIdU0J0f0E)
    * involved: nginx Ingress, network interrupts, conntrack, frozen CronJob, PLEG, stuck controllers
    * impact: lost requests, response time jumps, not ready nodes
* [Kubernetes Failure Stories, or: How to Crash Your Cluster - Zalando - ContainerDays EU 2019](https://www.youtube.com/watch?v=LpFApeaGv7A)
    * involved: AWS IAM, Kubelet, `--kube-api-qps`, Skipper-Ingress, AWS, `OOMKill`, CronJob, CoreDNS, CPU throttling
    * impact: build errors, production outages
* [Build Errors of Continuous Delivery Platform - Zalando - postmortem 2019](https://github.com/zalando-incubator/kubernetes-on-aws/blob/dev/docs/postmortems/jun-2019-kubelet-qps.md)
    * involved: AWS IAM, Kubelet, kube2iam, `--kube-api-qps`
    * impact: build errors
* [10 Ways to Shoot Yourself in the Foot with Kubernetes, #9 Will Surprise You - Datadog - KubeCon Barcelona 2019](https://www.youtube.com/watch?v=QKI-JRs2RIE)
    * involved: CoreDNS, `ndots:5`, IPVS conntrack, `imagePullPolicy: Always`, DaemonSet, NAT instances, `latest` tag, API server `OOMKill`, kube2iam, cluster-autoscaler, PodPriority, audit logs, `spec.replicas`, AWS ASG rebalance, CronJob, Pod toleration, zombies, `readinessProbe.exec`, cgroup freeze, kubectl
    * impact: unknown, API server outage, pending pods, slow deployments
* [How Spotify Accidentally Deleted All its Kube Clusters with No User Impact - Spotify - KubeCon Barcelona 2019](https://www.youtube.com/watch?v=ix0Tw8uinWs)
    * involved: GKE, cluster deletion, browser tabs, Terraform, global state file, git PRs, GCP permissions
    * impact: no impact on end users
* [Kubernetes Failure Stories - Zalando - KubeCon Barcelona 2019](https://www.youtube.com/watch?v=6sDTB4eV4F8)
    * involved: Skipper-Ingress, AWS, `OOMKill`, high latency, CronJob, CoreDNS, `ndots:5`, etcd, CPU throttling
    * impact: multiple production outages
* [Oh Sh\*t! The Config Changed! - Pusher - KubeCon Barcelona 2019](https://www.youtube.com/watch?v=8P7-C44Gjj8)
    * involved: AWS, nginx, ConfigMap change
    * impact: production outage
* [Misunderstanding the behaviour of one templating line - Skyscanner - blog post 2019](https://medium.com/@SkyscannerEng/misunderstanding-the-behaviour-of-one-templating-line-and-the-pain-it-caused-our-k8s-clusters-a420f30a99f1)
    * involved: HAProxy-Ingress, Service VIPs, Golang templating
    * impact: Significantly increased latency, 5XXs thrown from some services
* [How to kill the Algolia dashboard during Black Friday or How not to use Kubernetes - Algolia - Algolia Search Party 2019](https://www.youtube.com/watch?v=Fjyg7cxRZQs&list=PLuHdbqhRgWHJg9eOFCl5dgLvVjd_DFz8O&index=3&t=0s)
    * involved: GKE, Jobs, overload
    * impact: high latency, timeouts
* [All pods scheduled to same failing host - Moonlight - postmortem 2019](https://updates.moonlightwork.com/outage-post-mortem-87370)
    * involved: Google Kubernetes Engine, scheduler, anti-affinity rules
    * impact: major production outage, 100% traffic loss
* [The shipwreck of GKE Cluster Upgrade - loveholidays - blog post 2019](https://deploy.live/blog/the-shipwreck-of-gke-cluster-upgrade/)
    * involved: GCP Ingress, GKE Cluster, nodes
    * impact: critical drop in pod availability, loss of ingress, 2 hour maintenance lasting 7 hours
* [Breaking Kubernetes: How We Broke and Fixed our K8s Cluster - Civis Analytics - blog post 2019](https://medium.com/civis-analytics/https-medium-com-civis-analytics-breaking-kubernetes-how-we-broke-and-fixed-our-k8s-cluster-adfa6fbade61)
    * involved: AWS, kops, large clusters, batch jobs infrastructure, Datadog, API server, DNS, CPU throttling
    * impact: production outage
* [Let's talk about Failures with Kubernetes - Zalando - Hamburg meetup 2019](https://www.slideshare.net/try_except_/lets-talk-about-failures-with-kubernetes-hamburg-meetup)
    * involved: AWS, `NotReady` nodes, ELB dynamic IPs, Ingress, API server, CronJob, CoreDNS, `OOMKill`, kubelet memory leak, CPU throttling
    * impact: production outages
* [Total DNS outage in Kubernetes cluster - Zalando - postmortem 2019](https://github.com/zalando-incubator/kubernetes-on-aws/blob/dev/docs/postmortems/jan-2019-dns-outage.md)
    * involved: AWS, DNS, CoreDNS, `OOMKill`, `ndots:5`, HTTP retries
    * impact: production outage
* [Maximize learnings from a Kubernetes cluster failure - NU.nl - blog post 2019](https://www.tibobeijen.nl/2019/02/01/learning-from-kubernetes-cluster-failure/)
    * involved: AWS, `NotReady` nodes, `SystemOOM`, Helm, ElastAlert, no resource limits set
    * impact: user experience affected for internally used tools and dashboards
* [Kubernetes Load Balancer Configuration - Beware when draining nodes - DevOps Hof - blog post 2019](https://www.devops-hof.de/kubernetes-load-balancer-konfiguration-beware-when-draining-nodes/)
    * involved: GCP Load Balancer, `externalTrafficPolicy`, ingress-nginx
    * impact: total ingress traffic outage
* [On Infrastructure at Scale: A Cascading Failure of Distributed Systems - Target - Medium post January 2019](https://medium.com/@daniel.p.woods/on-infrastructure-at-scale-a-cascading-failure-of-distributed-systems-7cff2a3cd2df)
    * involved: on-premise, Kafka, large cluster, Consul, Docker daemon, high CPU usage
    * impact: development environment outage
* [How NOT to do Kubernetes - Sr.SRE Medya Ghazizadeh - Google - Cloud Native Meetup Sep 2018](https://www.youtube.com/watch?v=V0DVkrHf08k)
    * involved: public container registery, ingress wild card, image size, replica count, 12factor
    * impact: security, stablity of clusters.
* [Running Kubernetes in Production: A Million Ways to Crash Your Cluster - Zalando - DevOpsCon Munich 2018](https://www.slideshare.net/try_except_/running-kubernetes-in-production-a-million-ways-to-crash-your-cluster-devopscon-munich-2018)
    * involved: AWS, Ingress, CronJob, etcd, flannel, Docker, CPU throttling
    * impact: production outages
* [Outages? Downtime? - Veracode - blog post 2018](https://sethmccombs.github.io/work/2018/12/03/Outages.html)
    * involved: AWS, AWS IAM, region migration, kubespray, Terraform, pod CIDR
    * impact: QA/dev cluster outage
* [NRE Labs Outage Post-Mortem - NRE Labs - blog post 2018](https://keepingitclassless.net/2018/12/december-4-nre-labs-outage-post-mortem/)
    * involved: GCP, kubeadm, etcd, Terraform, `livenessProbe`
    * impact: production outage
* [A Perfect DNS Storm - Toyota Connected - blog post 2018](https://www.adammargherio.com/a-perfect-dns-storm/)
    * involved: Azure, DNS, `ndots:5`, Alpine musl libc
    * impact: DNS resolution failures
* [Kubernetes and the Menace ELB, the tale of an outage - Turnitin - blog post 2018](https://itnext.io/kubernetes-and-the-menace-elb-the-tale-of-an-outage-c00bef678fc0)
    * involved: AWS, kube-aws, ELB dynamic IPs, API server, kubelet, `NotReady` nodes
    * impact: 15 minutes cluster outage
* [Moving the Entire Stack to K8s Within a Year – Lessons Learned - ThredUP - DevOpsStage 2018](https://www.youtube.com/watch?v=tA8Sr3Nsx1I)
    * involved: AWS, kops, HAProxy, `livenessProbe`, DNS, too many open files
    * impact: unknown outages, DNS errors
* [AirMap Platform Service Outage - AirMap - incident report 2018](https://www.airmap.com/incident-180719/)
    * involved: Azure, `NotReady` nodes, kubelet PLEG, CNI
    * impact: production AirMap platform outage
* [Anatomy of a Production Kubernetes Outage - Monzo - KubeCon Europe 2018](https://www.youtube.com/watch?v=OUYTNywPk-s)
    * involved: AWS, etcd, Linkerd, `NullPointerException`, gRPC client, services without endpoints, incompatible Kubernetes API change
    * impact: production ledger/platform outage
* [Stories from the Playbook - Google - KubeCon Europe 2018](https://youtu.be/N2JUGnwinbQ)
    * involved: GKE, etcd, Docker daemon, Image registry, dnsmasq vulnerabilities
    * impact: production outage
* [101 Ways to "Break and Recover" Kubernetes Cluster - Oath/Yahoo - KubeCon Europe 2018](https://www.youtube.com/watch?v=likHm-KHGWQ)
    * involved: on-premise, namespace deletion, domain name collision, `NotReady` nodes, etcd empty dir, TLS certificate refresh, DNS issues, OOM
    * impact: unknown cluster outages
* [Experiences with running PostgreSQL on Kubernetes - Gravitational - blog post 2018](https://gravitational.com/blog/running-postgresql-on-kubernetes/)
    * involved: PostgreSQL, streaming replication
    * impact: data loss
* [101 Ways to Crash Your Cluster - Nordstrom - KubeCon North America 2017](https://www.youtube.com/watch?v=xZO9nx6GBu0)
    * involved: AWS, `NotReady` nodes, OOM, eviction thresholds, ELB dynamic IPs, kubelet, cluster autoscaler, etcd split
    * impact: full production cluster outage, other outages
* [Major Outage: Current account payments may fail - Monzo - Monzo Community post 2017](https://community.monzo.com/t/resolved-current-account-payments-may-fail-major-outage-27-10-2017/26296/95)
    * involved: AWS, etcd, Linkerd, `NullPointerException`, services without endpoints
    * impact: major production outage, full platform outage, current account payments fail
* [Fallacies of Distributed Computing with Kubernetes on AWS - Zalando - AWS User Group Hamburg October 2017](https://www.slideshare.net/RaffaeleDiFazio/fallacies-of-distributed-computing-with-kubernetes-on-aws)
    * involved: AWS, unhealthy nodes, Ingress, CronJob
    * impact: production outage
* [Search and Reporting Outage - Universe - incident report 2017](http://status.universe.com/incidents/115n3vxqwzcf)
    * involved: Job, `RestartPolicy`, consume node resources
    * impact: production Universe search and reporting outage
* [Our First Kubernetes Outage - Saltside - blog post 2017](https://engineering.saltside.se/our-first-kubernetes-outage-c6b9249cfd3a)
    * involved: AWS, kops, Helm, `NotReady` nodes, resource exhaustion
    * impact: nonproduction cluster outage
* [Our Failure Migrating to Kubernetes - Saltside - blog post 2017](https://engineering.saltside.se/our-failure-migrating-to-kubernetes-25c28e6dd604)
    * involved: AWS, kops, ELB, `BackendConnectionErrors`, `LoadBalancer` service
    * impact: aborted application migration
* [SaleMove US System Issue - SaleMove - incident report 2017](https://status.salemove.com/incidents/xf6cr710yrzn)
    * involved: AWS, ELB dynamic IPs, DNS `A` record for master, API server
    * impact: production issues with SaleMove US System

# Why

Kubernetes is a fairly complex system with many moving parts.
Its ecosystem is constantly evolving and adding even more layers (service mesh, ...) to the mix.
Considering this environment, we don't hear enough real-world horror stories to learn from each other!
This compilation of failure stories should make it easier for people dealing with Kubernetes operations (SRE, Ops, platform/infrastructure teams) to
learn from others and reduce the unknown unknowns of running Kubernetes in production.
For more information, [see the blog post](https://srcco.de/posts/kubernetes-failure-stories.html).

# Contributing

Please help the community and **[share a link to your failure story by opening a Pull Request!](https://github.com/hjacobs/kubernetes-failure-stories/edit/master/README.md)**
Failure stories can be anything like blog posts, conference/meetup talks, incident postmortems, tweetstorms, ...

I would also be glad to hear about your failure stories on Twitter: my handle is [@try_except_](https://twitter.com/try_except_)

# Thanks

Thanks to all contributors and everybody who writes public Kubernetes postmortems! 👏

Thanks to [Joe Beda](https://twitter.com/jbeda) for contributing his domain k8s.af for this project! 👏
