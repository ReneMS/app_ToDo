# Dockerfile para producción
FROM python:3.12-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos de configuración
COPY pyproject.toml uv.lock ./

# Instalar dependencias Python (solo producción)
RUN uv sync --frozen

# Copiar código fuente
COPY . .

# Construir frontend
RUN reflex export --frontend-only

# Exponer puertos
EXPOSE 3000 8000

# Comando de producción
CMD ["reflex", "host"]
