var map;
function initMap() {

  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -22.871638, lng: -43.261632},
    zoom: 11
  });

  var layer = new google.maps.FusionTablesLayer({
    query: {
      select: 'Location',
      from: '12a2tPdPOGzY-draRlwRrHtAirL1JC7GUXlqa3e8T'
    }
  });
  layer.setMap(map);


  var geocoder = new google.maps.Geocoder;
  var infowindow = new google.maps.InfoWindow;

  //Add listener
  google.maps.event.addListener(map, "click", function (event) {
      geocodeLatLng(geocoder, map, infowindow, event.latLng);
  }); //end addListener

}

// This function is called when the user clicks the UI button requesting
// a reverse geocode.
function geocodeLatLng(geocoder, map, infowindow, latlng) {
  geocoder.geocode({'location': latlng}, function(results, status) {

    if (status === google.maps.GeocoderStatus.OK) {
      if (results[1] && validate_coordenates(results[1])) {
          //save place id identifier  
          console.log(results[1].place_id);
          map.setZoom(11);
          marker = addMarker(latlng, results[1].formatted_address)
          infowindow.setContent(results[1].formatted_address);
          infowindow.open(map, marker);
      } 
    } else {
      window.alert('Geocoder failed due to: ' + status);
    }
  });
}


function addMarker(latlng, title){
  var marker = new google.maps.Marker({
    position: latlng,
    map: map,
    title: title
  });

  return marker;
}

function validate_coordenates(results){
  if (results.types.indexOf("country") > -1)
    return false;

  return true;
}