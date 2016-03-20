var map;

function initMap() {
  var myLatLng = {lat: -25.363, lng: 131.044};

  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });

  addMarker(myLatLng['lat'], myLatLng['lng'], "Initial");
 
  //Add listener
  google.maps.event.addListener(map, "click", function (event) {
      var latitude = event.latLng.lat();
      var longitude = event.latLng.lng();
      console.log( latitude + ', ' + longitude );
      addMarker(latitude, longitude, "teste");
  }); //end addListener

} 


function addMarker(lat, lng, title){
  var myLatLng = {lat: lat, lng: lng};

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: title
  });

}