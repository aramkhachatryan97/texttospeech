$(document).ready(function () {
    let speedInfoBlock = $(document).find('.speed-info-block')
    let pitchInfoBlock = $(document).find('.pitch-info-block')

    $(document).on('change', '#speed', function () {
        showRangeValue($(this).val(), speedInfoBlock)
    })

    $(document).on('change', '#pitch', function () {
        showRangeValue($(this).val(), pitchInfoBlock)
    })

    $(document).on('change', '#locale', function () {
        let voices = window.options_json[$(this).val()]
        let voice_types_select = $('#voice_type');
        let voice_name_select = $('#voice_name');
        voice_name_select.html('')
        voice_name_select.append("<option value='' selected>Select Voice Name (select language and type at first)</option>")

        if (voices != undefined) {
            voice_types_select.find('option').attr('disabled', 'disabled')
            voice_types_select.find('option:first').removeAttr('disabled').attr('selected', 'selected')
            $.map(voices, function (val) {
                voice_name_select.append("<option value='" + val.name + "'>" + val.name + "</option>")
                if (voice_types_select.find('option[value="' + val.type + '"]').length) {
                    voice_types_select.find('option[value="' + val.type + '"]').removeAttr('disabled')
                }
            });
            $('#voice_type').find('option:selected').removeAttr('selected')
            $('#voice_name').find('option:first').attr('selected', 'selected')
        } else {
            voice_types_select.find('option').removeAttr('disabled')
        }

    })

    $(document).on('change', '#voice_type', function () {
        let voice_name_select = $('#voice_name');
        let locale_select = $('#locale');
        let that = $(this);
        voice_name_select.html('')
        voice_name_select.append("<option value='' selected>Select Voice Name (select language and type at first)</option>")

        if (locale_select.find('option:selected').length) {
            let voices = window.options_json[locale_select.find('option:selected').val()]
            $.map(voices, function (val) {
                if (val.type == that.val()) {
                    voice_name_select.append("<option value='" + val.name + "'>" + val.name + "</option>")
                }
            });
        }
    })

    $(document).on('submit', '#options-form', function () {
        let data = {};
        $(this).find('input, textarea, select').each(function () {
            data[$(this).attr('name')] = $(this).val()
        })
        event.preventDefault()
        $.ajax({
            type: "POST",
            url: "/generate-speech",
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: 'json',
            success: function(data) {
                $('#player').html('').append(data.html)
            }
        });
    })
})

function showRangeValue(value, element) {
    element.text(value)
}