# Getting Started with k6 - Load Testing Tool
## reference
k6 is a modern load testing tool that allows developers to test the performance of their applications. It is designed to be developer-friendly, with a focus on scripting and automation.

https://k6.io/


## Installation
To get started with k6, you need to install it on your machine. You can do this using various methods depending on your operating system.

## installation reference

https://grafana.com/docs/k6/latest/set-up/install-k6/?pg=get&plcmt=selfmanaged-box10-cta1 

### linux install
```bash
sudo -i
gpg -k
gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | tee /etc/apt/sources.list.d/k6.list
apt-get update
apt-get install k6
```

## write test script
```
touch my-first-test.js
```
### populate the test script
```
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  iterations: 10,
};

// The default exported function is gonna be picked up by k6 as the entry point for the test script. It will be executed repeatedly in "iterations" for the whole duration of the test.
export default function () {
  // Make a GET request to the target URL
  http.get('https://attendees-responsive-ratel-af.apps.agi-explorer.com');

  // Sleep for 1 second to simulate real-world usage
  sleep(1);
}
```

## run test script
```bash
k6 run my-first-test.js
```

## scaling up the test
k6 run --vus 10 --duration 30s my-first-test.js
