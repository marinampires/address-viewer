var map;

function initMap() {
  var myLatLng = {lat: -25.363, lng: 131.044};

  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });

  addMarker(myLatLng, "Initial");

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
      if (results[1]) {
        map.setZoom(11);
        marker = addMarker(latlng, results[1].formatted_address)
        infowindow.setContent(results[1].formatted_address);
        infowindow.open(map, marker);

      } else {
        window.alert('No results found');
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