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

  $('INPUT#language_code').on('keypress', function (event) {
    const $lCode = $('INPUT#language_code').val().trim();
    const $url = `https://hellosalut.stefanbohacek.dev/?lang=${$lCode}`;
    if (event.which !== 13) return;
    $.ajax({
      type: 'GET',
      url: $url,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
