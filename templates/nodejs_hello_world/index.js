/**
 * A simple Lambda wrapped with Epsagon.
 */

const epsagon = require('epsagon');

epsagon.init({
  token: process.env.EPSAGON_TOKEN,
  appName: process.env.EPSAGON_APP_NAME || 'Default App'
})

// Epsagon simply wraps your function, no other code change is needed!
module.exports.handler = epasgon.lambdaWrapper((event, context, callback) => {

  // Your business logic goes here

  callback(null, 'It Worked!');
})