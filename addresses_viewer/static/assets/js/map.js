var map;
var geocoder;
var infowindow;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
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


  geocoder = new google.maps.Geocoder;
  infowindow = new google.maps.InfoWindow;

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
          save_address(latlng.lat(), latlng.lng(), results[1].formatted_address)
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

function save_address(lat, lng, address_name){
  data = {"lat": lat.toFixed(6), "lng":lng.toFixed(6), "address_name": address_name}
  console.log(data);
  
  $.ajax({
    type: "POST",
    url: "http://localhost:8000/addresses/",
    data: data,
    success: function(){
      html = address_name + " - "+lat+" - "+lng+"<br>";
      $(".list-addresses").append(html);

      map.setZoom(11);
      marker = addMarker({"lat": lat, "lng": lng}, address_name)
      infowindow.setContent(address_name);
      infowindow.open(map, marker);

    },
    error: function(response){
      console.log(response.responseText);
    },
    dataType: "json"
  });

}