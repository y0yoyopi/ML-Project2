# Dockerfile para Manim Community con Jupyter
FROM python:3.12-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libcairo2-dev \
    libgirepository1.0-dev \
    pkg-config \
    python3-dev \
    gir1.2-pango-1.0 \
    libpango1.0-dev \
    libgl1-mesa-glx \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /workspace

# Copiar requirements primero (para caché de Docker)
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar manim-jupyter para usar %%manim en notebooks
RUN pip install --no-cache-dir manim-jupyter

# Copiar el resto del proyecto
COPY . .

# Exponer puerto para Jupyter
EXPOSE 8888

# Comando por defecto - ejecutar Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]