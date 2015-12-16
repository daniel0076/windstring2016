$(document).ready(function(){
$('.ui.dropdown').dropdown();

$('.ui.form') .form({
		on:'blur',
    fields: {
      contact: {
        identifier: 'contact',
        rules: [
          {
            type   : 'empty',
            prompt : '聯絡人不得為空'
          }
        ]
      },
      cellphone: {
        identifier: 'cellphone',
        rules: [
          {
            type   : 'regExp[/09[0-9]{8}/]',
            prompt : '輸入正確的電話號碼，比如0987654321'
          }
        ]
      },
      email: {
        identifier: 'email',
        rules: [
          {
            type   : 'email',
            prompt : 'Email格式不正確'
          }
        ]
      },
      fb_url: {
        identifier: 'fb_url',
        rules: [
          {
            type   : 'empty',
            prompt : '請輸入你的FB網址'
          }
        ]
      },
      player1: {
        identifier: 'player1',
        rules: [
          {
            type   : 'empty',
            prompt : '「隊員1」不得為空，至少一個人才能比賽吧'
          }
        ]
      },
      song: {
        identifier: 'song',
        rules: [
          {
            type   : 'empty',
            prompt : '請輸入預賽歌曲名'
          }
        ]
      }
    }
  })
;
})

