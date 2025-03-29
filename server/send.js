fetch('https://bonserver.onrender.com/entries', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        "name" : "cake", 
        "kcal" : 240,
        "servingsize":1,
        "fat":1,
        "satfat":1,
        "tranfat":1,
        "chol":1,
        "sodium" :1,
        "carb": 1,
        "fiber": 1,
        "sugar" : 1,
        "protein": 1,
        "c13": false,
        "c14": false,
        "c15": false,
        "c16": false,
        "c17": false,
        "c18": false,
        "c19": false,
        "c20" : false
      })
  })
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));