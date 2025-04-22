# Lucas Thiesen

## Summary
---

- I’m proficient in Go, JavaScript/Node.js and Python, but also have experience using C and C++.
- I have experience with computer networks, distributed systems, GRPC, Rest APIs and GraphQL APIs.
- I’ve used several SQL and NOSQL databases, but most of my experience is with PostgreSQL and Redis.
- I have great experience developing and maintaining custom resources for Kubernetes and core infrastructure components.
- I’m used to work with agile methodologies like Scrum, Kanban and XP.
- I have experience leading and mentoring people and great communication skills.

## Engineering Experience
---

[Delivery hero](https://www.deliveryhero.com/) <br>
---
Food and groceries delivery platform present in 70+ countries. <br><br>
**Senior Software Engineer** _(May 2024 - Present)_ <br>
  - Implemented a A/B testing framework and A/B testing tracking.
  - Implemented a model monitoring solution so the team could measure ML model accuracy.
  - Implemented versioning of machine learning model variables to enable the team to run multiple model versions in parallel.
  - Migrated the infrastructure of several AdTech components to support new kubernetes version and the new Global development platform implemented in house.
  - Improved the latency of AdRanker's relevance component in 50% by tuning requests and limits parameters to avoid CPU throttling.
  - Developed a service responsible to host several different rankers to the different vendor categories taking into account, product popularity, user preferences and promotions.
  - Wrote an RFC Defining a department wide pagination strategy that deals with the blending of several rankers each with its own pagination structure.
  - Designed of a feature cache where we pre-proccess and store information so that machine learning models can consume it with very low latency to rank products for the product catalog.
  - **_Technologies used:_** Go · Redis · Open Telemetry · GRPC · Grafana · Kubernetes · Terraform · Google Cloud Platform (GCP)
<br><br>

[Zalando](https://zalando.de/) <br>
---
Online retail platform that sells fashion and beauty products. <br><br>
**Software Engineer** _(Dec 2022 - Apr 2024)_ <br>
There are a few core platform teams in Zalando that develop the underlying infrastructure for all Zalando products. I work in one of this teams, Gateway and Proxy. The gateway and proxy team owns all the edge logic in Zalando, from edge protection to routing and networking at Kubernetes level for all 200+ kubernetes clusters. My contributions within the team are: <br>

- Maintained an open source reverse proxy called skipper developed in Zalando and written in Go.
- Refactored and improved e2e tests of kubernetes ingress controller for clusters hosted in AWS developed in zalando and written in Go.
- Implemented external hostname based metrics collector to a kubernetes metric adapter, also developed within Zalando and written in Go, this component is responsible to provide metrics to horizontal pod autoscaler in kubernetes, enabling teams to autoscale based on more inteligent and complex metrics.
- Supported teams rolling out Fabric gateway, which is an API gateway built on top of skipper. This API gateway provide to development teams the ability to easily configure all routing, AuthN/AuthX, rate limiting and traffic shaping based on OpenAPI yamls and simple configuration of a Kubernetes CRD. Fabric Gateway was developed in Zalando and written in Go. <br>
- **_Technologies used:_** Go · Kubernetes · AWS <br>

**Site Reliability Engineer** _(Dec 2021 - Dec 2022)_ <br>
  - Improved rate limiting and bot traffic protection by:
    * Designing a strategy to improve rate limits in cart and checkout flows.
    * Developing several scripts to fetch data and make statistical analysis of rate limits.
    * Writing documentation and educational material to enable other engineers to make the same analysis and changes.
    * Training of other Engineers to use the tools I created to improve rate limits.
    * Design, review and vetting of a new rate limiting middleware using leaky bucket algorithm. <br>
    * This initiatives reduced incomming bot traffic by more than 50% helping Zalando save many thousands of Euros worth of unecessary infrastructure and outages due to overload in cart and checkout flows.
  - Moderated and participated Post incident analysis (Post mortens). This usualy involves many teams creating an oportunity of a lot of cross team work which improves the platform as a whole but also might improve playbooks and processes.
  - Developed a risk register internal tool to track possible and recurrent issues within the whole application ecosystem. This risk register enabled Engineering teams to report risks to high level management (heads and directors) creating cross team colaboration on reliability issues which reduces toil, share knowledge across teams and improves the department ability to act on post mortem action items.
  - Improved tracing and adaptive paging solution usage on web experience and checkout services. Reducing the number of false positives for incidents in the department by 13%.
  - Participated as 24x7 on call responder rotation with the web experience team within the checkout department. <br>
  - **_Technologies used:_** Go · Open Telemetry · Shell script · Python · Kubernetes
<br><br>

[Quinto Andar](https://www.quintoandar.com.br/) <br>
---
Online real estate platform where users are able to rent or buy completely online, the contract is also signed online and the company provide safety means and compensation in case of schemes. <br><br>
**Site Reliability Engineer** _(May 2021 - Oct 2021)_ <br>
  - Developed of a distributed and decoupled solution for authorization and authentication to all back office applications of the company, using Open Policy Agent (OPA), Kubernetes instrumentation, and Kong proxy;
  - Developed of different fluent bit log pipelines to keep access logs of all APIs of the company, also the development of a system to keep a record of old logs for the data access auditing process;
  - Maintained of a service mesh inside QuintoAndar’s six clusters using Istio 1.4;
  - Supported software engineering teams on DevOps practices and design decisions. <br>
  - **_Technologies used:_** Shell Scripting · Go · AWS · Terraform · Kubernetes
<br><br>

[3778](https://www.3778.care/) <br>
---
Healthtech specialized in corporate health care. It offers many services for companies looking for health care solutions for their employees and also dedicated solutions for hospitals. <br><br>
**Platform Engineer** _(Apr 2020 - May 2021)_ <br>
  - Developed an egress system for the whole company. This system enabled all ETL and automated scans of 3778 customers' databases to pass through a single output, making it easier to configure ingress on customers' networks;
  - Developed an SSO system for the whole company using OAuth2-Proxy, Envoy filters, and Istio configurations;
  - Configured and maintained a service mesh inside 3778 clusters using Istio 1.6;
  - Supported and maintained an infrastructure with three Kubernetes clusters;
  - Developed Terraform modules to automate 3778 infrastructure in GCP and AWS;
  - Supported development teams on system design and architecture; <br>
  - **_Technologies used:_** Shell Scripting · Istio · Envoy · SSO · Go · Google Cloud Platform (GCP) · Terraform · Kubernetes <br>

**Software Engineer** _(Sep 2019 - Apr 2020)_ <br>
  - Developed a system to help physicians, hospitals, and patients to enable preventive healthcare. It was a microservice-oriented architecture written in Go and a lightweight UI based on web components. <br>
  - **_Technologies used:_** Go · JavaScript · PostgreSQL
<br><br>

[CERTI](https://certi.org.br/en/index) <br>
---
Software outsourcing company based in Brazil with focus on inovation projects. <br><br>

**Software Engineer** _(Aug 2016 - Jun 2019)_ <br>
  - Developed a back office application to help after-sales and support professionals provide a better user experience and get insights from client usage and needs. This product was developed using React and Django; to gather the needed information this application had to interact with many other services;
  - Developed a test tool to accelerate the verification phase of DO-178B (development standard used to build and certify avionic systems and applications); it was used to ingest terabytes of data and produce reports on electronic tests. This tool made some of these tests take seconds instead of days.
  - Was responsible for the formal verification and validation of a communication protocol used for pre-competitive avionic embedded systems, according to DO-178B avionic software development standards;
  - Developed a web application for controlling, monitoring, optimization, and strategic analysis for smart grids.
  - Developed a desktop application for digital audio processing made for LG. The software is based on a digital processing library written in C/C++ created at CERTI and the graphical interface was made using Qt 4.0. <br>
  - **_Technologies used:_** C (Programming Language) · Redux.js · Redis · C++ · JavaScript · React.js · Node.js · PostgreSQL
<br><br>

## Aditional Experience
---

- **Mentor** _(2021)_: At 3778 I’m responsible for the onboarding of all Platform’s new members and mentoring to some
of its junior engineers;
- **Scrum master** _(2019)_: I was responsible for the agile development process of some teams, using Scrum and Kanban
at CERTI Foundation;
- **Protocol developer** _(2019)_: I developed MQTT and PPP implementations in college, which gave me a background on network protocol design. <br><br>

## Education
---

**Bachelor of Science** in Telecommunication Engineering (unfinished)<br>
[IFSC](https://www.ifsc.edu.br/) - Sao Jose, Santa Catarina, Brazil _(2014 - 2019)_ <br>

**Associate Degree of Technology** in Telecommunications <br>
[IFSC](https://www.ifsc.edu.br/) - Sao Jose, Santa Catarina, Brazil _(2010 - 2013)_ <br>
