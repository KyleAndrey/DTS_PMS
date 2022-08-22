
//BILLING INVOICE FORM

$("#addRowBilling").click(function () {
  var html = '';
  html += '<div id="productRowBilling" class="row reqCard justify-content-between forms">';
  html += '<div class="col-sm-12 col-md-2 col-lg-2">';
  html += '<input class="form-control forms" type="number" min="1" placeholder="Quantity" required>';
  html += '</div>';
  html += '<div class="col-sm-12 col-md-2 col-lg-2">';
  html += '<select id="searchItem" style="width: 100%;" name="item" required>';
  html += '{% for dat in items %}';
  html += '<option value="{{ dat.pk }}">{{ dat.itemName }}</option>';
  html += '{% endfor %}';
  html += '</select>';
  html += '</div>';
  html += '<div class="col-sm-12 col-md-4 col-lg-4">';
  html += '<textarea class="form-control forms" placeholder="Description" required></textarea>';
  html += '</div>';
  html += '<div class="col-sm-12 col-md-2 col-lg-2">';
  html += '<input class="form-control forms" type="number" min="1" placeholder="Price" readonly>';
  html += '</div>';
  html += '<div class="col-sm-12 col-md-2 col-lg-2">';
  html += '<i id="removeRowBilling" class="fa fa-minus-square" aria-hidden="true"></i>';
  html += '</div>';
  html += '</div>';

  $('#newProductRowBilling').append(html);
});

// remove row
$(document).on('click', '#removeRowBilling', function () {
  $(this).closest('#productRowBilling').remove();
});


  
//SALES INVOICE FORM

  $("#addRowSales").click(function () {
    var html = '';
    html += '<div id="productRowSales" class="row reqCard justify-content-between forms">';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<input class="form-control forms" type="number" min="1" placeholder="Quantity" required>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<select class="form-select forms" aria-label="Default select example" required>';
    html += '<option selected disabled>Unit</option>';
    html += '<option value="1">PCS</option>';
    html += '<option value="2">EA</option>';
    html += '<option value="3">UNT</option>';
    html += '<option value="3">SETS</option>';
    html += '</select>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-4 col-lg-4">';
    html += '<textarea class="form-control forms" placeholder="Description" required></textarea>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<input class="form-control forms" type="number" min="1" placeholder="Price" required>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<i id="removeRowSales" class="fa fa-minus-square" aria-hidden="true"></i>';
    html += '</div>';
    html += '</div>';
  
    $('#newProductRowSales').append(html);
  });
  
  // remove row
  $(document).on('click', '#removeRowSales', function () {
    $(this).closest('#productRowSales').remove();
  });



// QUOTATION FORM

  $("#addRowQuotation").click(function () {
    var html = '';
    html += '<div id="productRowQuotation" class="row reqCard justify-content-between forms">';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<input class="form-control" type="number" min="1" placeholder="Item No." required>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<input class="form-control" type="number" min="1" placeholder="Quantity" required>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-4 col-lg-4">';
    html += '<textarea class="form-control" placeholder="Description" required></textarea>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<input class="form-control" type="number" min="1" placeholder="Price" required>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<i id="removeRowQuotation" class="fa fa-minus-square" aria-hidden="true"></i>';
    html += '</div>';
    html += '</div>';
  
    $('#newProductRowQuotation').append(html);
  });
  
  // remove row
  $(document).on('click', '#removeRowQuotation', function () {
    $(this).closest('#productRowQuotation').remove();
  });
  




  //DELIVERY RECEIPT
  $("#addRowDelivery").click(function () {
    var html = '';
    html += '<div id="productRowDelivery" class="row reqCard justify-content-between forms">';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<input class="form-control" type="number" min="1" placeholder="Quantity" required>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<select class="form-select" aria-label="Default select example" required>';
    html += '<option selected disabled>Unit</option>';
    html += '<option value="1">PCS</option>';
    html += '<option value="2">EA</option>';
    html += '<option value="3">UNT</option>';
    html += '<option value="3">SETS</option>';
    html += '</select>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-6 col-lg-6">';
    html += '<textarea class="form-control" placeholder="Description" required></textarea>';
    html += '</div>';
    html += '<div class="col-sm-12 col-md-2 col-lg-2">';
    html += '<i id="removeRowDelivery" class="fa fa-minus-square" aria-hidden="true"></i>';
    html += '</div>';
    html += '</div>';
  
    $('#newProductRowDelivery').append(html);
  });
  
  // remove row
  $(document).on('click', '#removeRowDelivery', function () {
    $(this).closest('#productRowDelivery').remove();
  });