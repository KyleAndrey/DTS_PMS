



  $("#addRowSales").click(function () {
    var html = '';
    html += '<div id="productRowSales" class="row reqCard justify-content-between">';
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
    html += '<i id="removeRowSales" class="fa fa-minus-square forms" aria-hidden="true"></i>';
    html += '</div>';
    html += '</div>';
  
    $('#newProductRowSales').append(html);
  });
  
  // remove row
  $(document).on('click', '#removeRowSales', function () {
    $(this).closest('#productRowSales').remove();
  });
