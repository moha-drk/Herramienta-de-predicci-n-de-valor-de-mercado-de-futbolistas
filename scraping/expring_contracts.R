install.packages("worldfootballR")
devtools::install_github("JaseZiv/worldfootballR")


library(worldfootballR)
library(dplyr)
library(purrr)

# Lista de países
paises <- c("Spain", "Brazil", "Germany", "France", "Italy", "England", "Portugal",
            "Netherlands", "Uruguay", "Belgium", "Colombia", "Chile", "Croatia",
            "Sweden", "Switzerland", "United States", "Austria", "Russia", "Türkiye",
            "Greece", "Ukraine", "Denmark")

# Años de finalización del contrato de interés
contract_end_years <- 2025:2030

# Función para obtener y almacenar los contratos que expiran
get_expiring_contracts <- function(country_name, year) {
  message(paste("Procesando contratos que expiran en", country_name, "para el año", year))
  
  # Extraer los datos de los contratos que expiran
  expiring_contracts <- tryCatch({
    tm_expiring_contracts(country_name = country_name, contract_end_year = year)
  }, error = function(e) {
    message(paste("Error al obtener datos para:", country_name, "en el año", year, "Error:", e$message))
    return(NULL)
  })
  
  # Verificar si hay datos y devolver
  if (!is.null(expiring_contracts) && nrow(expiring_contracts) > 0) {
    expiring_contracts$Country <- country_name  # Añadir una columna con el nombre del país
    expiring_contracts$Year <- year  # Añadir una columna con el año de expiración del contrato
    return(expiring_contracts)
  } else {
    message(paste("No se encontraron datos para:", country_name, "en el año", year))
    return(data.frame())  # Devolver un dataframe vacío en caso de no encontrar datos
  }
}

# Aplicar la función a cada país y año, y combinar los resultados
all_expiring_contracts <- map_df(paises, function(country) {
  map_df(contract_end_years, function(year) {
    get_expiring_contracts(country, year)
  })
})

# Guardar los resultados en un archivo CSV
write.csv(all_expiring_contracts, "expiring_contracts_2025_to_2030.csv", row.names = FALSE)
message("El archivo 'expiring_contracts_2025_to_2030.csv' ha sido creado con éxito.")

