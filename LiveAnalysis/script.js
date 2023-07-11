//create package.json with npm init to track installed modules

//http request to https://coronavirus.m.pipedream.net/ to retureve data

const axios = require('axios');
var fs = require('fs');

var lastUpdated = "";
var rawData;
var dataToWrite = [];

// store data in a file to be accessed by python and juypyter


function appendDataToFile(data) {
  fs.appendFile('myfile.json', JSON.stringify(data) + '\n\n', function (err) {
    if (err) throw err;
    console.log('Data has been appended to the file!');
  });
}

async function getCovidData() {
    try {
        const response = await axios.get('https://coronavirus.m.pipedream.net/');
        if (response.status == 200) {
            console.log("NEW REQUEST");
            rawData =response.data.rawData;
            lastUpdated = response.data.cache.lastUpdated;

            appendDataToFile(rawData);
            //dataToWrite.push(JSON.stringify(rawData));
            //dataToWrite = rawData.slice(0, 10).map(obj => JSON.stringify(obj));
        }
     } catch (error) {
      console.error(error);
    }
}
getCovidData();












