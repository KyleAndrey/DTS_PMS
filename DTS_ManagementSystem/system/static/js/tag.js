var region = "";
var province = "";
var city = "";
var barangay = "";
var tasks = [];
$( document ).ready(function() {
    console.log( "ready!" );
    $('#tableAll').DataTable();
});

// $(document).ready(function () {
//     // Setup - add a text input to each footer cell
//     $('#tableAll tfoot th').each(function () {
//         var title = $(this).text();
//         $(this).html('<input type="text" placeholder="Search ' + title + '" />');
//     });
 
//     // DataTable
//     var table = $('#tableAll').DataTable({
//         initComplete: function () {
//             // Apply the search
//             this.api()
//                 .columns()
//                 .every(function () {
//                     var that = this;
 
//                     $('input', this.footer()).on('keyup change clear', function () {
//                         if (that.search() !== this.value) {
//                             that.search(this.value).draw();
//                         }
//                     });
//                 });
//         },
//     });
// });

$( document ).ready(function() {
    console.log( "ready!" );
    $('#selectTag').select2();
    $('.newProjectTasksSelect2').select2();
    // $('.addProjectTasksSelect2').select2();
});
$('.newProjectTasksSelect2').change(function() {
    tasks = [];
    $('.newProjectTasksSelect2').each(function() {
        tasks = $.merge(tasks,$(this).val());
    });
    $('#newProjectTasks').val(tasks);
});
$('.addProjectTasksSelect2').change(function() {
    tasks = [];
    $('.addProjectTasksSelect2').each(function() {
        tasks = $.merge(tasks,$(this).val());
    });
    $('#addProjectTasks').val(tasks);
});
$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchProjectType').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#addProjectTasksSelect').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchCompany').select2();
    $('#searchClientNewProj').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchCategory').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchCategoryClient').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchContent').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchBusinessStyle').select2();
});

// Address
$( document ).ready(function() {
    console.log( "ready!" );
    region = $('#editregion').val();
    province = $('#editprovince').val();
    city = $('#editcity').val();
    barangay = $('#editbarangay').val();

    $('#searchCompanyRegionEdit').ph_locations({'location_type': 'regions'});
    $('#searchCompanyProvinceEdit').ph_locations({'location_type': 'provinces'});
    $('#searchCompanyMunicipalityEdit').ph_locations({'location_type': 'cities'});
    $('#searchCompanyBarangayEdit').ph_locations({'location_type': 'barangays'});
    $('#searchCompanyRegionEdit').ph_locations('fetch_list');
    $('#searchCompanyRegionEdit').select2();
    $('#searchCompanyProvinceEdit').select2();
    $('#searchCompanyMunicipalityEdit').select2();
    $('#searchCompanyBarangayEdit').select2();

    setTimeout(function (){
        $('#searchCompanyRegionEdit').val(region);;
        $('#searchCompanyRegionEdit').trigger('change');
    }, 120);

    $('#searchCompanyRegion').ph_locations({'location_type': 'regions'});
    $('#searchCompanyProvince').ph_locations({'location_type': 'provinces'});
    $('#searchCompanyMunicipality').ph_locations({'location_type': 'cities'});
    $('#searchCompanyBarangay').ph_locations({'location_type': 'barangays'});
    $('#searchCompanyRegion').ph_locations('fetch_list');
    $('#searchCompanyRegion').select2();
    $('#searchCompanyProvince').select2();
    $('#searchCompanyMunicipality').select2();
    $('#searchCompanyBarangay').select2();
});
$('#searchCompanyRegion').change(function() {
    $('#searchCompanyProvince').ph_locations('fetch_list', [{"region_code": $("#searchCompanyRegion").select2().find(":selected").data("id")}]);
    $('#searchCompanyProvince').val('').trigger('change');
});
$('#searchCompanyProvince').change(function() {
    $('#searchCompanyMunicipality').ph_locations('fetch_list', [{"province_code": $("#searchCompanyProvince").select2().find(":selected").data("id")}]);
    $('#searchCompanyMunicipality').val('').trigger('change');
});
$('#searchCompanyMunicipality').change(function() {
    $('#searchCompanyBarangay').ph_locations('fetch_list', [{"city_code": $("#searchCompanyMunicipality").select2().find(":selected").data("id")}]);
});

$('#searchCompanyRegionEdit').change(function() {
    $('#searchCompanyProvinceEdit').ph_locations('fetch_list', [{"region_code": $("#searchCompanyRegionEdit").select2().find(":selected").data("id")}]);
    setTimeout(function (){
        $('#searchCompanyProvinceEdit').val(province);
        $('#searchCompanyProvinceEdit').trigger('change');
    }, 120);
});
$('#searchCompanyProvinceEdit').change(function() {
    $('#searchCompanyMunicipalityEdit').ph_locations('fetch_list', [{"province_code": $("#searchCompanyProvinceEdit").select2().find(":selected").data("id")}]);
    setTimeout(function (){
        $('#searchCompanyMunicipalityEdit').val(city);
        $('#searchCompanyMunicipalityEdit').trigger('change');
    }, 120);
});
$('#searchCompanyMunicipalityEdit').change(function() {
    $('#searchCompanyBarangayEdit').ph_locations('fetch_list', [{"city_code": $("#searchCompanyMunicipalityEdit").select2().find(":selected").data("id")}]);
    setTimeout(function (){
        $('#searchCompanyBarangayEdit').val(barangay);
        $('#searchCompanyBarangayEdit').trigger('change');
    }, 150);
});
$('#searchClientNewProj').change(function() {
    $('#NewProjTIN').val($("#searchClientNewProj").select2().find(":selected").data("companytin"));
    $('#businessStyleNew').val($("#searchClientNewProj").select2().find(":selected").data("businessstyle"));
    $('#companyaddressNewProj').val($("#searchClientNewProj").select2().find(":selected").data("companyaddress"));
    $('#longaddressNewProj').val($("#searchClientNewProj").select2().find(":selected").data("longadd"));
    $('#ClientNewProjid').val($(this).val());
});
var client = $('#currentClient').data('id');
$('#searchClientNewProj').val(client).trigger('change');

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchItem').select2();
});

$( document ).ready(function() {
    console.log( "ready!" );
    $('#searchUnit').select2();
});