# Use Nginx to serve the built Flutter web app
FROM nginx:1.25.2-alpine

# Copy the built web app to the Nginx default directory
COPY build/web/* /usr/share/nginx/html

# Expose Nginx port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
