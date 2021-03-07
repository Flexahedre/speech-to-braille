def TextToBraille():
    import requests 
    params = "test from API"
    brailleText= requests.post ("https://api.funtranslations.com/translate/braille, params = params)
   result= request.get_json(cache=True)
   return result