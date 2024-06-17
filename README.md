### Shell Scripting Sourcing a config file
    Many programs use external configuration files. Use of external configuration files prevents a user from making changes to a script. Config file is added with the help of source command.

### Shell Scripting getopts options
    The getopts options are used in shell scripts to parse arguments passed to them. When arguments are passed on the command line, getopts parse those arguments instead of command lines.




### Multi-stage builds in Dockerfile
    * Multi-stage builds are useful to anyone who has struggled to optimize Dockerfiles while keeping them easy to read and maintain.
    * With multi-stage builds, we use multiple FROM statements in our Dockerfile. Each FROM instruction can use a different base, and each of them begins a new stage of the build. We can selectively copy artifacts from one stage to another, leaving behind everything we don't want in the final image.




### HAProxy
    HAProxy, which stands for High Availability Proxy, is a popular open source software TCP/HTTP Load Balancer and proxying solution which can be run on Linux, macOS, and FreeBSD. Its most common use is to improve the performance and reliability of a server environment by distributing the workload across multiple servers

#### Access Control List (ACL)
    ACLs are used to test some condition and perform an action (e.g. select a server, or block a request) based on the test result. Use of ACLs allows flexible network traffic forwarding based on a variety of factors like pattern-matching and the number of connections to a backend.

#### Backend
    A backend is a set of servers that receives forwarded requests. Backends are defined in the backend section of the HAProxy configuration. A backend can be defined by:
    which load balance algorithm to use
    a list of servers and ports

#### Frontend
    A frontend defines how requests should be forwarded to backends. Frontends are defined in the frontend section of the HAProxy configuration. Their definitions are composed of the following components:
    * a set of IP addresses and a port (e.g. 10.1.1.7:80, *:443, etc.)
    * ACLs
    * use_backend rules, which define which backends to use depending on which ACL conditions are matched, and/or a default_backend rule that handles every other case
auro vila