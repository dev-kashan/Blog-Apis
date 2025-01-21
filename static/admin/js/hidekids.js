$(document).ready(function () {
    console.log("okk");
    $("#id_height").attr("min", "4").on('input', function() {
        if (parseInt($(this).val()) < 4) {
            $(this).val(4); // Reset to min value if below
        }
    });
    
    const maritalStatusField = $('#id_Marital_status');
    const Gender = $('#id_Gender');
    const kidsFieldWrapper = $('.form-row .field-kids');  // The field wrapper
    const incomeFieldWrapper = $('.form-row.field-Require_income_From.field-Require_income_To');  // The field wrapper
    
    function toggleKidsField() {
        if (maritalStatusField.val() === 'Single') {
            kidsFieldWrapper.hide();
            console.log("If");
        } else {
            kidsFieldWrapper.show();
            console.log("Else");
        }
    }
    function toggleincomeField() {
        if (Gender.val() === 'Male') {
            $("#id_Require_income_From").attr('value' , 0)
            $("#id_Require_income_To").attr('value' , 0)
            incomeFieldWrapper.hide();
            console.log("If gender");
        } else {
            $("#id_Require_income_From").attr('value' , 30000)
            $("#id_Require_income_To").attr('value' , 70000)
            incomeFieldWrapper.show();
            console.log("Else gender");
        }
    }
    // Initial check when the page loads
    
    toggleKidsField();
    toggleincomeField();
    
    // Add event listener for changes
    maritalStatusField.on('change', toggleKidsField);
    Gender.on('change', toggleincomeField);
    // Gender.on('change', toggleincomeField);
});