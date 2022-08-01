
$(document).ready(function(){
// Display states for the Country selected
    $('.get-country-data').on('click', function(){

        document.getElementById("city_ul").innerHTML = ""
        var country_id = $(this).attr('data-country');
        var action = $(this).attr('data-action')
        console.log("CountryId:" ,  country_id, "action:" , action)

        req = $.ajax({
            url : "/getcountrydata/",
            type : "POST",
            headers: { "X-CSRFToken": csrftoken},
            data : {'countryid' : country_id, 'action': action}
        })
        .done(function(states){
          if (!$.trim(states)){
            html = '<li class="list-group-item list-group-item-primary">No States Found</li>'

          }
          else
          {
              var html = ""
              $.each(states, function(key, value) {
                html += '<li class="list-group-item list-group-item-primary">' + value.name + ' ' +
                         value.state_code + '<span id="buttonspan">' +
                         '<button data-state=' + value.state_id + ' data-action="state_details" class="rounded-circle details get-state-details">' +
                         '<span id="st-details">More Details</span></button>' +
                         '<button data-state=' + value.state_id + ' data-action="cities" class="rounded-circle data get-state-data">' +
                         '<span id="st-data">Show Cities</span></button></span></li>'
              })
           }
           $("#state_list ul").html(html)

        })
        .fail(function(response){
           console.log(response)
        })

    });

// Display cities for the state selected
    $(document).on("click", ".get-state-data", function(){

            var state_id = $(this).attr('data-state')
            var action = $(this).attr('data-action')
            console.log("StateId:" ,  state_id, "action:" , action)

            req = $.ajax({
                url : "/getstatedata/",
                type : "POST",
                headers: { "X-CSRFToken": csrftoken},
                data : {'stateid' : state_id, 'action': action}
            })
            .done(function(cities){
              if (!$.trim(cities)){
                html = '<li class="list-group-item list-group-item-primary">No Cities Found</li>'

              }
              else
              {
                  var html = ""
                  $.each(cities, function(key, value) {
                    html += '<li class="list-group-item list-group-item-primary">' + value.name +
                             '<span id="buttonspan"><button data-city=' + value.city_id + ' data-action="city_details"' +
                              'class="rounded-circle details get-city-details"><span id="ci-details">More Details</span>' +
                              '</button></span></li>'
                  })
               }
               $("#city_list ul").html(html)
            })
            .fail(function(response){
               console.log(response)
            })

    });

// Search States
    $('#search_state').on("keyup", function(){
        var value = $(this).val().toLowerCase();
        $("#state_ul li").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
       });
    });

//Search Cities
    $('#search_city').on("keyup", function(){
        var value = $(this).val().toLowerCase();
        $("#city_ul li").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
       });
    });

// Display Country Details in Modal
    $('.get-country-details').click(function(){

        var country_id = $(this).attr('data-country');
        var action = $(this).attr('data-action')
        console.log("CountryId:" ,  country_id, "action:" , action)

       // AJAX request
       $.ajax({
        url: '/getcountrydetails/',
        type: 'post',
        dataType: 'json',
        headers: {"X-CSRFToken": csrftoken},
        data : {'countryid' : country_id, 'action': action}
      })
        .done(function(details){
          if (!$.trim(details)){
             alert("No details found!!!!")
          }
          else
          {
              $('.modal-body').html(details);
              $('.modal-title').html(JSON.parse(details)[0]["name"])
              $('#details_modal').modal('show');
          }
        })
        .fail(function(response){
           console.log(response)
        })
     });

// Display State Details in Modal
    $(document).on("click", ".get-state-details", function(){

        var state_id = $(this).attr('data-state');
        var action = $(this).attr('data-action')
        console.log("stateId:" ,  state_id, "action:" , action)

       // AJAX request
       $.ajax({
        url: '/getstatedetails/',
        type: 'post',
        dataType: 'json',
        headers: {"X-CSRFToken": csrftoken},
        data : {'stateid' : state_id, 'action': action}
      })
        .done(function(details){
          if (!$.trim(details)){
             alert("No details found!!!!")
          }
          else
          {
              $('.modal-body').html(details);
              $('.modal-title').html(JSON.parse(details)[0]["name"])
              $('#details_modal').modal('show');
          }
        })
        .fail(function(response){
           console.log(response)
        })
     });

// Display City Details in Modal
    $(document).on("click", ".get-city-details", function(){

        var city_id = $(this).attr('data-city');
        var action = $(this).attr('data-action')
        console.log("cityId:" ,  city_id, "action:" , action)

       // AJAX request
       $.ajax({
        url: '/getcitydetails/',
        type: 'post',
        dataType: 'json',
        headers: {"X-CSRFToken": csrftoken},
        data : {'cityid' : city_id, 'action': action}
      })
        .done(function(details){
          if (!$.trim(details)){
             alert("No details found!!!!")
          }
          else
          {
              $('.modal-body').html(details);
              $('.modal-title').html(JSON.parse(details)[0]["name"])
              $('#details_modal').modal('show');
          }
        })
        .fail(function(response){
           console.log(response)
        })
     });

// Close the Modal
    $(".btn-mod-close").on("click", function (e) {
        e.preventDefault();
        $("#details_modal").modal("hide");
        $('#details_modal').data("modal", null);
    });

//Add tooltip or dynamic Elements
     $(".get-country-details").append("<span id='co-details'>More Details</span>");
     $("#co-details").tooltip();
     $(".get-country-data").append("<span id='state-data'>Show States</span>");
     $("#state-data").tooltip();
     $("#co-data").tooltip();
     $("#st-data").tooltip();
     $("#st-details").tooltip();
     $("#ci-details").tooltip();
});

