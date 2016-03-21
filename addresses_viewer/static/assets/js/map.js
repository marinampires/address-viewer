var map;
var geocoder;
var infowindow;
var layer;
var table_id;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -22.871638, lng: -43.261632},
    zoom: 11
  });

  geocoder = new google.maps.Geocoder;
  infowindow = new google.maps.InfoWindow;

  //Add listener
  google.maps.event.addListener(map, "click", function (event) {
      geocodeLatLng(geocoder, map, infowindow, event.latLng);
  }); //end addListener

  setData();
}

function setData() {
  $.ajax({
    type: "GET",
    url: "http://localhost:8000/get_addresses",
    success: getData
  });
}

function getData(response) {
  var rows = response.rows;

  for (i = 0; i < rows.length; i++) {
    address_name = rows[i][0];

    string_coordinates = rows[i][1].replace("(", "").replace(")", "");
    if(string_coordinates != ""){
      split_coordinates = string_coordinates.split(",");
      lat = parseFloat(split_coordinates[0]);
      lng = parseFloat(split_coordinates[1]);

      addMarker({"lat": lat, "lng": lng}, address_name);  
    }
  }
}


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
  
  $.ajax({
    type: "POST",
    url: "http://localhost:8000/addresses",
    data: data,
    success: function(){
      html = address_name+"<br>";
      $(".list-addresses").append(html);

      map.setZoom(11);
      marker = addMarker({"lat": lat, "lng": lng}, address_name)
      infowindow.setContent(address_name);
      infowindow.open(map, marker);

      setData();

    },
    error: function(response){
      console.log(response.responseText);
    },
    dataType: "json"
  });
}

function clear_data(){
  $.ajax({
    type: "DELETE",
    url: "http://localhost:8000/clear-data",
    success: function(){
      $(".list-addresses").html("");
      setData();
    },
    error: function(response){
      console.log(response.responseText);
    },
  });
}
