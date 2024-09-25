# Valores das áreas de plantio
areas <- c(5000.00, 45000, 19113.45, 7853.98)

# Cálculo da média
media <- mean(areas)

# Cálculo do desvio padrão
desvio_padrao <- sd(areas)

# Cálculo do valor mínimo e máximo
valor_minimo <- min(areas)
valor_maximo <- max(areas)

# Exibir resultados de forma mais detalhada
cat("=== Resultados das Áreas de Plantio ===\n")
cat(sprintf("Média: %.2f m²\n", media))
cat(sprintf("Desvio Padrão: %.2f m²\n", desvio_padrao))
cat(sprintf("Valor Mínimo: %.2f m²\n", valor_minimo))
cat(sprintf("Valor Máximo: %.2f m²\n", valor_maximo))
cat("========================================\n")
