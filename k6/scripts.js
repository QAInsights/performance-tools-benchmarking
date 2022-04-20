import { sleep } from "k6"
import http from "k6/http"

// init 
export let options = {
    vus: 10,
    // duration: '60s',
    scenarios: {
        contacts: {
          executor: 'ramping-vus',
          startVUs: 0,
          stages: [
            { duration: '1s', target: 50 },
            { duration: '10s', target: 50 },
            { duration: '1s', target: 100 },
            { duration: '10s', target: 100 },
            { duration: '1s', target: 150 },
            { duration: '10s', target: 150 },
            { duration: '1s', target: 200 },
            { duration: '10s', target: 200 },
          ],
          gracefulRampDown: '0s',
        },
      },
};

//vus
export default function () {
    let res = http.get("https://petclinic.ycrash.io/")
    console.log(res.status)
    sleep(1)
}