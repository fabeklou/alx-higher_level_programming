$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const $lCode = $('INPUT#language_code').val().trim();
    const $url = `https://hellosalut.stefanbohacek.dev/?lang=${$lCode}`;
    $.ajax({
      type: 'GET',
      url: $url,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
