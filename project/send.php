<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<?php
/* Здесь проверяется существование переменных */
if (isset($_POST['name'])) {$phone = $_POST['name'];}
if (isset($_POST['phone'])) {$name = $_POST['phone'];}
if (isset($_POST['email'])) {$name = $_POST['email'];}

$myaddres  = "goroda.tvoego.pyteshestviaya@gmail.com"; // кому отправляем

/* А здесь прописывается текст сообщения, \n - перенос строки */
$mes = "Поиск попутчика!\nТелефон: $phone\nФИО: $name"\nПочта: $email;

/* А эта функция как раз занимается отправкой письма на указанный вами email */
$sub='Бот'; //сабж
$email='Поиск попутчика'; // от кого
$send = mail ($myaddres,$sub,$mes,"Content-type:text/plain; charset = utf-8\r\nFrom:$email");

ini_set('short_open_tag', 'On');
header('Refresh: 3; URL=index.html');
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="refresh" content="3; url=index.html">
<title>Спасибо! Мы свяжемся с вами!</title>
<meta name="generator">
<script type="text/javascript">
setTimeout('location.replace("/index.html")', 5000);
</script>
</head>
<body>
<h1>Спасибо! Мы свяжемся с вами!</h1>
</body>
</html>