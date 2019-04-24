# Kubernetes Failure Stories

A compiled list of links to public failure stories related to Kubernetes.
Most recent publications on top.

* [Misunderstanding the behaviour of one templating line - Skyscanner - blog post 2019](https://medium.com/@SkyscannerEng/misunderstanding-the-behaviour-of-one-templating-line-and-the-pain-it-caused-our-k8s-clusters-a420f30a99f1)
    * involved: HAProxy-Ingress, Service VIPs, Golang templating
    * impact: Significantly increased latency, 5XXs thrown from some services
* [All pods scheduled to same failing host - Moonlight - postmortem 2019](https://updates.moonlightwork.com/outage-post-mortem-87370)
    * involved: Google Kubernetes Engine, scheduler, anti-affinity rules
    * impact: major production outage, 100% traffic loss
* [The shipwreck of GKE Cluster Upgrade - Loveholidays GKE - blog post 2019](https://deploy.live/blog/the-shipwreck-of-gke-cluster-upgrade/)
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
* [NRE Labs Outage Post-Mortem - NRE Labs - blog post 2018](https://keepingitclassless.net/2018/12/december-4---nre-labs-outage-post-mortem/)
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

Please help the community and **share a link to your failure story by opening a Pull Request!**
Failure stories can be anything like blog posts, conference/meetup talks, incident postmortems, tweetstorms, ...

I would also be glad to hear about your failure stories on Twitter: my handle is [@try_except_](https://twitter.com/try_except_)
