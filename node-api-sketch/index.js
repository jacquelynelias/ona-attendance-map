'use strict'
//
const fs = require('fs')
const path = require('path')
//
//uncomment these selectively to run later
// getAttendeesInfo()
// pluckLocationData()
//
function getAttendeesInfo() {
  var Twitter = require('twitter');


  var client = new Twitter({
    consumer_key: '',
    consumer_secret: '',
    access_token_key: '',
    access_token_secret: ''
  });

  var params = {screen_name: 'nodejs'};
  client.get('lists/members', {
    slug: 'ona17-attendees1',
    owner_screen_name: 'ONA',
    count: 5000
  }, function(error, tweets, response) {
    if (error) {
      console.log('failed retrieving data!', err)
      return
    }

    fs.writeFileSync(path.join(__dirname, './attendees.json'), JSON.stringify(tweets))

  });
}

function pluckLocationData() {
  const data = require('./attendees.json')
  // to get just the location data:
  const locations = data.users
  .filter((u) => (u.location || '').length)
  .map((u) => u.location)

  fs.writeFileSync(path.join(__dirname, './locations.txt'), locations.join('\n'))
}
