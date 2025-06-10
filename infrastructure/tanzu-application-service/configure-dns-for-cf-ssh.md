* Tanzu Application Service ( Tanzu Platform for CF dns records )

review DNS settings
*.apps.<domain> should point to router
ssh.<sys.domain> should point to diego brains (full) or control vm (small)
https://docs.cloudfoundry.org/deploying/common/dns_prereqs.html 

| Domain |	Example	| Notes |
|--------|------------------|-----------------------------------------------------|
| HTTP	| *.apps.example.com	| This handles HTTP traffic destined for the Gorouter. |
| TCP	| *.tcp.example.com	| This handles TCP traffic destined for the TCP Router. |
| HTTP	| *.sys.example.com	| This is the system domain that handles HTTP traffic for system components destined for the Gorouter. |
| HTTP	| *.apps.example.com	| This is the app domain that handles HTTP traffic for applications destined for the Gorouter. |
| SSH	| ssh.sys.example.com	| This is an optional domain that provides SSH access to application containers - directs traffic to diego brains vm (full footprint) or control vm for (small footprint) |

