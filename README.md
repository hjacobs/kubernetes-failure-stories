# Kubernetes Failure Stories

A compiled list of links to public failure stories related to Kubernetes.
Most recent publications on top.

* [Kubernetes Load Balancer Konfiguration – Vorsicht beim Drainen von Nodes (German) - DevOps Hof - blog post 2019](https://www.devops-hof.de/kubernetes-load-balancer-konfiguration-vorsicht-beim-drainen-von-nodes/)
* [On Infrastructure at Scale: A Cascading Failure of Distributed Systems - Target - Medium post January 2019](https://medium.com/@daniel.p.woods/on-infrastructure-at-scale-a-cascading-failure-of-distributed-systems-7cff2a3cd2df)
* [Running Kubernetes in Production: A Million Ways to Crash Your Cluster - Zalando - DevOpsCon Munich 2018](https://www.slideshare.net/try_except_/running-kubernetes-in-production-a-million-ways-to-crash-your-cluster-devopscon-munich-2018)
* [Outages? Downtime? - Veracode - blog post 2018](https://sethmccombs.github.io/work/2018/12/03/Outages.html)
* [NRE Labs Outage Post-Mortem - NRE Labs - blog post 2018](https://keepingitclassless.net/2018/12/december-4---nre-labs-outage-post-mortem/)
* [A Perfect DNS Storm - Toyota Connected - blog post 2018](https://www.adammargherio.com/a-perfect-dns-storm/)
* [Kubernetes and the Menace ELB, the tale of an outage - Turnitin - blog post 2018](https://itnext.io/kubernetes-and-the-menace-elb-the-tale-of-an-outage-c00bef678fc0)
* [Moving the Entire Stack to K8s Within a Year – Lessons Learned - ThredUP - DevOpsStage 2018](https://www.youtube.com/watch?v=tA8Sr3Nsx1I)
* [AirMap Platform Service Outage - AirMap - incident report 2018](https://www.airmap.com/incident-180719/)
* [Anatomy of a Production Kubernetes Outage - Monzo - KubeCon Europe 2018](https://www.youtube.com/watch?v=OUYTNywPk-s)
* [101 Ways to "Break and Recover" Kubernetes Cluster - Oath/Yahoo - KubeCon Europe 2018](https://www.youtube.com/watch?v=likHm-KHGWQ)
* [101 Ways to Crash Your Cluster - Nordstrom - KubeCon North America 2017](https://www.youtube.com/watch?v=xZO9nx6GBu0)
* [Major Outage: Current account payments may fail - Monzo - Monzo Community post 2017](https://community.monzo.com/t/resolved-current-account-payments-may-fail-major-outage-27-10-2017/26296/95)
* [Search and Reporting Outage - Universe - incident report 2017](http://status.universe.com/incidents/115n3vxqwzcf)
* [Our First Kubernetes Outage - Saltside - blog post 2017](https://engineering.saltside.se/our-first-kubernetes-outage-c6b9249cfd3a)
* [Our Failure Migrating to Kubernetes - Saltside - blog post 2017](https://engineering.saltside.se/our-failure-migrating-to-kubernetes-25c28e6dd604)
* [SaleMove US System Issue - SaleMove - incident report 2017](https://status.salemove.com/incidents/xf6cr710yrzn)

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
