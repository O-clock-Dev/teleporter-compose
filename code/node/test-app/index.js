
const express = require('express')
const app = express()
const port = 3018

app.get('/', (req, res) => {
  res.send(`
  <html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #282a36 ;
        text-align: center;
        padding: 50px;
      }
      .message {
        font-size: 24px;
        color: #50fa7b;
      }
    </style>
  </head>
  <body>
    <div class="message">
      App lancée sur le port ${port}
    </div>
  </body>
</html>
  `)
})

app.listen(port, () => {
  console.log(`Application accessible sur l'adresse http://localhost:${port}`)
})

