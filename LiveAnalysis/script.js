//create package.json with npm init to track installed modules

//http request to https://coronavirus.m.pipedream.net/ to retureve data

const axios = require('axios');
var fs = require('fs');

var lastUpdated = "";
var rawData;
var dataToWrite = [];
const file = "myfile.json"

// store data in a file to be accessed by python and juypyter

/**
 * Method replaces the specified file and content if it exists. 
 * If the file does not exist, a new file, 
 * containing the specified content will be created
 * @param {*} fileName is the file to write to
 * @param {*} data is data that will be written to file called fileName 
 */

function writeToFile(fileName, data){

  fs.writeFile(fileName, JSON.stringify(data) + '\n\n', function (err) {
    if (err) throw err;
    console.log('Saved!');
  });
 
}

/**Read the content within a file
 * Display on console
 * @param {*} fileName is file name to be read 
 */

function readFileContent(fileName) {
  fs.open(fileName, 'r', function (err, file) {
    //if file does not exist throw exception
    if (err) throw err;

    console.log(file);
  });
  
}





/**
 * Appends specified content to a file. 
 * If the file does not exist, the file will be created:
 */
function appendDataToFile(fileName,data) {
  fs.appendFile(fileName, JSON.stringify(data) + '\n\n', function (err) {
    if (err) throw err;
    console.log('Data has been appended to the file!');
  });
}


/**
 * Retrive Data t be analzed and write to a file
 */
async function getCovidData() {
  
    try {
        const response = await axios.get('https://coronavirus.m.pipedream.net/');
        if (response.status == 200) {
            console.log("NEW REQUEST");
            rawData =response.data.rawData;
            lastUpdated = response.data.cache.lastUpdated;
           

            writeToFile(file,rawData);
            readFileContent(file)
            //appendDataToFile(rawData);
            //dataToWrite.push(JSON.stringify(rawData));
            //dataToWrite = rawData.slice(0, 10).map(obj => JSON.stringify(obj));
        }
     } catch (error) {
      console.error(error);
    }
}
getCovidData();












