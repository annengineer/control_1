function changeMoney() {
   var sum = document.getElementById("moneyInput").value;
   var result = "result";

   // Можно ли разменять?
   if (sum % 2 != 0 || sum < 10) {
    result = "Разменять нельзя";
   } else {
    var count500 = Math.floor(sum / 500);
    sum -= count500 * 500;
    var count100 = Math.floor(sum / 100);
    sum -= count100 * 100;
    var count10 = Math.floor(sum / 10);
    sum -= count10 * 10;
    var count2 = sum / 2;

    result += "500 руб.: " + count500 + "<br>";
    result += "100 руб.: " + count100 + "<br>";
    result += "10 руб.: " + count10 + "<br>";
    result += "2 руб.: " + count2 + "<br>";
   }
   document.getElementById("result").innerHTML = result;
  }

   if (result1 = result) {
    result2 = "Ответ верный";
   } else {
    result2 = "Ответ неверный";
   }