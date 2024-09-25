library(httr)
library(jsonlite)

# Substitua pela sua API Key
api_key <- "fd1f39b9fe572a87292db2bfc4205eb3"
cidade <- commandArgs(trailingOnly = TRUE)[1]

# Requisição para a API
url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", cidade, "&appid=", api_key, "&units=metric")
response <- GET(url)

# Verifique se a requisição foi bem-sucedida
if (status_code(response) == 200) {
  weather_data <- fromJSON(content(response, "text"))
  
  temperatura <- weather_data$main$temp
  Clima <- weather_data$weather[1, "description"]
  umidade <- weather_data$main$humidity
  vento <- weather_data$wind$speed
  
  # Personalizando a descrição
  if (Clima == "broken clouds") {
    Clima <- "nuvens quebradas"
  } else if (Clima == "scattered clouds") {
    Clima <- "nuvens dispersas"
  } else if (Clima == "clear sky") {
    Clima <- "céu limpo"
  } else if (Clima == "few clouds") {
    Clima <- "poucas nuvens"
  } else if (Clima == "shower rain") {
    Clima <- "chuva leve"
  } else if (Clima == "rain") {
    Clima <- "chuva"
  } else if (Clima == "thunderstorm") {
    Clima <- "tempestade"
  } else if (Clima == "mist") {
    Clima <- "neblina"
  }
  
  # Formatar e imprimir os dados
  cat("Temperatura:", temperatura, "C\n")
  cat("Clima:", Clima, "\n")
  cat("Umidade:", umidade, "%\n")
  cat("Velocidade do Vento:", vento, "m/s\n")
} else {
  cat("Erro: Não foi possível obter os dados do tempo. Verifique o nome da cidade ou a chave da API.\n")
}
