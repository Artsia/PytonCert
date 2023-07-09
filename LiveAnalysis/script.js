//create package.json with npm init to track installed modules

//http request to https://coronavirus.m.pipedream.net/ to retureve data

const axios = require('axios');

let lastUpdated = "";
let rawData;


async function getCovidData() {
    try {
        const response = await axios.get('https://coronavirus.m.pipedream.net/');
        if (response.status == 200) {
            console.log("NEW REQUEST");
            rawData =response.data.rawData;
            //console.log(rawData);
            lastUpdated = response.data.cache.lastUpdated;


        }
        
    } catch (error) {
        console.error(error);
    }
}

getCovidData();








// store data in a file to be accessed by python nad juypyter
