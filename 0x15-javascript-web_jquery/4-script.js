$('DIV#toggle_header').click(function () {
  const $header = $('header');
  if ($header.hasClass('red')) {
    $header.removeClass('red');
    $header.addClass('green');
  } else {
    $header.removeClass('green');
    $header.addClass('red');
  }
});
