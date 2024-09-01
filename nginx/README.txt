# Build Docker image for nginx
docker build -t nginx-app -f nginx/Dockerfile .

# If we want to execute nginx docker image,
docker exec -it container_id sh 
bash is not supported generally, so install "apk add --no-cache bash" inside sh and exit .
use bash normally.

# Check the build path copied to the nginx serve path 
/usr/share/nginx/html