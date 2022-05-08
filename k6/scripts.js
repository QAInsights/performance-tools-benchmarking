import { sleep } from "k6"
import http from "k6/http"
import { randomIntBetween } from 'https://jslib.k6.io/k6-utils/1.2.0/index.js';
// init

export let options = {
  scenarios: {
    contacts: {
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '60s', target: 1000 },
        { duration: '900s', target: 1000 }
      ],
      gracefulRampDown: '0s',
    },
  },
};

//vus
export default function () {
  let res = http.get("https://petclinic.ycrash.io/")
  console.log(res.status)
  sleep(randomIntBetween(1, 5))
}