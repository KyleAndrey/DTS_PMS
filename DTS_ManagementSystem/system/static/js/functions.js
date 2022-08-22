var doneTasks = [];
var undoneTasks = [];
var doneTasksFile = [];
var undoneTasksFile = [];

$(document).ready(function() {
    console.log( "ready!" );
    $('#tableAll').DataTable();
    var type = $('#currentAccountType').data('name');
    $('#accountTypeEdit').val(type);
    var department = $('#currentDepartment').data('name');
    $('#departmentEdit').val(department);
    var unit = $('#currentUnit').data('name');
    $('#unitEdit').val(unit);
});

$('.departmentEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#departmentIDEdit').val(id);
    $('#departmentNameEdit').val(name);
});
$('.departmentDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#departmentIDActive').val(id);
    $('#departmentIDInactive').val(id);
});
$('.businessStyleEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#businessStyleIDEdit').val(id);
    $('#businessStyleNameEdit').val(name);
});
$('.businessStyleDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#businessStyleIDActive').val(id);
    $('#businessStyleIDInactive').val(id);
});
$('.setasactiveClass').click(function() {
    var id = $(this).data('id');
    $('#clientID').val(id);
});
$('.setasinactiveClass').click(function() {
    var id = $(this).data('id');
    $('#clientID').val(id);
});
$('.projectTypeEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#projectTypeIDEdit').val(id);
    $('#projectTypeNameEdit').val(name);
});
$('.projectTypeDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#projectTypeIDActive').val(id);
    $('#projectTypeIDInactive').val(id);
});
$('.setprojasactiveClass').click(function() {
    var id = $(this).data('id');
    $('#projectID').val(id);
});
$('.setprojasinactiveClass').click(function() {
    var id = $(this).data('id');
    $('#projectID').val(id);
});
$('.taskEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    var phase = $(this).data('phase');
    var option = $(this).data('option');
    $('#taskIDEdit').val(id);
    console.log($('#taskIDEdit').val());
    $('#taskNameEdit').val(name);
    $('#taskPhaseEdit').val(phase);
    $('#taskOptionEdit').prop('checked', (option == 'True'));
});
$('.taskDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#taskIDActive').val(id);
    $('#taskIDInactive').val(id);
});
$('.itemEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    var price = $(this).data('price');
    var type = $(this).data('type');
    $('#itemIDEdit').val(id);
    $('#itemNameEdit').val(name);
    $('#itemPriceEdit').val(price);
    $('#itemTypeEdit').val(type);
});
$('.itemDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#itemIDActive').val(id);
    $('#itemIDInactive').val(id);
});
$('.unitEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#unitIDEdit').val(id);
    $('#unitNameEdit').val(name);
});
$('.unitDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#unitIDActive').val(id);
    $('#unitIDInactive').val(id);
});
$('.categoryEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#categoryIDEdit').val(id);
    $('#categoryNameEdit').val(name);
});
$('.categoryDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#categoryIDActive').val(id);
    $('#categoryIDInactive').val(id);
});
$('.contentEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#contentIDEdit').val(id);
    $('#contentNameEdit').val(name);
});
$('.contentDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#contentIDActive').val(id);
    $('#contentIDInactive').val(id);
});
$('.tagEditButton').click(function() {
    var id = $(this).data('id');
    var name = $(this).data('name');
    $('#tagIDEdit').val(id);
    $('#tagNameEdit').val(name);
});
$('.tagDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#tagIDActive').val(id);
    $('#tagIDInactive').val(id);
});
$('.fileDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#fileIDDelete').val(id);
    console.log(id);
});
$('.taskInput').change(function() {
    doneTasks = [];
    undoneTasks = [];
    $('.taskInput').each(function() {
        if($(this).prop('checked')) {
            var tempArr = [];
            tempArr.push($(this).val());
            doneTasks = $.merge(doneTasks,tempArr);
        }else{
            var tempArrNot = [];
            tempArrNot.push($(this).val());
            undoneTasks = $.merge(undoneTasks,tempArrNot);
        }
    });
    $('#doneTasks').val(doneTasks);
    $('#undoneTasks').val(undoneTasks);
});
$('.taskInputFile').change(function() {
    doneTasksFile = [];
    undoneTasksFile = [];
    $('.taskInputFile').each(function() {
        if($(this).prop('checked')) {
            var tempArrFile = [];
            tempArrFile.push($(this).val());
            doneTasks = $.merge(doneTasksFile,tempArrFile);
        }else{
            var tempArrNotFile = [];
            tempArrNotFile.push($(this).val());
            undoneTasksFile = $.merge(undoneTasksFile,tempArrNotFile);
        }
    });
    $('#doneTasksFile').val(doneTasksFile);
    $('#undoneTasksFile').val(undoneTasksFile);
    console.log($('#doneTasksFile').val());
});
$('.taskDeleteButton').click(function() {
    var id = $(this).data('id');
    $('#assignedTaskIDdel').val(id);
});
$('.taskInputFileUp').change(function() {
    if ($(this).get(0).files.length === 0) {
        var id = $(this).data('id');
        $('#fileChk_'+id).prop('checked', false).trigger('change');
    }else{
        $('#file-chosen').val($(this).get(0).files.name);
        var id = $(this).data('id');
        $('#fileChk_'+id).prop('checked', true).trigger('change');
    }
});
$('.taskInputFileUpClear').click(function() {
    var id = $(this).data('id');
    $('#file_'+id).val('').trigger('change');
});
