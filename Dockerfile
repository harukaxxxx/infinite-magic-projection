# Use Python 3.10.10 as the base image
FROM python:3.10.10

# Set the working directory
WORKDIR /app

# Check if discord_bot.py exists and update the repository if necessary
RUN if [ -f "discord_bot.py" ]; then \
    git -C /app pull origin main; \
    else \
    git clone https://github.com/harukaxxxx/infinite-magic-projection.git /app; \
    fi

# Copy the required files into the container
COPY requirements.txt .
COPY discord_bot.py .

# Install the required packages
RUN pip install -r requirements.txt

# Run your Discord.py application inside the container
CMD [ "python", "discord_bot.py" ]