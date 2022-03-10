INSTRUCTIONS

1) Build the image:
docker build -t streamlitapp:latest .

2) Run the container:
docker run --rm -p 8501:8501 -v $(pwd)/app:/app streamlitapp:latest
