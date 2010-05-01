// Javascript for skiing-buddy-finder
//
// Copyright 2010 Juha Autero <jautero@iki.fi>
//
//

function array_to_latlng (array) {
    return new google.maps.LatLng(array["latitude"],array["longitude"])
}

function add_marker (map,buddy_name,buddy_position) {
    var buddy_LatLng=array_to_latlng(buddy_position);
    var buddy_marker = new google.maps.Marker({
        position: buddy_LatLng,
        map: map,
        title:buddy_name
    });
    if (buddy_position["message"]) {
        var buddy_infowindow = new google.maps.InfoWindow({
            content: buddy_position["message"]
        });

        google.maps.event.addListener(buddy_marker, 'click', function() {
          buddy_infowindow.open(map,buddy_marker);
        });
    }
    
    
}

function initialize () {
    var map_centre=array_to_latlng(positions['centre']);
    var myOptions = {
      zoom: 8,
      center: map_centre,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    for (k in positions) {
        if ( k != "centre") {
            add_marker(map,k,positions[k]);
        }
    }
}